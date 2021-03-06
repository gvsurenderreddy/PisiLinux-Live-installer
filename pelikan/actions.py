#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools


def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Debug \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DWITH_PARTITIONMANAGER=1 \
                          -DCMAKE_INSTALL_LIBDIR=lib \
                          -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
                          ")
    
def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    
    pisitools.remove("/usr/bin/calamares")
    pisitools.dodoc("README.*")