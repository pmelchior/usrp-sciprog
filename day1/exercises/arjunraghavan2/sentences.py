# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 14:31:32 2015

@author: arjunr
"""
str=''

while '.' in str or '!' in str or '?' in str:
            inp=raw_input('Enter a word (.,!, or ? to end):')
            str=str+inp
print str

    