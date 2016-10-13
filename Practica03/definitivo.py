import random, math

random.seed(201610123)

TAMANO_POBLACION = 20
NUM_ALELOS = 20

MAX_GENERACIONES = 10000
MIN_ALELO = -5
MAX_ALELO = 5
PORCENTAJE_MUTACION = 1

MAX_INT = 88888888
MIN_INT = -88888888

class Individuo(object):
	"""docstring for Individuo"""
	def __init__(self, genotipo):
		super(Individuo, self).__init__()
		self.__genotipo = genotipo
		self.__fitness = -1
		self.__fx = MAX_INT

	def getGenotipo(self): return self.__genotipo
	def getFitness(self): return self.__fitness
	def setFitness(self, fitness): self.__fitness = fitness
	def setFx(self, fx): self.__fx = fx
	def getFx(self): return self.__fx

	def setMutacion(self, index, val ) : self.__genotipo[index] = val

	def funcionFitness( self ):
		auxFitness = 0

		for alelo in self.getGenotipo():
			auxFitness += alelo ** 2

		self.setFx( auxFitness )

		try:
			self.setFitness( 1 / auxFitness )
		except ZeroDivisionError:
			self.setFitness( MAX_INT )
		except:
			raise


class Poblacion(object):
	"""docstring for Poblacion"""
	def __init__(self, numAlelos, minAlelo, maxAlelo, maxGeneraciones, tamanoPoblacion, porcentajeMutacion):
		super(Poblacion, self).__init__()
		self.poblacion = []
		self.hijos = []
		self.minAlelo = minAlelo
		self.maxAlelo = maxAlelo
		self.maxGeneraciones = maxGeneraciones
		self.tamanoPoblacion = tamanoPoblacion
		self.numAlelos = numAlelos
		self.totalFitness = 0
		self.porcentajeMutacion = float(porcentajeMutacion) / 100

	#def generaAlelo(self):	return 	( random.random() * random.randint( self.minAlelo, self.maxAlelo ) )
	def generaAlelo(self): return random.uniform( -5. , 5. )
	def resetTotalFItness(self): self.totalFitness = 0
	def setPoblacion(self, hijos) : self.poblacion = hijos

	def inicializaPoblacion(self):
		for i in range(self.tamanoPoblacion):
			auxGenoma = []
			for j in range(self.numAlelos):
				auxGenoma.append( self.generaAlelo() )

			self.poblacion.append( Individuo( auxGenoma ) )

	def calculaFitness(self):
		for individuo in self.poblacion:
			individuo.funcionFitness()
			self.totalFitness += individuo.getFitness()

	def aparear(self, padre, madre):
		numAlelos = random.randint( 1, len( padre.getGenotipo() ) - 1 )

		genoma1 = padre.getGenotipo()[ : numAlelos ] + madre.getGenotipo()[ numAlelos : ]
		genoma2 = madre.getGenotipo()[ : numAlelos ] + padre.getGenotipo()[ numAlelos : ]

		return 	Individuo( genoma1 ) , Individuo( genoma2 )

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

	def ruleta( self ):
		totalProbabilidad = 0

		elegido = random.random()

		for individuo in self.poblacion:
			aux =  (individuo.getFitness() / self.totalFitness) 
			totalProbabilidad += aux

			if elegido <= totalProbabilidad:
				#print( "Debug: " , totalProbabilidad )
				return individuo

		print(len(self.poblacion))
		return self.poblacion[-1]
		#print( elegido, totalProbabilidad )
		raise

	def imprimirPoblacion( self ):
		for individuo in self.poblacion:
			auxImpresion = []
			for j in individuo.getGenotipo():
				print "{}\t".format( round( j, 2 )  ) ,
			print "f(x) = " + str( round(individuo.getFx() , 4) ) , 
			print "fitness(x) = " + str( round(individuo.getFitness(), 4 ) )

		print()
		pass

	def sortPoblacion(self, criterio = None):
		self.setPoblacion( sorted( self.poblacion,key = lambda x: x.getFitness() ) )

	def mutarPoblacion(self):
		numeroMutantes = int(math.ceil(self.tamanoPoblacion * self.numAlelos * self.porcentajeMutacion))

		for i in range( numeroMutantes ):
			aux = self.poblacion[ random.randint( 0, self.tamanoPoblacion - 1 ) ]
			aux.setMutacion( random.randint( 0, self.numAlelos - 1 ) , self.generaAlelo() )

	def cicloPrincipal(self):
		numGeneraciones = 0

		p.inicializaPoblacion()
		p.calculaFitness()
		p.sortPoblacion()
		print("Generacion " + str(numGeneraciones) )
		p.imprimirPoblacion()

		while (numGeneraciones <= self.maxGeneraciones):
			#print(len(self.poblacion))
			self.hijos = []
			self.resetTotalFItness()
			self.sortPoblacion()
			self.calculaFitness()

			while len(self.hijos) < self.tamanoPoblacion:
				self.seleccionMejores()
				self.mutarPoblacion()

			self.setPoblacion( self.hijos )

			numGeneraciones += 1

			if (numGeneraciones % 50) == 0:
				print("Generacion " + str(numGeneraciones) )
				p.calculaFitness()
				p.sortPoblacion()
				p.imprimirPoblacion()

		print("Generacion " + str(numGeneraciones) )
		p.calculaFitness()
		p.sortPoblacion()
		p.imprimirPoblacion()
			
		print(p.poblacion[-1].getGenotipo())

if __name__ == '__main__':
	p = Poblacion( NUM_ALELOS, MIN_ALELO, MAX_ALELO, MAX_GENERACIONES, TAMANO_POBLACION, PORCENTAJE_MUTACION)
	p.cicloPrincipal()