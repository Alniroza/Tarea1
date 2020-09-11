from datetime import datetime

#Compara los strings y retorna (hora_operacion, string mas largo, lenstring1, lenstring2, string1, string2)
def compareString(string1 = '', string2 = ''):
	try:
		if not (isinstance(string1, str) and isinstance(string2, str)):
			raise TypeError('no se ha entregado un string')

		data = [datetime.now(), '' ,str(len(string1)), str(len(string2)), string1, string2]
		if len(string1) > len(string2):
			print("El string1 es mas largo con " + str(len(string1)) + " caracteres.")
			data[1] = "string1 > string2"

		elif len(string1) == len(string2):
			print("El string1 y el string2 son igual de largos " + str(len(string1)) + " caracteres.")
			data[1] = "string1 = string2"
		else:
			print("El string2 es mas largo con " + str(len(string2)) + " caracteres.")
			data[1] = "string1 < string2"

		logMaker(data)
		return data

	except TypeError as err:
		log = "ERROR, " + str(err)
		logMaker(log, 1)

	except KeyboardInterrupt as err:
		log = "ERROR, "+ str(err)
		logMaker(log, 1)

	except MemoryError as err:
		log = "ERROR, " + str(err)
		logMaker(log, 1)

def logMaker(data, err = 0):
	try:
		file = open('logs.txt', 'a')
	except OSError() as err:
		log = "WARNING, " + str(err)
		print(log)
	else:
		log = ""
		if err == 0:
			log += data[0] + ', ' + data[1] + ', ' + data[2] + ', ' + data[3] + ', ' + data[4] + ', ' + data[5] + '\n'
		else:
			print(data)
			file.write(str(datetime.now())+ ', ' + data + "\n")
		return file.close()
