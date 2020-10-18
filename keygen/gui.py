#! python

#  gui.py: The GUI
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
"""usage: gui.py"""

import json
import os
import os.path
import pkg_resources
import sys

from PySide2.QtGui import QGuiApplication, QIcon, QPixmap
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QFileDialog

import keygen
from keygen import key


DATA = pkg_resources.resource_filename(__name__, 'data/')
HOME = os.path.expanduser('~/')
UI = f'{DATA}ui/'
if sys.platform == 'win32':
    CONFIG = f'{os.environ["APPDATA"]}/keygen.json'
else:
    CONFIG = f'{HOME}.config/keygen.json'


def browse_key(dialog):
    """Set the path to the private key.

    Args:
        dialog: The Preferences dialog
    """
    path = QFileDialog.getOpenFileName(
        dialog, dir=HOME, filter='RSA keys (*.pem)')[0]
    if path:
        dialog.line_key.setText(path)


def browse_private(dialog):
    """Set the path to the new private key.

    Args:
        dialog: The New Key Pair dialog
    """
    path = QFileDialog.getSaveFileName(
        dialog, dir=f'{HOME}private.pem', filter='RSA keys (*.pem)')[0]
    if path:
        if not path.endswith('.pem'):
            path += '.pem'
        dialog.line_private.setText(path)


def browse_public(dialog):
    """Set the path to the new public key.

    Args:
        dialog: The New Key Pair dialog
    """
    path = QFileDialog.getSaveFileName(
        dialog, dir=f'{HOME}public.pem', filter='RSA keys (*.pem)')[0]
    if path:
        if not path.endswith('.pem'):
            path += '.pem'
        dialog.line_public.setText(path)


def copy_signature(dialog):
    """Copy the signature to the clipboard.

    Args:
        dialog: The Signature dialog
    """
    clipboard = QGuiApplication.clipboard()
    signature = dialog.label_signature.text()
    clipboard.setText(signature)


def new_pair(ui_loader, window):
    """Show the New Key Pair dialog.

    Args:
        ui_loader: The UI loader
        window: The main window
    """
    dialog = ui_loader.load(f'{UI}new_pair.ui', window)
    dialog.button_public.clicked.connect(lambda: browse_public(dialog))
    dialog.button_private.clicked.connect(lambda: browse_private(dialog))
    if dialog.exec_():
        key.new_pair(dialog.line_public.text(), dialog.line_private.text())


def show_about(ui_loader, window):
    """Show the About dialog.

    Args:
        ui_loader: The UI loader
        window: The main window
    """
    dialog = ui_loader.load(f'{UI}about.ui', window)
    dialog.label_logo.setPixmap(QPixmap(f'{DATA}logo.png'))
    dialog.label_version.setText(keygen.__version__)
    dialog.label_description.setText(keygen.__doc__)
    dialog.label_copy.setOpenExternalLinks(True)
    dialog.exec_()


def show_preferences(ui_loader, window):
    """Show the Preferences dialog.

    Args:
        ui_loader: The UI loader
        window: The main window
    """
    dialog = ui_loader.load(f'{UI}preferences.ui', window)
    dialog.line_key.setText(ui_loader.config['key'])
    dialog.button_browse.clicked.connect(lambda: browse_key(dialog))
    if dialog.exec_():
        ui_loader.config['key'] = dialog.line_key.text()
        with open(CONFIG, 'w') as file:
            json.dump(ui_loader.config, file)


def show_signature(ui_loader, window):
    """Show the Signature dialog.

    Args:
        ui_loader: The UI loader
        window: The main window
    """
    data = window.line_email.text()
    signature = key.signature(data, ui_loader.config['key'])
    dialog = ui_loader.load(f'{UI}signature.ui', window)
    dialog.label_signature.setText(signature)
    dialog.button_copy.clicked.connect(lambda: copy_signature(dialog))
    dialog.exec_()


def main():
    """Run the app."""
    app = QApplication([])
    ui_loader = QUiLoader()
    if os.path.exists(CONFIG):
        with open(CONFIG) as file:
            ui_loader.config = json.load(file)
    else:
        ui_loader.config = {'key': 'private.pem'}
    window = ui_loader.load(f'{UI}main.ui', None)
    window.setWindowIcon(QIcon(f'{DATA}icon.png'))
    window.action_new_pair.triggered.connect(
        lambda: new_pair(ui_loader, window))
    window.action_preferences.triggered.connect(
        lambda: show_preferences(ui_loader, window))
    window.action_about.triggered.connect(lambda: show_about(ui_loader, window))
    window.button_sign.clicked.connect(
        lambda: show_signature(ui_loader, window))
    window.line_email.textChanged.connect(
        lambda: window.button_sign.setEnabled(window.line_email.text() != ''))
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
