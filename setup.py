"""Setup module for PyLink IRC Services."""

from setuptools import setup, find_packages
from codecs import open
import subprocess
from os import path

# Get version from Git tags.
try:
    version = subprocess.check_output(['git', 'describe', '--tags']).decode('utf-8').strip()
except Exception as e:
    print('ERROR: Failed to get version from "git describe --tags": %s: %s' % (type(e).__name__, e))
    from __init__ import __version__ as fallback_version

    # Mark builds with unretrievable version (GitHub tarballs, etc.) as -dirty
    if not fallback_version.endswith('-dirty'):
        fallback_version += '-dirty'

    print('Using fallback version of %r.' % fallback_version)
    version = fallback_version

# Write the version to disk.
with open('__init__.py', 'w') as f:
    f.write('# Automatically generated by setup.py\n')
    f.write('__version__ = %r\n' % version)

curdir = path.abspath(path.dirname(__file__))

# FIXME: Convert markdown to RST
with open(path.join(curdir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pylinkirc',
    version=version,

    description='PyLink IRC Services',
    long_description=long_description,

    url='https://github.com/GLolol/PyLink',

    # Author details
    author='James Lu',
    author_email='GLolol@overdrivenetworks.com',

    # Choose your license
    license='MPL 2.0',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='IRC services chat',
    install_requires=['pyyaml'],

    # Folders (packages of code)
    packages=['pylinkirc', 'pylinkirc.protocols', 'pylinkirc.plugins', 'pylinkirc.coremods'],

    # Data files
    package_data={
        '': ['example-conf.yml'],
    },

    package_dir = {'pylinkirc': '.'},

    # Executable scripts
    scripts=["pylink"],
)
