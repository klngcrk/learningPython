#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys 
import io

s = sys.stdout
stream = io.StringIO()
sys.stdout = stream

import hello_world

sys.stdout = s
received = stream.getvalue()

expected = 'Hello world! Nazywam się'
assert  expected in received, "Oczekiwano tekstu zawierajacego\n'{}'\n, a otrzymano:\n'{}'".format(expected,  received if received else 'Pusty tekst')
print("Success!")