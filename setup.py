from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Objectionlol to Txt'
LONG_DESCRIPTION = 'This package is made for the purpose of making objection.lol\'s technical stuff easy'

setup(
        name="objectionloltotxt", 
        version=VERSION,
        author="Plright",
        author_email="plright1@protonmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[],
        keywords=['python', 'objectionlol to txt'],
        classifiers= [
            "Development Status :: 3 Alpha",
            "Intended Audience :: Objection.lol Users",
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Linux",
        ]
)