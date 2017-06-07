#!/usr/bin/python
from Tkinter import *
from math import sin, cos, sqrt, atan2, radians

import tkMessageBox
import csv

citiesDict = {}

# approximate radius of earth in km
earthR = 6373.0

# conversion factor
conv_fac = 0.621371

def calcDist(entry1,entry2):
	if entry1 and entry2 in citiesDict:
		
		temp1 = citiesDict.get(entry1)
		lat1 = radians(float(temp1['lat']))
		lng1 = radians(float(temp1['lng']))
		
		temp2 = citiesDict.get(entry2)
		lat2 = radians(float(temp2['lat']))
		lng2 = radians(float(temp2['lng']))

		dlon = lng2 - lng1
		dlat = lat2 - lat1

		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))

		km = earthR * c
		miles = km * conv_fac
		kmResult = str(round(km, 2))
		mlResult = str(round(miles, 2))
		
		tkMessageBox.showinfo( "Result", 
			"Starting City: " + entry1 + "\n" + 
			"Destination City: " + entry2 + "\n" + 
			"Kilometers: "+ kmResult + " \n Miles: " + mlResult)

	else:
		tkMessageBox.showinfo( "Can't Find City", "One or Both of the cities cannot be found")	

def checkInput(entry1, entry2):
	if entry1.strip() and entry2.strip():
		calcDist(entry1,entry2)
	else:
		tkMessageBox.showinfo( "INVALID INPUT", "Make sure you add a valid city names")
		

def main():
	#Starts GUI and adds all components
	root = Tk()
	root.title("How Far")
	root.resizable(0,0)

	label1 = Label(root, text="Choose First city")
	label1.pack()

	e1 = Entry(root)
	e1.pack()

	label2 = Label(root, text="Choose Second city")
	label2.pack()

	e2 = Entry(root)
	e2.pack()

	b1 = Button(root, text="Calculate Distance", command = lambda : checkInput(e1.get(), e2.get()))
	b1.pack()

	root.mainloop()

if __name__ == '__main__':
	#imports csv and adds cities to dictionaire
	citiesList = [row for row in csv.DictReader(open('cities.csv'))]
	for city in citiesList[0:]:
		citiesDict[city['city']] = city
	main()
