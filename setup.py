from setuptools import setup, Extension
import setuptools
import os
import sys

# get __version__, __author__, and __email__
exec(open("./cluedo/metadata.py").read())

with open('requirements.txt','r') as f:
    install_requires = [ s.replace('\n','') for s in f.readlines() ]

setup(
    name='cluedo',
    version=__version__,
    author=__author__,
    author_email=__email__,
    url='https://github.com/noah-jones/cluedo',
    license=__license__,
    description="Encrypt your passwords visually.",
    long_description='',
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
    install_requires=install_requires,
    #tests_require=['pytest', 'pytest-cov'],
    #setup_requires=['pytest-runner'],
    classifiers=['License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3.7'
                 'Programming Language :: Python :: 3.8'
                 'Programming Language :: Python :: 3.9'
                 ],
    project_urls={
        'Documentation': 'TODO',
        'Bug Reports': 'https://github.com/noah-jones/cluedo/issues',
        'Source': 'https://github.com/noah-jones/cluedo/',
    },
    include_package_data=True,
    entry_points = {
            'console_scripts': [
                    'cluedo = cluedo.encrypt:main',
                ],
        },
    zip_safe=False,
)
