#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	maxi=list()
	for liste in numbers:
		a=max(liste)
		maxi.append(a)

	return maxi

def join_integers(numbers):
	c=str()
	for num in numbers:
		a=str(num)
		c+=a



	return int(c)

def generate_prime_numbers(limit):
	premier=list()
	entier=[n for n in range(2, limit+1)]

	for num in entier:
		for num2 in entier:
			if num2%num == 0 and num2 !=num:
				entier.remove(num2)

	return entier

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	liste=list()
	if excluded_multiples==None:
		excluded_multiples=1

	for element in strings:
		for num in range(1, num_combinations, excluded_multiples):
			liste.append(element+str(num))


	return liste

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
