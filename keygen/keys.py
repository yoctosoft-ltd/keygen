#  keygen.py: Generate license keys for your app.
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
"""A simple tool to generate and verify license keys for your app.

This app uses RSA signature verification to sign the email address of a
user with a private key, then verify the signature with an associated
public key.

First generate a new pair of RSA keys with ``new_rsa()``.

When a user purchases a license, generate a license key with
``generate_license()`` and send it to the user.

In your app, verify the license key with ``valid()``.  You will have to
ship the public RSA key with your app.
"""

from base64 import b64decode, b64encode

import rsa


def generate_license(email, private_key):
    """Generate a license key.

    Sign the email address of the user with the private RSA key.

    Args:
        email (str): The email address of the user.
        private_key (str): The path to the private RSA key.

    Returns:
        str: The license key.
    """
    with open(private_key, 'rb') as file:
        key = rsa.PrivateKey.load_pkcs1(file.read())
    return b64encode(rsa.sign(email.encode(), key, 'SHA-1')).decode()


def new_rsa(public_key, private_key):
    """Generate a new pair of RSA keys.

    Args:
        public_key (str): The path to the public RSA key.
        private_key (str): The path to the private RSA key.
    """
    public, private = rsa.newkeys(512)
    with open(public_key, 'wb') as file:
        file.write(public.save_pkcs1())
    with open(private_key, 'wb') as file:
        file.write(private.save_pkcs1())


def valid(email, license_key, public_key):
    """Verify the license key.

    Verify the license key with the email address of the user and the
    public RSA key.

    Args:
        email (str): The email address of the user.
        license_key (str): The license key of the user.
        public_key (str): The path to the public RSA key.

    Returns:
        bool: True if the license key is valid, otherwise False.
    """
    with open(public_key, 'rb') as file:
        key = rsa.PublicKey.load_pkcs1(file.read())
    try:
        rsa.verify(email.encode(), b64decode(license_key), key)
    except rsa.VerificationError:
        return False
    else:
        return True
