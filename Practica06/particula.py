import random as rnd

MAXINT = 999999999999

class Particula():
	def __init__(self, dimensiones, tamVecindario, rangoMin, rangoMax, velocidadMax, funcionFitness):
		self.__vecindario = []
		self.__posicion = []
		self.__velocidad = []
		self.__fitness = -1
		self.__mejorFitness = -1
		self.__mejorPosicion = []
		self.__velocidadMax = velocidadMax
		self.__valor = None

		self.__funcionFitness = funcionFitness
		self.rangoMin = rangoMin
		self.rangoMax = rangoMax
		self.dimensiones = dimensiones

		self.inicializar()

	def __str__(self): return 	"Pos: " + str( [ round( x, 2) for x in self.__posicion ] ) + \
								"\nVel: " + str( [ round( x , 2) for x in self.__velocidad ] ) +\
								"\nFit: " + str(  self.__fitness ) +\
								" MF:  " + str(  self.__mejorFitness ) +\
								" Val: " + str( self.__valor )

	def inicializar(self):
		for i in range(self.dimensiones):
			self.__posicion.append( self.getRandom( self.rangoMin, self.rangoMax ) )
			self.__velocidad.append( self.getRandom( -self.__velocidadMax, self.__velocidadMax ) )

		self.calculaFitness()
		self.__mejorFitness = self.__fitness
		self.__mejorPosicion = self.__posicion


	def getRandom(self, rMin, rMax): return rnd.uniform( rMin, rMax)
	def calculaFitness(self) : 
		self.__fitness, self.__valor =  self.__funcionFitness( self.__posicion ) 

def fitness( posicion ):
	suma = 0
	for i in posicion:
		suma += pow( i , 2 )

	print(suma)

	if suma == 0:
		return MAXINT, suma
	else:
		return 1 / suma, suma

if __name__ == '__main__':
	a = Particula( 20, 2, -5, 5, 2. , fitness )

	print(a)