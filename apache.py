import correo
from subprocess import Popen, PIPE, STDOUT

#	Comando a ejecutar
cmd = 'service apache2 status'
p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)

#	Guardamos el resultado en una variable
output = p.stdout.read()

#	Convertimos en Mayuscula y buscamos la palabra NOT
resultado = output.upper().count('NOT')

#	Apache2 is NOT running
if resultado == 0:
	print "OK"
else:
	correo.mail("vomar24@gmail.com", "Error Apache", "Existe un error en Apache")
