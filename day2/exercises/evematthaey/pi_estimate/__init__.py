''' 
the presence of this file tells python to treat the pi_estimate directory
as a package rather than simply a directory.  it also functions the way a java Main does (?)
''' 

import numpy as np
import matplotlib.pyplot as plt
import board
import genpoint
import checkpoint
import stats

stats.testn(1000, 1000)
testboard = board.Board(10000)
testboard.showboard()
stats.accuracy()
