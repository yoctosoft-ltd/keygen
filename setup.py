#! python

#  setup.py: Build/install the app.
#  Copyright (c) 2020  Yoctosoft (PTY) Ltd. <info@yoctosoft.co.za>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""usage: setup.py build|install"""

from setuptools import setup

import keygen


def readme():
    """Return the README file."""
    with open('README.txt') as file:
        return file.read()


setup(
    name='keygen-yocto', version=keygen.__version__, packages=['keygen'],
    url='https://github.com/yoctosoft-ltd/keygen',
    license='GNU General Public License (GPL)', author='Yoctosoft',
    author_email='info@yoctosoft.co.za', description=keygen.__doc__,
    long_description=readme(), long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.8',
        'Topic :: Security',
        'Topic :: Utilities'],
    keywords='key generator', install_requires=['rsa', 'PySide2'],
    python_requires='>=3.8',
    package_data={'keygen': [
        'data/icon.png', 'data/logo.png', 'data/ui/about.ui',
        'data/ui/main.ui', 'data/ui/new_pair.ui', 'data/ui/preferences.ui',
        'data/ui/signature.ui']},
    data_files=[('.', ['private.pem', 'public.pem'])],
    entry_points={'gui_scripts': ['keygen = keygen.gui:main']})
