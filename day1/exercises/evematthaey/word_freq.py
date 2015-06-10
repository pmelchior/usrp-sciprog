#! /usr/bin/env python                                                                                                       
                                                                                                                             
''' 
reads in a file (file name given on command line) and returns the most common words and their frequencies
'''

import sys
import operator
import re

fn = sys.argv[1];
fn_nameonly = fn.split('.');
input_file = open(fn, 'r');
input_text = input_file.read();
words = re.split('(( |\n\n)|,)|"', input_text);
wordfreqs = {};

print words

for el in words:
   freq = wordfreqs.get(el, 0);
   wordfreqs[el] = freq + 1;

output_file = open('{}_counts.txt'.format(fn_nameonly[0]), 'w');
sorted_output = sorted(wordfreqs.items(), key=operator.itemgetter(1));
for el in reversed(sorted_output):
   word, freq = el;
   if word is None:
      del word;
   else: 
      if len(word) > 3:
         output_file.write('{}: {}\n'.format(word, freq));
output_file.close();
    
