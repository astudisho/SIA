import random as rnd

MAXINT = 999999999999

class Particula():
	def __init__(self, numDimensiones, tamVecindario, rangoMin,\
				 rangoMax, velocidadMin, velocidadMax, funcionFitness, maxPhi ):
		self.__vecindario = []
		self.__posicion = []
		self.__velocidad = []
		self.__fitness = None

		self.__mejorFitness = None
		self.__mejorPosicion = []
		self.__mejorVecino = None
		self.__velocidadMax = velocidadMax
		self.__phi1 = []
		self.__phi2 = []
		self.__minPhi = 0
		self.__maxPhi = maxPhi

		self.__funcionFitness = funcionFitness
		self.__rangoMin = rangoMin
		self.__rangoMax = rangoMax
		self.__numDimensiones = numDimensiones

		self.__inicializar()

	def __str__(self): return 	"Pos: " + str( [ round( x, 2) for x in self.__posicion ] ) + \
								"\nVel: " + str( [ round( x , 2) for x in self.__velocidad ] ) +\
								"\nFit: " + str(  self.__fitness ) +\
								" MF:  " + str(  self.__mejorFitness ) + "\n\n"

	def __inicializar(self):
		for i in range(self.__numDimensiones):
			self.__posicion.append( self.getRandom( self.__rangoMin, self.__rangoMax ) )
			self.__velocidad.append( self.getRandom( -self.__velocidadMax, self.__velocidadMax ) )

		self.calculaFitness()
		self.__mejorFitness = self.__fitness
		self.__mejorPosicion = self.__posicion
		self.__inicializaPhi()

	def __inicializaPhi(self):
		self.__phi1 = []
		self.__phi2 = []

		for x in range( self.__numDimensiones ):
			self.__phi1.append( self.getRandom( self.__minPhi , self.__maxPhi ) )
			self.__phi2.append( self.getRandom( self.__minPhi , self.__maxPhi ) )

	def calculaMejorVecino(self):
		mejorVal = MAXINT
		mejorVecino = None

		for vecino in self.__vecindario:
			if vecino.getFitness() < mejorVal:
				mejorVecino = vecino
				mejorVal = mejorVecino.getFitness()

		self.__mejorVecino = mejorVecino

	def calculaVelocidad(self):
		self.__inicializaPhi()
		velocidadAuxiliar = []

		for i in range( self.__numDimensiones ):
			#print( self.__mejorVecino.getPosicion()[ i ] )

			BiXi = self.__mejorPosicion[ i ] - self.__posicion[ i ]			
			HiXi = self.__mejorVecino.getPosicion()[ i ] - self.__posicion[ i ]

			aux = self.__phi1[ i ] * BiXi
			aux1 = self.__phi2[ i ] * HiXi

			resultado = self.__velocidad[ i ] + aux + aux1

			if abs(resultado) > self.__velocidadMax:
				resultado = resultado * self.__velocidadMax / abs( resultado )

			velocidadAuxiliar.append( resultado )

		self.__velocidad = velocidadAuxiliar

	def calculaPosicion(self):
		posicionAuxiliar = []

		for i in range(self.__numDimensiones):
			resultado = self.__posicion[ i ] + self.__velocidad[ i ]

			if resultado < self.__rangoMin:
				resultado = self.__rangoMin

			elif resultado > self.__rangoMax:
				resultado = self.__rangoMax

			posicionAuxiliar.append(resultado)

		self.calculaFitness()

		if self.getFitness() < self.__mejorFitness:
			#print("Encontro mejor fitness")
			self.__mejorPosicion = self.getPosicion()
			self.__mejorFitness = self.getFitness()

		self.__posicion = posicionAuxiliar

	def getRandom(self, rMin, rMax): return rnd.uniform( rMin, rMax)
	def calculaFitness(self) : self.__fitness =  self.__funcionFitness( self.__posicion )

	def getVecindario(self) : return self.__vecindario
	def setVecindario(self, vecindario) : self.__vecindario = vecindario
	def getPosicion(self) : return self.__posicion
	def getVelocidad(self) : return self.__velocidad
	def getFitness(self) : return self.__fitness
	def getMejorFitness(self) : return self.__mejorFitness
	def getMejorPosicion(self) : return self.__mejorPosicion
	def getValor(self): return self.__valor