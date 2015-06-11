'''                                                                                                                            
generates random points within the square containing the unit circle (-1, 1, -1, 1)                                                                  
'''

import random

def point():
   x = random.uniform(-1, 1)
   y = random.uniform(-1, 1)
   p = x, y
   return p
