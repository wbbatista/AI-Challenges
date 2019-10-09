"""
Arutora: Wana Batista, criado em 08/10/2019
 
"""


import numpy as np 
import random as rd
import string



def randomString(s_length):
    """Generate a random string of fixed length """
    #letters = string.ascii_lowercase
    string_seq = "abcdef"

    st = ''.join(rd.choice(string_seq) for i in range(s_length))
    return st


def write_file(filename, my_list):

	with open(str(filename) + '.txt', 'w') as f:
	    for st in my_list:
	        f.write("%s\n" %st)
	return print('done write')


if __name__ =="__main__":
	number_of_lines = 5
	my_list = [number_of_lines]
	i=0
	while i < number_of_lines:
		n = rd.randrange(3, 10, 1)
		s = randomString(n)
		my_list.append(s)

		i += 1
	write_file("list_of_string",my_list)
