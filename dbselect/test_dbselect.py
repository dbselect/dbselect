import unittest
from dbselect import dbselect

class TestDBSelect(unittest.TestCase):

    def setUp(self):

        self.dbselect = dbselect.DBSelect(limit=100)


        #table_names
        self.tables = [None,'','employee']

        #empty parameter dict
        self.parameters = [
            None,
            {},
            {'columns': None},
            {'columns': ''},
            {'columns': 'col1,col2,col3'},
            {'columns': ['col1', 'col2', 'col3']}
        ]

    def tearDown(self):
        pass

    def test1(self):
        sql = self.dbselect.generate_select('employee',{})
        self.assertEqual(sql,'select * from employee where rownum <= 100')

    def test2(self):
        sql = self.dbselect.generate_select('employee',{'columns':''})
        self.assertEqual(sql, 'select * from employee where rownum <= 100')

    def test3(self):
        sql = self.dbselect.generate_select('employee',{'columns':None})
        self.assertEqual(sql, 'select * from employee where rownum <= 100')

    def test4(self):
        sql = self.dbselect.generate_select('employee',{'columns':'code'})
        self.assertEqual(sql, 'select code from employee where rownum <= 100')

    def test5(self):
        sql = self.dbselect.generate_select('employee',{'columns':'code,name,description'})
        self.assertEqual(sql,'select code,name,description from employee where rownum <= 100')

    def test22(self):
        sql = self.dbselect.generate_select('employee',{'order_by':''})
        self.assertEqual(sql, 'select * from employee where rownum <= 100')

    def test23(self):
        sql = self.dbselect.generate_select('employee',{'order_by':None})
        self.assertEqual(sql, 'select * from employee where rownum <= 100')

    def test24(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'code'})
        self.assertEqual(sql, 'select * from employee where rownum <= 100 order by code')

    def test25(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'code,name'})
        self.assertEqual(sql,'select * from employee where rownum <= 100 order by code,name')

    def test32(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'','asc_desc':''})
        self.assertEqual(sql, 'select * from employee where rownum <= 100')

    def test33(self):
        sql = self.dbselect.generate_select('employee',{'order_by':None,'asc_desc':None})
        self.assertEqual(sql, 'select * from employee where rownum <= 100')

    def test34(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'code','asc_desc':''})
        self.assertEqual(sql, 'select * from employee where rownum <= 100 order by code')

    def test35(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'code','asc_desc':'asc'})
        self.assertEqual(sql, 'select * from employee where rownum <= 100 order by code asc')

    def test36(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'code,name','asc_desc':'asc,desc'})
        self.assertEqual(sql,'select * from employee where rownum <= 100 order by code asc,name desc')

    def test37(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'code,name','asc_desc':'asc'})
        self.assertEqual(sql,'select * from employee where rownum <= 100 order by code asc,name')

    def test38(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'code','asc_desc':'asc,desc'})
        self.assertEqual(sql,'select * from employee where rownum <= 100 order by code asc')

    def test50(self):
        sql = self.dbselect.generate_select('employee',{'code':'gt,123'})
        self.assertEqual(sql,'select * from employee where rownum <= 100 and code > 123')

    def test51(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'','code':'gt,123'})
        self.assertEqual(sql, 'select * from employee where rownum <= 100 and code > 123')

    def test52(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'','code':'eq,MT'})
        self.assertEqual(sql, "select * from employee where rownum <= 100 and code = 'MT'")

    def test53(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'','code':'in,MT,TD'})
        self.assertEqual(sql, "select * from employee where rownum <= 100 and code in ('MT','TD')")

    def test54(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'','code':'in,MT,TD,AB'})
        self.assertEqual(sql, "select * from employee where rownum <= 100 and code in ('MT','TD','AB')")

    def test55(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'','code':'in,10,20'})
        self.assertEqual(sql, "select * from employee where rownum <= 100 and code in (10,20)")

    def test56(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'','code':'in,10,20,15'})
        self.assertEqual(sql, "select * from employee where rownum <= 100 and code in (10,20,15)")

    def test60(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'','code':'btw,10,20'})
        self.assertEqual(sql, "select * from employee where rownum <= 100 and code between 10 and 20")

    def test61(self):
        sql = self.dbselect.generate_select('employee',{'order_by':'','code':'btw,2008-01-01,2018-12-31'})
        self.assertEqual(sql, "select * from employee where rownum <= 100 and code between '2008-01-01' and '2018-12-31'")


    if __name__ == '__main__':
        unittest.main()