import random as rnd

MAXINT = 999999999999

class Particula():
	def __init__(self, numDimensiones, tamVecindario, rangoMin, rangoMax, velocidadMax, funcionFitness):
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
		self.numDimensiones = numDimensiones

		self.inicializar()

	def __str__(self): return 	"Pos: " + str( [ round( x, 2) for x in self.__posicion ] ) + \
								"\nVel: " + str( [ round( x , 2) for x in self.__velocidad ] ) +\
								"\nFit: " + str(  self.__fitness ) +\
								" MF:  " + str(  self.__mejorFitness ) +\
								" Val: " + str( self.__valor )

	def inicializar(self):
		for i in range(self.numDimensiones):
			self.__posicion.append( self.getRandom( self.rangoMin, self.rangoMax ) )
			self.__velocidad.append( self.getRandom( -self.__velocidadMax, self.__velocidadMax ) )

		self.calculaFitness()
		self.__mejorFitness = self.__fitness
		self.__mejorPosicion = self.__posicion


	def getRandom(self, rMin, rMax): return rnd.uniform( rMin, rMax)
	def calculaFitness(self) : self.__fitness, self.__valor =  self.__funcionFitness( self.__posicion )

	def getVecindario(self) : return self.__vecindario
	def setVecindario(self, vecindario) : self.__vecindario = vecindario
	def getPosicion(self) : return self.__posicion
	def getVelocidad(self) : return self.__velocidad
	def getFitness(self) : return self.__fitness
	def getMejorFitness(self) : return self.__mejorFitness
	def getMejorPosicion(self) : return self.__mejorPosicion
	def getValor(self): return self.__valor