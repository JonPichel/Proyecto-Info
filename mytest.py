import airline, aircraft, flight

# Test aircraft
ac = aircraft.Aircraft()
ac.callsign = "AC320"
ac.type = "A320"
ac.seats = 80
aircraft.show_aircraft(ac)

# Test flight
fl = flight.Flight()
fl.dep = "Barcelona"
fl.arr = "Vigo"
fl.time_dep = 60 * 8
fl.time_arr = 60 * 9 + 10
fl.passengers = 81
flight.show_flight(fl)

print(flight.fits_flight_in_aircraft(fl, ac))

# Test airline
al = airline.Airline()
al.name = "Rabos Airlines"
al.aircrafts.append(ac)
al.operations.append(fl)

airline.show_airline(al)