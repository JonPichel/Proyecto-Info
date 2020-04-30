#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Program to test project phase 1
import aircraft
import flight
import airline

def createXicaAirline ():
    """ Function createXicaAirline
    ==============================
    This function has no input parameters
    Returns an airline with 2 aircraft and 4 flights
    """ 
    # creates first aircraft with some values
    AC1 = aircraft.Aircraft()
    AC1.callsign = "EC234"
    AC1.type = "A320"
    AC1.seats = 280
    # creates a second aircraft with other values
    AC2 = aircraft.Aircraft()
    AC2.callsign = "EC504"
    AC2.type = "A321"
    AC2.seats = 310

    # creates first flight with some values
    FL1 = flight.Flight()
    FL1.dep = "Barcelona"
    FL1.arr = "Budapest"
    FL1.time_dep = 8*60
    FL1.time_arr = 11*60
    FL1.passengers = 54
    # creates second flight with some values
    FL2 = flight.Flight()
    FL2.dep = "Barcelona"
    FL2.arr = "Istambul"
    FL2.time_dep = 9*60
    FL2.time_arr = 12.5*60
    FL2.passengers = 154
    # creates third flight with some values
    FL3 = flight.Flight()
    FL3.dep = "Istambul"
    FL3.arr = "Budapest"
    FL3.time_dep = 17*60
    FL3.time_arr = 19.25*60
    FL3.passengers = 140
    # creates fourth flight with some values
    FL4 = flight.Flight()
    FL4.dep = "Budapest"
    FL4.arr = "Barcelona"
    FL4.time_dep = 20*60
    FL4.time_arr = 23*60
    FL4.passengers = 97

    # creates the airline
    Xica = airline.Airline()
    Xica.name = "Xica Airline"
    airline.add_aircraft(Xica, AC1)
    airline.add_aircraft(Xica, AC2)
    airline.add_operation(Xica, FL1)
    airline.add_operation(Xica, FL2)
    airline.add_operation(Xica, FL3)
    airline.add_operation(Xica, FL4)
    return Xica

# main
print ("Phase1 test program")
A = createXicaAirline()
airline.show_airline(A)
print ("Phase1 test program end")

