import random
import sys

random.seed(1)

NUM_ALELOS = 20
MAX_POBLACION = 20
MAX_GENERACIONES = 100
VAL_MIN = -5
VAL_MAX = 5
MUTACION = 0.02

NUM_DECIMALES = 4
AUMENTO = 1



def funcionFitness( x ):
	try:
		aux = 0
		for i in x:
			aux += i ** 2

		return ( 1 / aux )
	except ZeroDivisionError:
		return sys.maxint
	except Exception:
		raise

	

def funcionFx( x ):
	aux = 0

	for i in x:
		aux += i ** 2

	return aux



class Individuo(object):
	"""docstring for Individuo"""
	def __init__(self, genoma ):
		super(Individuo, self).__init__()
		
		self.genoma = genoma
		self.fitness = -1
		self.fx = None

	def setFitness(self, fitness):		self.fitness = fitness
	def setFx(self, fx): 	self.fx = fx

class Poblacion(object):
	"""docstring for Poblacion"""

	def __init__(self, funcionFitness ):
		super(Poblacion, self).__init__()

		self.poblacion = []
		self.poblacionNueva = []

		self.funcionFitness = funcionFitness
		self.totalFitness = 0

	def setPoblacion(self, poblacion ): self.poblacion = poblacion

	def generaAlelo(self):
		return ( random.random() * random.randint( VAL_MIN , VAL_MAX ) )

	def aparear(self, padre, madre):

		numAlelos = random.randint( 1, len( padre.genoma ) - 1 )

		genoma1 = padre.genoma[ : numAlelos ] + madre.genoma[ numAlelos : ]
		genoma2 = madre.genoma[ : numAlelos ] + padre.genoma[ numAlelos : ]


		return 	Individuo( genoma1 ) , Individuo( genoma2 )

	def seleccionMejores( self ):
		aux1 = self.ruleta()

		flag = True

		while( flag ):
			aux2 = self.ruleta()

			if aux1 != aux2:
				flag = False

		hijos = self.aparear( aux1, aux2 )

		self.poblacionNueva.append( hijos[0] )
		self.poblacionNueva.append( hijos[1] )

	def inicializaPoblacion(self):
		for i in range ( 0 ,  MAX_POBLACION):

			auxGenoma = []
			for i in range( NUM_ALELOS ):
				auxGenoma.append( self.generaAlelo() )

			print(auxGenoma)
			nuevoIndividuo = Individuo( auxGenoma )
			self.poblacion.append( nuevoIndividuo )

		self.poblacion = sorted( self.poblacion , key= lambda ind: ind.fitness )

	def resetTotalFitness( self ) : self.totalFitness = 0

	def calcularFitness( self ):
		for individuo in self.poblacion:
			fitness = self.funcionFitness( individuo.genoma )
			individuo.setFitness( fitness )
			self.totalFitness += fitness
			#print( individuo.genoma + ' : ' + str( self.funcionFitness( individuo.fenotipo ) ) )

	def ruleta( self ):
		totalProbabilidad = 0

		elegido = random.random()

		for individuo in self.poblacion:
			aux =  (individuo.fitness / self.totalFitness) 
			totalProbabilidad += aux

			if elegido <= totalProbabilidad:
				#print( "Debug: " , totalProbabilidad )
				return individuo

		return self.poblacion[-1]
		#print( elegido, totalProbabilidad )
		raise

	def imprimirPoblacion( self ):
		self.poblacion = sorted( self.poblacion , key= lambda ind: ind.fitness )

		print("Poblacion: ")
		for ind in self.poblacion:
			print( ind.fitness)

	def calcularFx( self ):
		for ind in self.poblacion:
			ind.setFx( funcionFx( ind.genoma ) )

	def sortPoblacion(self, criterio = None):
		self.poblacion = sorted( self.poblacion,key = lambda x: x.fitness )

	def mutar( self ):
		numeroMutantes = int( (len(self.poblacion) * len(self.poblacion[0].genoma) ) \
						 * MUTACION )


def cicloPrincipal( maxGeneraciones ):
	numGeneraciones = 0

	p = Poblacion(funcionFitness)
	p.inicializaPoblacion()
	p.calcularFitness()
	p.imprimirPoblacion()

	while( numGeneraciones != maxGeneraciones ):
		#p.poblacionNueva.clear()
		del( p.poblacionNueva[:] )
		p.resetTotalFitness()
		p.calcularFitness()

		while( len( p.poblacionNueva) != MAX_POBLACION ):
			p.seleccionMejores()

		#p.poblacion = p.poblacionNueva
		p.setPoblacion( p.poblacionNueva )
		p.mutar()
		p.calcularFitness()
		p.calcularFx()
		p.sortPoblacion()
		#p.imprimirPoblacion()

		numGeneraciones += 1

		if (numGeneraciones % 32) == 0:
			p.calcularFitness()
			p.imprimirPoblacion()

			raw_input()
if __name__ == '__main__':
	cicloPrincipal( MAX_GENERACIONES )