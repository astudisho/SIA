import random, math

VALOR_INICIAL = 0
NUMERO_HORMIGAS = NUMERO_CIUDADES = 16

GENERACIONES = 20
ALFA = 1
BETA = 5
Q_DEPOSITO = 20
P_EVAPORACION = 0.9
PI_0 = 10e-6

class Camino(object):
	"""docstring for Camino"""
	def __init__(self, distancia, ):ff
		super(Camino, self).__init__()
		self.__distancia = distancia
		self.__feromonas = PI_0

	def __str__(self): return "Dst: " + str( round( self.__distancia , 3 ) ) + " Fer: " + str(self.__feromonas)

	def getDistancia( self ):	return self.__distancia
	def getFeromona( self ): return self.__feromoanas

class Ciudad(object):
	"""docstring for Ciudad"""
	def __init__(self, coordenadas, nombre ):
		super(Ciudad, self).__init__()
		self.__coordenadas = coordenadas
		self.__nombre = nombre

	def __str__(self): return self.__nombre + " : " + str( self.__feromonas )

	def getNombre(self):	return self.__nombre
	def getCoordenada(self): return self.__coordenadas


class Hormiga():
	def __init__(self, ciudadInicio):
		self.__ciudadInicio = ciudadInicio
		self.reset()

	def reset():
		self.__ciudadesVisitadas = [ ciudadInicio ]

		self.__ciudadesPorVisitar = range( NUMERO_CIUDADES )
		self.__ciudadesPorVisitar = self.__ciudadesPorVisitar.remove( ciudadInicio )


CIUDADES = {	
				0 :	Ciudad( (38.24, 20.42) , "Ciudad01" ),
				1 : Ciudad( (39.57, 26.15) , "Ciudad02" ),
				2 : Ciudad(	(40.56, 25.32) , "Ciudad03" ),
				3 : Ciudad( (36.26, 03.12) , "Ciudad04" ),

				4 : Ciudad( (33.48, 10.54) , "Ciudad05" ),
				5 : Ciudad(	(37.56, 12.19) , "Ciudad06" ),
				6 : Ciudad( (38.42, 13.11) , "Ciudad07" ),
				7 : Ciudad( (37.52, 20.44) , "Ciudad08" ),

				8 : Ciudad( (41.23, 09.10) , "Ciudad09" ),
				9 : Ciudad( (41.17, 09.10) , "Ciudad10" ),
				10: Ciudad( (36.08, -5.21) , "Ciudad11" ),
				11: Ciudad( (38.47, 15.13) , "Ciudad12" ),

				12: Ciudad( (38.15, 15.35) , "Ciudad13" ),
				13: Ciudad( (37.51, 15.17) , "Ciudad14" ),
				14: Ciudad( (35.49, 14.32) , "Ciudad15" ),
				15: Ciudad( (39.36, 19.56) , "Ciudad16" )
			}

def distancia(ciudadX, ciudadY):
	return math.sqrt(	( ciudadX.getCoordenada()[ 0 ] - ciudadY.getCoordenada()[ 0 ] ) ** 2 + \
						( ciudadX.getCoordenada()[ 1 ] - ciudadY.getCoordenada()[ 1 ] )	** 2 )

CAMINOS = [ ([  ] * NUMERO_CIUDADES) for x in range(NUMERO_CIUDADES) ]

for indiceX, ciudadX in enumerate( CIUDADES ):
	for indiceY, ciudadY in enumerate( CIUDADES ):
		CAMINOS[ indiceX ].append( Camino( distancia( CIUDADES[ ciudadX ], CIUDADES[ ciudadY ] ) ) )