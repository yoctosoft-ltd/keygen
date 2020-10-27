#  gui.py: The GUI.
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
"""The GUI.

Todo:
    * Verify license keys.
    * Show a list of license keys that was generated.
"""

import json
import os
import os.path
import pkg_resources
import sys

from PySide2.QtGui import QGuiApplication, QIcon, QPixmap
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QDialogButtonBox, QFileDialog

import keygen
from keygen import keys


DATA = pkg_resources.resource_filename(__name__, 'data/')
HOME = os.path.expanduser('~/')
CONFIG = (
    f'{os.environ["APPDATA"]}/keygen2.json' if sys.platform == 'win32'
    else f'{HOME}.config/keygen2.json')
CONFIG_OLD = (
    f'{os.environ["APPDATA"]}/keygen.json' if sys.platform == 'win32'
    else f'{HOME}.config/keygen.json')
IMAGES = f'{DATA}images/'
UI = f'{DATA}ui/'


def about(ui_loader, window):
    """Show the About dialog.

    Args:
        ui_loader: The UI loader.
        window: The main window.
    """
    dialog = ui_loader.load(f'{UI}about.ui', window)
    dialog.label_logo.setPixmap(QPixmap(f'{IMAGES}logo.png'))
    dialog.label_version.setText(keygen.__version__)
    dialog.label_description.setText(keygen.__doc__)
    dialog.label_copyright.setOpenExternalLinks(True)
    dialog.exec_()


def browse_private_open(window):
    """Set the path to the private RSA key for generating license keys.

    Args:
        window: The main window.
    """
    if path := QFileDialog.getOpenFileName(
            window, dir=HOME, filter='RSA keys (*.pem)')[0]:
        window.line_private.setText(path)
        config = preferences()
        config['private_key'] = path
        save_preferences(config)


def browse_private_save(dialog):
    """Set the path to the new private RSA key.

    Args:
        dialog: The New Key Pair dialog.
    """
    if path := QFileDialog.getSaveFileName(
            dialog, dir=f'{HOME}private.pem', filter='RSA keys (*.pem)')[0]:
        if not path.endswith('.pem'):
            path = ''.join([path, '.pem'])
        dialog.line_private.setText(path)


def browse_public_save(dialog):
    """Set the path to the new public RSA key.

    Args:
        dialog: The New Key Pair dialog.
    """
    if path := QFileDialog.getSaveFileName(
            dialog, dir=f'{HOME}public.pem', filter='RSA keys (*.pem)')[0]:
        if not path.endswith('.pem'):
            path = ''.join([path, '.pem'])
        dialog.line_public.setText(path)


def copy_license(dialog):
    """Copy the license key to the clipboard.

    Args:
        dialog: The License Key dialog.
    """
    clipboard = QGuiApplication.clipboard()
    clipboard.setText(dialog.label_license.text())


def generate_license(ui_loader, window):
    """Generate a license key.

    Args:
        ui_loader: The UI loader.
        window: The main window.
    """
    dialog = ui_loader.load(f'{UI}license_key.ui', window)
    license_key = keys.generate_license(
        window.line_email.text(), window.line_private.text())
    dialog.label_license.setText(license_key)
    dialog.button_copy.clicked.connect(lambda: copy_license(dialog))
    dialog.exec_()


def new_rsa(ui_loader, window):
    """Generate a new pair of RSA keys.

    Args:
        ui_loader: The UI loader.
        window: The main window.
    """
    dialog = ui_loader.load(f'{UI}new_rsa.ui', window)
    dialog.button_box.button(QDialogButtonBox.Save).setDisabled(True)
    dialog.button_public.clicked.connect(lambda: browse_public_save(dialog))
    dialog.button_private.clicked.connect(lambda: browse_private_save(dialog))
    dialog.line_public.textChanged.connect(lambda: validate_new_pair(dialog))
    dialog.line_private.textChanged.connect(lambda: validate_new_pair(dialog))
    if dialog.exec_():
        keys.new_rsa(dialog.line_public.text(), dialog.line_private.text())


def preferences():
    """Load the preferences of the app.

    Returns:
        dict: The preferences of the app.
    """
    if os.path.exists(CONFIG):
        with open(CONFIG) as file:
            return json.load(file)
    else:
        return {'private_key': ''}


def save_preferences(config):
    """Save the preferences of the app.

    Args:
        config (dict): The preferences of the app.
    """
    with open(CONFIG, 'w') as file:
        json.dump(config, file)


def validate_main(window):
    """Validate the input of the main window.

    Args:
        window: The main window.
    """
    window.button_license.setEnabled(
        window.line_private.text() != '' and window.line_email.text() != '')


def validate_new_pair(dialog):
    """Validate the input of the New Pair dialog.

    Args:
        dialog: The New Pair dialog.
    """
    dialog.button_box.button(QDialogButtonBox.Save).setEnabled(
        dialog.line_public.text() != '' and dialog.line_private.text() != '')


def main():
    """Run the app."""
    if os.path.exists(CONFIG_OLD):
        os.remove(CONFIG_OLD)
    app = QApplication([])
    ui_loader = QUiLoader()
    window = ui_loader.load(f'{UI}main.ui', None)
    window.setWindowIcon(QIcon(f'{IMAGES}icon.ico'))
    private_key = preferences()['private_key']
    if private_key and os.path.exists(private_key):
        window.line_private.setText(private_key)
    window.button_private.clicked.connect(
        lambda: browse_private_open(window))
    window.button_license.clicked.connect(
        lambda: generate_license(ui_loader, window))
    window.line_private.textChanged.connect(lambda: validate_main(window))
    window.line_email.textChanged.connect(lambda: validate_main(window))
    window.action_new_pair.triggered.connect(
        lambda: new_rsa(ui_loader, window))
    window.action_about.triggered.connect(lambda: about(ui_loader, window))
    window.show()
    app.exec_()
