# Key Generator

A simple tool to generate and verify license keys for your app.

This app uses RSA signature verification to sign the email address of a user
with a private key, then verify the signature with an associated public key.

![The main window.](keygen/data/images/main.png)

## Installation

From the [Python Package Index](https://pypi.org/project/keygen-yocto/):

```bash
pip install keygen-yocto
```

or from the source:

```bash
./setup.py install
```

### Requirements

*   [Python](https://www.python.org/)

## Usage

```bash
keygen
```

1.  Generate a new pair of RSA keys.

    ![The New RSA Keys dialog.](keygen/data/images/new_rsa.png)

    **Note:** You will only have to do this once.

2.  When a user purchases a license, generate a license key and send it to the
    user.

    ![The License Key dialog.](keygen/data/images/license_key.png)

    **Note:** Sales and Customer Service teams will only have to do this step.
    You will have to ship the private RSA key with this app to them.

3.  In your app, verify that the license key is valid.

    ```python
    from keygen import keys

    if keys.valid('email', 'license_key', 'public_key'):
        pass    # The license key is valid.
    else:
        pass    # The license key is invalid.
    ```

    **Note:** You will have to ship the public RSA key with your app.

## Support

Email [info@yoctosoft.co.za](mailto:info@yoctosoft.co.za) for help.

## Roadmap

1.  Verify license keys in the GUI.
2.  Show a list of license keys that was generated.

## Contributing

Pull requests are welcome.  For major changes, please open an issue first to
discuss what you would like to change.

Please make sure to update tests as appropriate.

## Acknowledgements

*   Based on
    [this article](https://build-system.fman.io/generating-license-keys).

*   [Python-RSA](https://stuvel.eu/software/rsa/) for generating and verifying
    the keys.

*   [Qt for Python](https://wiki.qt.io/Qt_for_Python) for the GUI.

## License

Copyright (c) 2020  Yoctosoft (PTY) Ltd.
[info@yoctosoft.co.za](mailto:info@yoctosoft.co.za)

This program comes with ABSOLUTELY NO WARRANTY.  This is free software, and you
are welcome to redistribute it under certain conditions. See the
[GNU General Public License](https://www.gnu.org/licenses/) for more details.
