import os

#hostname = "code.google.com"
hostname = "almach.cuefa.inpg.fr"

response = os.system("ping -c 1 " + hostname)

if response == 0:
    print hostname, '[ OK ]'
else:
    print hostname, '[ BAD ]'
