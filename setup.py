from setuptools import setup, find_packages
from os.path import basename
from os.path import splitext
from glob import glob

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='ocpp_auth_key',
    version='0.1.0',
    description='OCPP AuthKey',
    author='Kelsey Mok',
    author_email='kelseymok@gmail.com',
    url='https://github.com/kelseymok/ocpp_auth_key',
    packages=find_packages('src', exclude=('tests')),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    install_requirements=required
)
