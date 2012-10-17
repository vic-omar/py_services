import time

while True:
	#	Cada 20 Segundos se ejecutara el file
	time.sleep(20)
	import apache
	reload(apache)
	print "---"

# Developer Vic
