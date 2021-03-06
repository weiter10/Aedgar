import csv
import os
import shutil
import sys
import time

if len(sys.argv) <= 2:

	f_origen = sys.argv[1]
	f_destino =str(time.strftime("%c")).replace(" ","-").replace("/","_").replace(":","-")
	
	directoryPath = f_origen+'/'+f_destino
	if not os.path.exists(directoryPath):
		os.mkdir(directoryPath)
	
	for fichero in os.listdir(f_origen):
			if not os.path.isdir(f_origen+'/'+fichero):
				shutil.move(f_origen+"/"+fichero,directoryPath)
else:
	print "Error en la llamada. Se necesitan carpetas origen y destino"
	print "ejemplo: python mover.py c_origen c_destino"