from math import sqrt

fi = open('./input.txt', 'r')
inp = fi.read().split()
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])

x=(a**2-c**2+b**2)/2*b
y=sqrt(a**2-x**2)

newX = x/2.0
newY = y/2.0

newB = b/2.0
newA = sqrt((newX-newB)**2+newY**2)
newC = sqrt((((newX+b)/2.0)-newB)**2+newY**2)

result = (newA+newB+newC)/3.0

fo = open('./output.txt', 'w')
fo.write(str(result))
