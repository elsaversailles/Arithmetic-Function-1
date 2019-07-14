#Written by Elsa Versailles
#CC BY 3.0
import math

print ("Arithmetic Sequence Calculator")
print ("")
n1 = int(input('First term: '))
print ("")
n2 = int(input('Number of Terms: '))
print ("")
n3 = int(input('Common difference: '))
print ("")
n4 = int(input('Sequence 1:'))
print ("")
n5 = int(input('Sequence 2 :'))
print ("")
n6 = int(input('Sequence 3 :'))

a = (n2 - 1)
b = (a * n3)
c = (n1 + b)
print ("")
print ("Answer's Sign:")
if (n4 > n6):
 print ("")
 print ("(-)")
 print ("NEGATIVE")
if (n4 < n6):
	print("")
	print("(+)")
	print ("POSITIVE")
print("")
print (c)
