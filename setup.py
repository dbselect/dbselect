import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dbselect",
    version="0.0.5",
    author="mmoiz",
    author_email="moizmuhammad@yahoo.com",
    description="Generate SQL select statement for given parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dbselect/dbselect",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
