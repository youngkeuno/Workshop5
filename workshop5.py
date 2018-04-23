from graphics import*
from time import*
from random import*

def process_line (the_line):
	data_list = the_line.split(",")
	answer = int ( data_list[2])
	return answer

def process_file (filename):
	the_file = open(filename,"r")
	for line in the_file:
		area = process_line (line)
		print(area)


def total_area():
	total_area=0
	for x in open("states.csv", "r"):
		area=process_line (x)
		total_area=total_area+area
	print("total area is:")
	print(total_area)	

total_area()

def process_line2 (the_line):
	data_list = the_line.split(",")
	answer = int ( data_list[3])
	return answer

def total_pop():
	total_pop=0
	for x in open("states.csv", "r"):
		pop=process_line2 (x)
		total_pop=total_pop+pop
	print("total population is:")
	print(total_pop)

total_pop()	

def pop_density():
	for x in open("states.csv", "r"):
		area= process_line(x)
		pop= process_line2(x)
		print(pop/area)

pop_density()

def avg_pop_density():
	total_area=0
	for x in open("states.csv", "r"):
		area=process_line (x)
		total_area=total_area+area
	total_pop=0
	for x in open("states.csv", "r"):
		pop=process_line2 (x)
		total_pop=total_pop+pop
	print("national average is:")	
	print(total_pop/total_area)

avg_pop_density()

def process_line3 (the_line):
	data_list = the_line.split(",")
	answer = data_list[0]
	return answer

def compare_to_national_avg():
	print("these states have population densities below the national average:")
	total_area=0
	for x in open("states.csv", "r"):
		area=process_line (x)
		total_area=total_area+area
	total_pop=0
	for x in open("states.csv", "r"):
		pop=process_line2 (x)
		total_pop=total_pop+pop
	z=total_pop/total_area
	for x in open("states.csv", "r"):
		pop= process_line2(x)
		area= process_line(x)
		name= process_line3(x)
		y=pop/area
		if y<z:
			print(name) 

compare_to_national_avg()

input("press a key to continue")
