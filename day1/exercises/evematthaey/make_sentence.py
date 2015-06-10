#! /usr/bin/env python                                                                                                        
''' make_sentence.py                                                                                                             takes input from the user to create a sentence and then prints the result                                                                                                         
'''

sen = '';
has_ended = False;
count = 0;
while has_ended == False:
   word = raw_input("Enter a word (. ! or ? to end): ");
   if (word != '.' and word != '!') and word != '?':
      if count == 0:
         sen += word;
      else:
         sen += ' ' + word;
      count += 1;
   else:
      sen += word;
      has_ended = True;
print sen;
