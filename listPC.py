#!/usr/bin/env python3

# Пингуем включенные ПК с именем chelN, где N это цифры от 01 до 1000, резулятат выводим в файл.

import subprocess

m = open('/etc/ansible/listPC.txt','w')

for ping in range(1, 100):
    ip = "chel0" + str(ping)
    result = subprocess.call(["ping", "-c", "1", ip])
    if result == 0:
        m.write("\n" + ip)
    else:
	pass

for ping in range(100, 1000):
    ip = "chel" + str(ping)
    result = subprocess.call(["ping", "-c", "1", ip])
    if result == 0:
        m.write("\n" + ip)
    else:
	pass

m.close()
