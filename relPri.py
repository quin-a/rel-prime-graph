import sys
import numpy as np
import matplotlib.pyplot as plt

def inc_tup(a,b):
	if a <= b:
		return (a,b)
	else:
		return (b,a)

def np_gcd(a,b):
	s,l = inc_tup(a,b)
	if s == 0:
		return 0
	else:
		r = l % s	
		while r > 0:
			l = s
			s = r
			r = l % s
		return s

x0 = 0
y0 = 0

try:
    x1 = int(sys.argv[1])
    y1 = int(sys.argv[1])
except (ValueError, IndexError):
    x1 = 10
    y1 = 10
try:
    y1 = int(sys.argv[2])
except ValueError:
    y1 = 10
except IndexError:
    pass
    
if len(sys.argv) > 4:
    try:
        s = int(sys.argv[3])
        t = int(sys.argv[4])
        x0 = x1
        x1 = y1
        y0 = s
        y1 = t
    except (ValueError, IndexError):
        pass

ylist = [y0]
xlist = [x0]

for y in range(y0,y1):
    for x in range(x0,x1):
        if np_gcd(x,y) == 1:
            xlist = xlist + [x]
            ylist = ylist + [y]

plt.plot(xlist,ylist, marker='.', ls='', c='r')
plt.yticks(np.arange(y0,y1))
plt.xticks(np.arange(x0,x1))
plt.grid(ls='--')
plt.show()
