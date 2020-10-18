#  key.py: Generate keys and signatures.
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
"""Generate keys and signatures."""

from base64 import b64encode

import rsa


def new_pair(public='public.pem', private='private.pem'):
    """Generate a new pair of keys.

    Args:
        public (str): The path to the public key.
        private (str): The path to the private key.
    """
    pub, pvt = rsa.newkeys(512)
    with open(public, 'wb') as file:
        file.write(pub.save_pkcs1())
    with open(private, 'wb') as file:
        file.write(pvt.save_pkcs1())


def signature(data, key='private.pem'):
    """Return the signature.

    Args:
        data (str): The data to sign.
        key (str): The path to the private key.

    Returns:
        str: The signature
    """
    with open(key, 'rb') as file:
        key = file.read()
    key = rsa.PrivateKey.load_pkcs1(key)
    signature_ = rsa.sign(data.encode(), key, 'SHA-1')
    return b64encode(signature_).decode()
