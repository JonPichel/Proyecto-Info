import aircraft, flight, assignment

ac1 = aircraft.Aircraft()

ac1.callsign = 'AC320'
ac1.type = 'A320'
ac1.seats = 80

ac2 = aircraft.Aircraft()

ac2.callsign = 'PAPA'
ac2.type = 'A320'
ac2.seats = 94234

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

f3 = flight.Flight()

f3.dep = "Palma"
f3.arr = "Paris"
f3.time_dep = 14 * 60
f3.time_arr = 15 * 60
f3.passengers = 67

ass1 = assignment.Assignment()

ass1.aircraft = ac1
ass1.flights = [f1, f2]

ass2= assignment.Assignment()

ass2.aircraft = ac2
ass2.flights = [f1, f3]

assignment.plot_assignment(ass1)

assignment.plot_assignments([ass1, ass2])
