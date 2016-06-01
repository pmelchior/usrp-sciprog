'''                                                                                                                            
returns true if the point falls within the unit circle, false otherwise                                                        
'''

def check(x, y):
   if (x*x + y*y)**.5 <=1:
      return True;
   else:
      return False;
