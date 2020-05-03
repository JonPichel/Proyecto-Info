import aircraft, flight, assignment

ac = aircraft.Aircraft()

ac.callsign = 'AC320'
ac.type = 'A320'
ac.seats = 80

f1 = flight.Flight()

f1.dep = "Barcelona"
f1.arr = "Vigo"
f1.time_dep = 8 * 60
f1.time_arr = 9 * 60 + 50
f1.passengers = 48

f2 = flight.Flight()

f2.dep = "Vigo"
f2.arr = "New York"
f2.time_dep = 15 * 60
f2.time_arr = 20 * 60
f2.passengers = 74

ass = assignment.Assignment()

ass.aircraft = ac
ass.flights = [f1, f2]

assignment.plot_assignment(ass)
