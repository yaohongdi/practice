#!/usr/bin/env python
# coding=utf-8
import unittest

from mydict import Dict
class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a =1, b ='test')
        self.assertEqual(d,a,1)
        self.assertEqual(d,b,'test')
        self.assertEqual(isinstance(d,dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d['key'] in d)
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

