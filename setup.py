from setuptools import setup, find_packages

setup(
    name='ocpp_auth_key',
    version='0.1.0',
    description='OCPP AuthKey',
    author='Kelsey Mok',
    author_email='kelseymok@gmail.com',
    url='https://github.com/kelseymok/ocpp-auth-key',
    packages=find_packages(exclude=('tests'))
)
