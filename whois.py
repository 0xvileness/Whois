import socket
from ipwhois import IPWhois
from pprint import ppring 

print()
print("  ╦ ╦┬ ┬┌─┐┬┌─┐ ")
print("  ║║║├─┤│ ││└─┐ ")
print("  ╚╩╝┴ ┴└─┘┴└─┘ ")
print(" Made By @Oxycrime ")
print()

target = input("Enter Website")

#get ip of the server
ip = socket.gethostbyname(target)
obj = IPWhois(ip)
obj = obj.lookup_whois()

#out put 
pprint(obj)
