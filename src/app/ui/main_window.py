# SkyRenderV1: A real-time skymap application visualizing radio sources.
# Copyright (C) 2024 Shaga Sresthaa
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="SkyRenderV1")
        self.set_default_size(800, 600)
        self.set_position(Gtk.WindowPosition.CENTER)
        label = Gtk.Label(label="Welcome to SkyRenderV1!")
        self.add(label)