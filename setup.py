from setuptools import setup
import re
import os
import shutil

# Parse version number from moto-maintenance-python/__init__.py:
with open('motomaintenance/__init__.py') as f:
    info = {}
    for line in f:
        if line.startswith('version'):
            exec(line, info)
            break

# TODO: write a description
long_description = '''

'''

setup(
    name='motormaintenance',
    version=info['version'],
    description='Python Motorcycle Maintenance Finder',
    author='Linas Beresna',
    author_email='linas_beresna@sfu.ca',
    url='https://github.com/LinasBeres/motomaintence',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['motomaintenance'],
)
