from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='ocpp_auth_key',
    version='0.1.0',
    description='OCPP AuthKey',
    author='Kelsey Mok',
    author_email='kelseymok@gmail.com',
    url='https://github.com/kelseymok/ocpp_auth_key',
    packages=find_packages(exclude=('tests')),
    install_requirements=required
)
