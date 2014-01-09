from setuptools import setup
setup(
    name='django-bmemcached',
    version='0.2.1',
    author='Jayson Reis',
    author_email='santosdosreis@gmail.com',
    description='A Django cache backend to use bmemcached module which ' + \
        'supports memcached binary protocol with authentication.',
    url='https://github.com/jaysonsantos/django-bmemcached',
    packages=['django_bmemcached'],
    install_requires=['python-binary-memcached'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
