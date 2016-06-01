#!/usr/bin/env python
# coding: utf-8

from __future__ import division

sentence = []
while not any(word in sentence for word in ['.', '!', '?']):
    word = raw_input('Enter a word (. ! or ? to end):')
    sentence += word
    sentence += (' ')
print ''.join(sentence)