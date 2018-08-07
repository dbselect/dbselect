
class DBSelect:

    # list of standard parameters
    STANDARD_PARAMS = ['columns', 'limit', 'order_by', 'asc_desc']

    # list of operators with no operands
    ZERO_OPERAND_OPERATORS = {
        'null': 'is null', 'nnull': 'is not null'
    }

    # list of operators with single operand
    SINGLE_OPERAND_OPERATORS = {
        'gt': '>', 'gte': '>=', 'lt': '<', 'lte': '<=', 'eq': '=', 'neq': '!=',
        'like': 'like', 'nlike': 'not like'
    }

    # list of operators with one or more operands
    MULTIPLE_OPERAND_OPERATORS = {
        'in': 'in', 'nin': 'not in', 'btw': 'between'
    }

    RESERVE_WORDS = ['select','insert','update','delete','drop','grant','create']

    def __init__(self, limit=1000):

        self.LIMIT = limit

    def generate_select(self, table_name, params):
        """generate SQL select statements"""

        # get columns list
        columns = self.get_columns(params)

        # get where clause
        where_clause = self.get_where_clause(params)

        # get order by clause
        order_by_clause = self.get_order_by_clause(params)

        # build sql
        sql = 'select ' + self.clean(columns) + ' from ' + self.clean(table_name) + where_clause + order_by_clause

        print(sql)
        return sql

    def get_columns(self, params):
        """return comma separated column names or * """

        # fetch columns
        columns = params.get('columns')

        # if columns exists
        if columns:

            # create comma separate list of columns
            if type(columns) == list:
                columns = ','.join(columns)

            # do noting
            elif type(columns) == str:
                pass

        # consider all columns
        else:
            columns = '*'

        return columns

    def get_where_clause(self, params):
        """return where clause"""

        # get row limit
        limit = params.get('limit') or self.LIMIT

        #
        where_clause = ' where rownum <= ' + str(limit)

        for key, value in params.items():

            if key not in self.STANDARD_PARAMS:

                if value:

                    # if str then convert to list
                    if type(value)== str:
                        value = value.split(',')

                    # if list length is 1 then zero operand case
                    if len(value) == 1:
                        operator = self.ZERO_OPERAND_OPERATORS.get(value)
                        where_clause = where_clause + ' and ' + key + ' ' + operator

                    # single operand case
                    if len(value) == 2:
                        operator = self.SINGLE_OPERAND_OPERATORS.get(value[0])
                        operand = self.get_value(value[1])
                        where_clause = where_clause +  ' and ' + key + ' ' + operator + ' ' + operand

                    # multiple operands case
                    elif len(value) > 2:

                        operands = ''
                        for val in value[1:]:
                            if operands != '':
                                operands = operands + ','
                            operands = operands + self.get_value(val)

                        if value[0] == 'in':

                            where_clause = where_clause + ' and ' + key + ' in (' + operands + ')'

                        elif value[0] == 'nin':

                            where_clause = where_clause + ' and ' + key + ' not in (' + operands + ')'

                        elif value[0] == 'btw':

                            where_clause = where_clause + ' and ' + key + ' between ' + self.get_value(value[1]) + ' and ' + self.get_value(value[2])

        return where_clause

    def get_order_by_clause(self, params):
        """return order by clause"""

        # initialize
        order_by_clause = ''

        # get order by list
        order_by = params.get('order_by')

        # get asc_desc list
        asc_desc = params.get('asc_desc')

        # order_by exists then create a list
        if order_by:

            order_by_clause = ' order by '
            order_by = order_by.split(',')

            # if asc_desc exists then create a list
            if asc_desc:

                asc_desc = asc_desc.split(',')

            # iterate over the order_by list
            for index in range(0,len(order_by)):

                # if not first item then place a comma separator
                if index == 0:
                    order_by_clause = order_by_clause + order_by[index]
                else:
                    order_by_clause = order_by_clause + ',' + order_by[index]

                # place respective ascending / descending order after order_by column
                if asc_desc and len(asc_desc) > index:

                    order_by_clause = order_by_clause + ' ' + asc_desc[index]

        return order_by_clause

    def get_value(self, text):
        """checks whether the text value is numeric. If not then returns quoted text string else the same text string"""

        if text.isnumeric():

           return text

        else:

           return "'" + text + "'"

    def clean(self,text):
        """removes spaces and reserved words"""
        return text.replace(' ','')