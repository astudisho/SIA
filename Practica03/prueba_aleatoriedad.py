import random

ITERACIONES = 100000

a = [0] * 11
b = [0] * 11

for i in range( ITERACIONES ):
	a[ int( round( random.random() * random.randint( -5, 5 ) ) ) + 5 ] += 1
	b[ int( round( random.uniform( -5, 5 ) + 5 ) ) ] += 1


print( a )
print( b )