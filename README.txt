# Key Generator

Generate license keys for your app.

![The main window.](keygen/data/images/main.png)

### Installation

From the [Python Package Index](https://pypi.org/project/keygen-yocto/):

    pip install keygen-yocto

or from the source:

    ./setup.py install

### Usage

    keygen

This app uses RSA signature verification to sign the email address of a
user with a private key, then verify the signature with an associated
public key.

1. Generate a new pair of RSA keys.

   ![The New RSA Keys dialog.](keygen/data/images/new_rsa.png)

2. When a user purchases a license, generate a license key and send it
   to the user.

   ![The License Key dialog.](keygen/data/images/license_key.png)

3. In your app, verify that the license key is valid.

       from keygen import keys

        if keys.valid(email, license_key, public_key):
            # The license key is valid.
        else:
            # The license key is invalid.

**Note:** You will have to ship the public RSA key along with your app,
and ship the private RSA key along with this app to your Sales and
Customer Service teams.

### Acknowledgements

This app is based on
[this article](https://build-system.fman.io/generating-license-keys)
by Michael Herrmann @mherrmann

### License

Copyright (c) 2020  Yoctosoft (PTY) Ltd. <info@yoctosoft.co.za>

This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under
certain conditions.
See the [GNU General Public License](https://www.gnu.org/licenses/) for
more details.
