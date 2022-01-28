from platform import python_version
from public import install
from setuptools import setup

with open('README.md',"r",encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'src'
    ,version='0.0.1'
    ,author='Dipendra Pratap'
    ,description='A small package for dvc ml pipeline demo'
    ,long_description=long_description
    ,long_description_content_type="text/markdown"
    ,url='https://github.com/dipdregan/DVC_ML_BASICE'
    ,author_email='dipendrapratap155@gmail.com'
    ,packages=['src']
    ,python_requires=">3.7"
    ,install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]


)