# -*- coding: utf-8 -*-
# :Project:   pycov-mode —
# :Created:   mer 8 dic 2021, 11:39:02
# :Author:    Lele Gaifax <lele@etour.tn.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2021 Lele Gaifax
#

import pytest

import module

@pytest.mark.parametrize('a, b, expected', ((1, 2, 3),
                                            (None, None, None),
                                            (None, 1, 1)))
def test_add(a, b, expected):
    assert module.add(a, b) == expected
