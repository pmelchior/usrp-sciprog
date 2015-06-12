import pi_estimate as pe
import pi_estimate.singleTest as sT
import pi_estimate.multiTest as mT

#a = sT.singleTest(100)
#a.dartplot()

Nlist = [100, 1000, 50000]

b = mT.multiTest(Nlist)
b.plotprecision_N()
