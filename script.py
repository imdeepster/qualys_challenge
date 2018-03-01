import numpy as np
from elasticsearch import Elasticsearch,helpers

#read from the given data.dat file - 2 part numbers, first part being real and second part being imaginary. Each part is a unsigned integer
def read_from_file(filename):
	dt = np.dtype([('real',np.uint8),('imag',np.uint8)])
	return np.fromfile(filename,dtype = dt)

#compute average of the real numbers array and imaginary numbers array
def compute_averages(real_numbers,imag_numbers):
	average_realNumbers = real_numbers.mean()
	average_imagNumbers = imag_numbers.mean()
	print("Real Numbers average = " + str(average_realNumbers) + " Imaginary Numbers average =" + str(average_imagNumbers))

#constructing array of complex numbers from corresponding values in real numbers and imaginary numbers array
def join_complex_numbers(real_numbers,imag_numbers):
	comp_numbers =  np.column_stack((real_numbers,imag_numbers))
	return comp_numbers

#inserting each complex number into the elastic search index by converting the 2D matrix into a json format
def insert_into_ES(complex_numbers):
	es = Elasticsearch(['https://username:password@elastic_search_database_ip:port'])
	doc = [{'real':int(i[0]), 'imag':int(i[1])} for i in complex_numbers.tolist()]
	print(es.count(index = "complex-numbers"))
	for d in doc:
		res = es.index(index = "complex-numbers", doc_type = 'complexnumbers', body = d)
	print(es.count(index = "complex-numbers"))

def main():
	filename = 'data.dat'
	values = read_from_file(filename)
	real_numbers = values['real']
	imag_numbers = values['imag']
	compute_averages(real_numbers,imag_numbers)
	complex_numbers = join_complex_numbers(real_numbers,imag_numbers)
	insert_into_ES(complex_numbers)

if __name__ == "__main__":
	main()