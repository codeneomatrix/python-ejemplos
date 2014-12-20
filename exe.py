

def f(lista):
	for i in lista:
		print ("recibo")
		print(i)
		yield 2


if __name__ == "__main__":

	for i in f(['a','b','c']):
		print ("Me ha devuelto")
		print (i)