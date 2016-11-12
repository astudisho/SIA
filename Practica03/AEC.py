#Algoritmo genetico evolutivo continuo
import random, sys

random.seed(201610123)

NUM_DECIMALES = 28
MAX_FITNESS = sys.maxint
MAX_GENERACIONES = 1000
MAX_POBLACION = 20
NUM_ALELOS = 20
ALELO_MIN = -5
ALELO_MAX = 5
MUTACION = 0.02


def funcionFitness( genoma ):
	auxFitness = 0

	for alelo in genoma:
		auxFitness += alelo ** 2

	print( "Aux fitness: ", auxFitness)

	if auxFitness == 0.:
		return MAX_FITNESS
	else:
		return 1 / auxFitness

class Individuo(object):
	"""docstring for Individuo"""
	def __init__(self, genoma):
		super(Individuo, self).__init__()
		self.genoma = genoma
		self.fitness = None
		#self.fx = fx

	def setFitness(self, fitness): self.fitness = fitness
	#def setFx(self, fx): self.fx = fx

class Poblacion(object):
	"""docstring for Poblacion"""
	def __init__(self, funcionFitness, numAlelos , aleloMin  , aleloMax , mutacion):
		super(Poblacion, self).__init__()
		
		self.poblacion = []
		self.hijos = []
		self.funcionFitness = funcionFitness
		self.totalFitness = 0
		self.aleloMin = aleloMin
		self.aleloMax = aleloMax
		self.numAlelos = numAlelos
		self.mutacion = mutacion

	def resetTotalFitness( self ): self.totalFitness = 0
	def setPoblacion( self, poblacion ): self.poblacion = poblacion

	def seleccionMejores( self ):
		aux1 = self.ruleta()

		flag = True

		while( flag ):
			aux2 = self.ruleta()

			if aux1 != aux2:
				flag = False

		hijos = self.aparear( aux1, aux2 )

		self.hijos.append( hijos[0] )
		self.hijos.append( hijos[1] )

	def aparear( self, padre, madre ):
		numAlelos = random.randint( 1, len( padre.genoma ) - 1 )

		genoma1 = padre.genoma[ : numAlelos ] + madre.genoma[ numAlelos : ]
		genoma2 = madre.genoma[ : numAlelos ] + padre.genoma[ numAlelos : ]


		return 	Individuo( genoma1 ) , Individuo( genoma2 )

	def calcularFitness( self ):
		for individuo in self.poblacion:
			#fitness = round( self.funcionFitness( individuo.fenotipo ) , NUM_DECIMALES )
			fitness = self.funcionFitness(individuo.genoma)
			#print(fitness)
			individuo.setFitness( fitness )
			self.totalFitness += fitness
			print(self.totalFitness)

	def ruleta( self ):
		totalProbabilidad = 0

		elegido = round( random.random() , NUM_DECIMALES )

		for individuo in self.poblacion:
			aux =  (individuo.fitness / self.totalFitness) 
			totalProbabilidad += aux

			if elegido <= totalProbabilidad:
				#print( "Debug: " , totalProbabilidad )
				return individuo

		return self.poblacion[-1]
		#print( elegido, totalProbabilidad )
		raise

	def sortPoblacion(self, criterio = None):
		self.poblacion = sorted( self.poblacion,key = lambda x: x.fitness )

	def generaAlelo( self ):
		alelo = random.random() * random.randint( self.aleloMin, self.aleloMax )
		print(alelo)
		return alelo

	def inicializaPoblacion( self ):
		for i in range( 0 , MAX_POBLACION ):
			auxGenoma = []
			for j in range(NUM_ALELOS):
				alelo = self.generaAlelo()
				#auxGenoma.append( self.generaAlelo() )
				auxGenoma.append( alelo )

			self.poblacion.append( Individuo( auxGenoma ) )

	def imprimirPoblacion( self ):
		for individuo in self.poblacion:
			print( individuo.fitness )
		print()

	def mutar( self ):
		numeroMutantes = int( (MAX_POBLACION * NUM_ALELOS) * self.mutacion )

		for i in range( numeroMutantes ):
			individuo = self.poblacion[ random.randint( 0, MAX_POBLACION - 1 ) ]
			individuo.genoma[ random.randint( 0, NUM_ALELOS - 1 ) ] = self.generaAlelo

def cicloPrincipal( maxGeneraciones ):
	numGeneraciones = 0

	p = Poblacion( funcionFitness, NUM_ALELOS, ALELO_MIN, ALELO_MAX, MUTACION )
	p.inicializaPoblacion()
	p.calcularFitness()
	p.sortPoblacion()
	#p.imprimirPoblacion()
	while ( numGeneraciones <= MAX_GENERACIONES ):
		del( p.hijos[ : ] )

		while len( p.hijos ) != MAX_POBLACION :
			p.seleccionMejores()

		p.setPoblacion( p.hijos )
		p.calcularFitness()
		p.sortPoblacion()
		#p.mutar()

		numGeneraciones += 1

	print( p.poblacion[0].genoma ) 
	print( p.poblacion[0].fitness ) 

if __name__ == '__main__':
	cicloPrincipal( MAX_GENERACIONES )