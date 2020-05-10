#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:01:54 2020

@author: cristina
"""

import aircraft, flight, airline, assignment

from testAirline import createXicaAirline

X = airline.assign_operations(createXicaAirline())

airline.plot_assignments(X, title="Assignments for today")
for assig in X.assignments:
    flight.plot_flights(assig.flights, title=f"Flights for {assig.aircraft.callsign}")

airline.insert_delay(X, "Barcelona", 8*60, 60)
if airline.check_operations(X):
    print("No problem with the delay")
else:
    print("Reasigning flights again")
    X = airline.assign_operations(X)

airline.plot_assignments(X, title="Assignments after reassignment.")

# Now Budapest to Barcelona cannot be assigned since it overlaps with the new timing for the previous one
for assig in X.assignments:
    flight.plot_flights(assig.flights, title=f"Flights for {assig.aircraft.callsign}")

airline.show_airline(X)