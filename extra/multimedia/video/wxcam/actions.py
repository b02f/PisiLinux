#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    pisitools.ldflags.add("-pthread")
    autotools.autoreconf("-vif")
    autotools.configure("--with-wx-config=/usr/bin/wxconfig \
                         --disable-silent-rules \
                         --disable-dependency-tracking \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/doc")

    pisitools.dodoc("COPYING")
