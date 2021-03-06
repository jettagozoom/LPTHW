# -*- coding: utf-8 -*-
PI = 3.14159265359
places = 6
print "Print PI to %d decimals: %0.*f" % (places,places,PI)

pf = '%0.*f' % (places,PI)
print "Print PI to %d decimals: %s" % (places,pf)
print "Print PI to %d decimals: %r" % (places,pf)

# Using new string.format(). I love it. I don't need to use 'places' twice
# in the variable list.
print "Print PI to {0} decimals: {1:.{0}f}".format(places,PI)
# Use named arguments
print "Print PI to {pl} decimals: {pi:.{pl}f}".format(pl=places,pi=PI)
# Use format as a function: separate the formatting from the data
myformat = "Print PI to {pl} decimals: {pi:.{pl}f}".format
print myformat(pl=places, pi=PI)
print myformat(pl=4, pi=3.14159265359)
myformat2 = "Print 2PI*{1} to {0} decimals: {2:.{0}f}".format
r = 15
print myformat2(4, r, PI*2*r)

