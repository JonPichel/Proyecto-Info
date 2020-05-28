#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:25:43 2020

@author: cristina
"""

#test code of Phase3
import airline, airport

#uploading the data from files
primera = airline.read_airline("PrimeraAir.txt")
costs = airport.read_airports("AP.txt")
# faltaba leer los costes
airport.read_airport_costs(costs, "APC.txt")

#do calculations
primera = airline.assign_operations(primera)
to_pay = airline.calculate_day_costs(primera, costs)

#results in screen and in file
print("Total cost for the day operations is "+str(to_pay)+" Euros\n")
if airline.write_day_plan(primera, "May7.txt"):
    print("See detailed planning in file 'May7th.txt'")