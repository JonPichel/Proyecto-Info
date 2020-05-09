#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Program to test project phase 1
import aircraft
import flight

# Create some flights
f1 = flight.Flight()
f2 = flight.Flight()
f3 = flight.Flight()
f4 = flight.Flight()

# Flight 1
f1.dep = "Singapore"
f1.arr = "Barcelona"
f1.time_dep = 6
f1.time_arr = 927
f1.passengers = 300

# Flight 2
f2.dep = "Barcelona" 
f2.arr = "Vigo"
f2.time_dep = 8 * 60
f2.time_arr = 9 * 60 + 20
f2.passengers = 90

# Flight 3
f3.dep = "Paris"
f3.arr = "Amsterdam"
f3.time_dep = 13 * 60 + 25
f3.time_arr = -25
f3.passengers = 230

# Flight 4
f4.dep = "Madrid" 
f4.arr = "Oporto"
f4.time_dep = 18 * 60 + 20
f4.time_arr = 19 * 60
f4.passengers = 180

# Create an aircraft
ac = aircraft.Aircraft()
ac.callsign = "AC320F"
ac.type = "A320"
ac.seats = 220

# Make a list of the flights
flights = [f1, f2, f4, f3]

# main
print("Phase1 test program")
# Show all the initial values
for f in flights:
    flight.show_flight(f)
    print("Flight duration:", flight.format_time(flight.flight_duration(f)))
    print("")
# Delay flights
if not flight.delay_flight(f1, 30):
    print("Couldn't delay the flight 1")
if not flight.delay_flight(f2, -30):
    print("Couldn't delay the flight 2")
if not flight.delay_flight(f3, 22400):
    print("Couldn't delay the flight 3")

for f in flights:
    if flight.fits_flight_in_aircraft(f, ac):
        print("Flight from", f.dep, "to", f.arr, "fits in aircraft.")
    else:
        print("Flight from", f.dep, "to", f.arr, "doesn't fit in aircraft.")

print("Phase1 test program end")

print("Phase2 test program")
# Test plot_flight
flight.plot_flight(f1)

# Test plot_flights
flight.plot_flights(flights)

for f in flights:
    print(f.time_dep)

for f in flight.sort_flights(flights):
    print(f.time_dep)