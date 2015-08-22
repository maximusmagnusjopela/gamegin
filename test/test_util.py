#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

sys.path.append('../gamegin')

import util

class TestUtil:

    def test_is_unique_true(self):
        """ Should return true when coll contains a unique element """

        coll = [1,1,1,1]
        assert util.is_unique(coll)
        return

    def test_is_unique_false(self):
        """ Should return false when a coll does not contain a unique element """

        coll = [1,1,1,1,2]
        assert not util.is_unique(coll)




