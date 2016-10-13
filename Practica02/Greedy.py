MIN = 0
MAX = 100 + 1

resultados = []
veces = 0

for i in range ( MIN , MAX):
	a = i
	for j in range ( MIN , MAX):
		b = j
		for k in range( MIN, MAX ):
			c = k
			for m in range ( MIN , MAX):
				d = m
				veces += 1
				if ( a + 2*b + 3*c + 4*d ) == 30:
					resultados.append( (a , b, c , d) )

print( "Veces: ", veces )
print( len(resultados) )

#for res in resultados:
#	print res