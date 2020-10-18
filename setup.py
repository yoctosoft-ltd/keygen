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


if __name__ == '__main__':
    setup(
        name='Key Generator',
        version=keygen.__version__,
        packages=['keygen'],
        url='https://www.yoctosoft.co.za',
        license='GNU General Public License (GPL)',
        author='Yoctosoft',
        author_email='info@yoctosoft.co.za',
        description=keygen.__doc__,
        long_description=readme(),
        long_description_content_type='text/markdown',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: MacOS X',
            'Environment :: Win32 (MS Windows)',
            'Environment :: X11 Applications',
            'Intended Audience :: Customer Service',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Natural Language :: English',
            'Operating System :: MacOS :: MacOS X',
            'Operating System :: Microsoft :: Windows :: Windows 10',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3.8',
            'Topic :: Security',
            'Topic :: Utilities'],
        keywords='key generator',
        install_requires=['rsa', 'PySide2'],
        python_requires='>=3.8',
        entry_points={'gui_scripts': ['keygen = keygen.gui:main']})
