import aircraft, flight, assignment

from testFlight import createFlights

# Create some flights
flights = list(createFlights())

# Create a couple of assignments
ass1 = assignment.Assignment()
ass2 = assignment.Assignment()

# Create a couple of aircrafts
ac1 = aircraft.Aircraft()
ac1.callsign = "ACJ34"
ac1.type = "A320"
ac1.seats = 280

ac2 = aircraft.Aircraft()
ac2.callsign = "BS34J"
ac2.type = "A321"
ac2.seats = 310

print("=" * 5,"PHASE 2 TEST PROGRAM", "=" * 5, "\n")
print("Functions this week:")
funcs = ["plot_assignment", "plot_assignments", "assign_aircraft", "assign_flight", "show_assignment"]
for f in funcs:
    print(f"\t{f}")

input("\n - PRESS ENTER TO TEST ASSIGN_AIRCRAFT AND ASSIGN_FLIGHT:")

if assignment.assign_aircraft(ass1, ac1):
    print("ac1 assigned to ass1")
else:
    print("Couldn't assign ac1 to ass1")

# What if we try to add another aircraft to the same assignment
if assignment.assign_aircraft(ass1, ac2):
    print("Aircraft was successfully assigned.")
else:
    print("Couldn't assign ac2 to ass1")

# But what if we add first a flight?
ass2.flights.append(flights[0])

if assignment.assign_aircraft(ass2, ac2):
    print("Aircraft was successfully assigned.")
else:
    print("Couldn't assign ac2 to ass2")

# Empty the flights list
ass2.flights = []
if assignment.assign_aircraft(ass2, ac2):
    print("Aircraft was successfully assigned.")
else:
    print("Couldn't assign ac2 to ass2")

# Try assigning some flights
for i, f in enumerate(flights):
    if assignment.assign_flight(ass1, f):
        # Remove the assigned flight from the list, to not assign it again
        flights = flights[:i] + flights[i + 1:]

# Try assigning some flights
for i, f in enumerate(flights):
    if assignment.assign_flight(ass2, f):
        # Remove the assigned flight from the list, to not assign it again
        flights = flights[:i] + flights[i + 1:]

input("\n - PRESS ENTER TO TEST SHOW_ASSIGNMENT:")

assignment.show_assignment(ass1)

assignment.show_assignment(ass2)

input("\n - PRESS ENTER TO TEST PLOT_ASSIGNMENT:")
print("Plotting ass1...")
assignment.plot_assignment(ass1)

print("Plotting ass2...")
assignment.plot_assignment(ass2)

input("\n - PRESS ENTER TO TEST PLOT_ASSIGNMENTS:")
print("Plotting ass1 and ass2 together...")
assignment.plot_assignments([ass1, ass2])