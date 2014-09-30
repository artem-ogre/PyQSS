import sys
from helpers import *

def parse(string):
	"Parse QSS for python insertions, evaluate python code for every snipplet and insert it back"
	import re
	res_str = string
	toExec = re.findall( "\@(.+?)\@", string, re.DOTALL )
	print (toExec)
	for i in range( len( toExec ) ):
		res_str = res_str.replace( "@" + toExec[i] + "@", "" )
		exec( toExec[i], globals() )
	toEval = re.findall("\$(.+?)\$", string, re.DOTALL)
	evalRes = [str( eval( e ) ) for e in toEval]
	toEval = ["$" + e + "$" for e in toEval]
	for i in range( len(toEval) ):
		res_str = res_str.replace( toEval[i], evalRes[i] )
	return res_str


if __name__ == "__main__":
	if len(sys.argv) != 3:
		print ("Invalid argument list. Use syntax: PyQSS input_filename (pyqss) output_filename (qss).")
		print ('Number of arguments:', len(sys.argv), 'arguments.')
		print ('Argument List:', str(sys.argv))
		quit()
	#Enhanced QSS goes here. Use: $your_code$ to embed Python code.
	pyqss_str = open( sys.argv[1], "r" ).read() #QSS enhanced with Python insertions
	output_file = open( sys.argv[2], "w" )
	result = parse( pyqss_str )
	print ("Resulting qss file is sucessfully generated from qss+python.")
	output_file.write( result )
	output_file.close()