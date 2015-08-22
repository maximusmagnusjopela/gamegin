#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_unique(coll):
    """ Returns True if the collection contains a unique element. False otherwise."""
    return len(set(coll)) <= 1
