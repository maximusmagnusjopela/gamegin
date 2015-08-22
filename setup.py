
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gamegin',
    version='0.1.1',

    description='General purpose library for building board game',
    long_description=long_description,

    url='https://github.com/maximusmagnusjopela/gamegin',

    author='Jonathan Pelletier (maximusmagnusjopela)',
    author_email='jonathan.pelletier1@gmail.com',

    license='GPLv2',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment :: Board Games',

        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='game theory AI',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    entry_points={
        'console_scripts': [
            'play=play:main',
        ],
    },
)
