#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:01:54 2020

@author: cristina
"""

import aircraft, flights, airline, assignment
from testAirline import createXicaAirline

X = airline.assign_operations(createXicaAirline())
airline.plot_assignments(X)

airline.insert_delay(X, "Barcelona", 8*60, 60)
if airline.check_operations(X):
    print("No problem with the delay")
else:
    print("Reasigning flights again")
    X = airline.assign_operations(X)

airline.show_airline(X)