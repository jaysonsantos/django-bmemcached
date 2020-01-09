from setuptools import setup

setup(
    name='django-bmemcached',
    version='0.3.0',
    author='Jayson Reis',
    author_email='santosdosreis@gmail.com',
    description='A Django cache backend to use bmemcached module which ' +
                'supports memcached binary protocol with authentication.',
    url='https://github.com/jaysonsantos/django-bmemcached',
    packages=['django_bmemcached'],
    install_requires=['python-binary-memcached'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
