#! /usr/bin/env python

#  test_key.py: Test keys.
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
"""usage: test_keys.py"""

import os
import os.path
import unittest

from keygen import keys


class GenerateLicense(unittest.TestCase):
    """Generate a license key."""

    def setUp(self):
        """Generate a new pair of RSA keys."""
        keys.new_rsa('public.pem', 'private.pem')

    def tearDown(self):
        """Delete the pair of RSA keys."""
        os.remove('public.pem')
        os.remove('private.pem')

    def test_license(self):
        """Test generating a license key."""
        self.assertIsInstance(
            keys.generate_license('info@yoctosoft.co.za', 'private.pem'), str)


class NewRSA(unittest.TestCase):
    """Generate a new pair of RSA keys."""

    def setUp(self):
        """Generate a new pair of RSA keys."""
        keys.new_rsa('public.pem', 'private.pem')

    def tearDown(self):
        """Delete the pair of RSA keys."""
        os.remove('public.pem')
        os.remove('private.pem')

    def test_private(self):
        """Test generating the private RSA key."""
        self.assertTrue(os.path.exists('private.pem'))

    def test_public(self):
        """Test generating the public RSA key."""
        self.assertTrue(os.path.exists('public.pem'))


class Verify(unittest.TestCase):
    """Verify a license key."""

    def setUp(self):
        """Generate a new pair of RSA keys and a license key."""
        keys.new_rsa('public.pem', 'private.pem')
        self.license_key = keys.generate_license(
            'info@yoctosoft.co.za', 'private.pem')

    def tearDown(self):
        """Delete the pair of RSA keys."""
        os.remove('public.pem')
        os.remove('private.pem')

    def test_invalid(self):
        """Test an invalid license key."""
        valid = keys.valid(
            'delvian@yoctosoft.co.za', self.license_key, 'public.pem')
        self.assertFalse(valid)

    def test_valid(self):
        """Test a valid license key."""
        valid = keys.valid(
            'info@yoctosoft.co.za', self.license_key, 'public.pem')
        self.assertTrue(valid)


if __name__ == '__main__':
    unittest.main()
