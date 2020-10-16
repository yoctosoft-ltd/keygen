#! python

#  test_key.py: Test key.py
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
"""usage: test_key.py"""

import os
import os.path
import unittest

from keygen import key


class NewPair(unittest.TestCase):
    """Make a new pair of keys."""

    def setUp(self):
        """Make a new pair of keys."""
        key.new_pair('test_public.pem', 'test_private.pem')

    def tearDown(self):
        """Delete the keys."""
        os.remove('test_public.pem')
        os.remove('test_private.pem')

    def test_private(self):
        """Test making the private key."""
        self.assertTrue(os.path.exists('test_private.pem'))

    def test_public(self):
        """Test making the public key."""
        self.assertTrue(os.path.exists('test_public.pem'))


if __name__ == '__main__':
    unittest.main()
