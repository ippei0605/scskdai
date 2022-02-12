from setuptools import setup

setup(
    name="scskdai",
    version='1.0',
    description='SCSKDAI Common Function',
    author='Ippei Suzuki',
    author_email='ippei0605@gmail.com',
    url='https://github.com/ippei0605/scskdai',
    entry_points = {
        'console_scripts': ['scskdai = scskdai.receipt_cleansing:hello2']
    },
)
