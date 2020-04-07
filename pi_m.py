#!/usr/bin/env Python3
import random
print("ingrese la cantidad de valores:")
cdv = input()
def valor_pi(n):
	c = 0
	for x in range(n): 	
		x = random.uniform(0,1)
		y = random.uniform(0,1)
		if x**2+y**2 < 1 :
			c = c + 1
	v_pi = 4*(c/n)
	return v_pi	
print("El valor de pi para esta cantidad de puntos es:")
print(valor_pi(int(cdv)))


