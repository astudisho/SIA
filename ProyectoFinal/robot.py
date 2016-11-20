import math

L1 = L2 = 135

def calculaPosicion( q ):
	q1 = math.radians( q[0] % 360 )
	q2 = math.radians( q[1] % 360 )
	q3 = math.radians( q[2] % 360 )

	particula = ( L1 * math.cos( q2 ) + L2 * math.cos( q2 + q3 ) )

	x =	math.sin( q1 ) * particula
	y =	math.cos( q1 ) * particula
	z = L1 * math.sin( q2 ) + L2 * math.sin( q2 + q3 )

	return (x, y, z)

def calculaError( posicion, posicionDeseada ):
	suma = 	( posicionDeseada[0] - posicion[0] ) ** 2 + \
			( posicionDeseada[1] - posicion[1] ) ** 2 + \
			( posicionDeseada[2] - posicion[2] ) ** 2
	resultado = math.sqrt( suma )
	#print(resultado)
	return 	resultado