'''                                                                                                                            
creates a board object based on the input argument of the number of points                                                     
'''

import checkpoint
import genpoint
import matplotlib.pyplot as plt

class Board:

   def __init__(self, n):
      self.n = n;
      self.circlepoints = [];
      self.squarepoints = [];
      self.numcirclepoints = 0;
      self.numsquarepoints = 0;

      for i in range(0, self.n):
         x, y = genpoint.point();
         is_inside = checkpoint.check(x, y);
         if is_inside:
            self.numcirclepoints += 1;
            self.numsquarepoints += 1;
            self.circlepoints.append((x,y));
            self.squarepoints.append((x,y));
         else:
            self.numsquarepoints += 1;
            self.squarepoints.append((x,y));


   def showboard(self):
      ''' creates a plt figure of the board and saves it in current directory'''
      plt.figure();
      x_square = [x[0] for x in self.squarepoints]
      y_square = [x[1] for x in self.squarepoints]
      plt.scatter(x_square, y_square, c='b')
      x_circle = [x[0] for x in self.circlepoints]
      y_circle = [x[1] for x in self.circlepoints]
      plt.scatter(x_circle, y_circle, c='r')
      plt.xlabel('x')
      plt.ylabel('y')
      plt.savefig('board_{}.png'.format(self.n))
      plt.close()


   def calculate_pi(self):
      ''' calculates pi using the board created here '''
      return 4.0 * self.numcirclepoints / self.numsquarepoints
