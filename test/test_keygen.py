#! python

#  test_keygen.py: Test the keygen package.
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
"""usage: test_keygen.py"""

import unittest

import keygen


class Metadata(unittest.TestCase):
    """Test the metadata of the package."""

    def test_author(self):
        """Test the author of the package."""
        self.assertEqual('Yoctosoft <info@yoctosoft.co.za>', keygen.__author__)

    def test_version(self):
        """Test the version of the package."""
        self.assertEqual('1.0', keygen.__version__)


if __name__ == '__main__':
    unittest.main()
