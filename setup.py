from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='leap-sdk',
    version='1.0.17',
    description='LeapCloud Python SDK',

    url='https://leap.as/',

    author='czhou',
    author_email='czhou@ilegendsoft.com',

    license='LGPL',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='Leap SDK',

    packages=['leapcloud'],

    package_dir={'leapcloud':'leapcloud'},

    package_data={'leapcloud':['*.py']},

    test_suite='nose.collector',

    install_requires=[
        'requests',
        'iso8601',
        'arrow',
        'flask',
    ],

    extras_require={
        'dev': ['sphinx'],
        'test': ['nose', 'coverage'],
    },
)
