# -*- coding: utf-8 -*-
# :Project:   pycov-mode — Example
# :Created:   mer 8 dic 2021, 11:37:44
# :Author:    Lele Gaifax <lele@etour.tn.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2021 Lele Gaifax
#

def add(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return a + b

def mul(a, b):
    if a is None or b is None:  # pragma: no cover
        return None
    return a * b
