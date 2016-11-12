import math

L1 = L2 = 135

def fitness(q1,q2,q3):
	q1 = math.radians( q1 )
	q2 = math.radians( q2 )
	q3 = math.radians( q3 )

	particula = ( L1 * math.cos( q2 ) + L2 * math.cos( q2 + q3 ) )

	x =	math.sin( q1 ) * particula
	y =	math.cos( q1 ) * particula
	z = L1 * math.sin( q2 ) + L2 * math.sin( q2 + q3 )

	return (x, y, z)

print( fitness( 0, 0, 0) )
print( fitness( 90, 0, 0) )
print( fitness( 0, 90, 0) )
print( fitness( 0, 0, 90) )
print( fitness( 180, 0, 0) )
print( fitness( 0, 180, 0) )
print( fitness( 0, 0, 180) )