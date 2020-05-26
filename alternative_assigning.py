def chain_potential(f, vf):
    if f.time_arr <= f.time_dep:
        return (0, f.passengers)
    subsequent = [fl for fl in vf if fl.time_dep >= (f.time_arr + 60)]
    chainable = [fl for fl in subsequent if fl.dep == f.arr]
    # If there are not chainable flights, the maximum will be 0
    if not chainable:
        potential = 0
        max_seats = f.passengers
    else:
        maximum = 0
        for fl in chainable:
            # Recursively call chain_potential for the chainable flights
            potential, seats = chain_potential(fl, subsequent)
            if potential >= maximum:
                maximum = potential
                max_seats = seats
        potential = maximum + 1
    # If this flight is the more crowded one, update max_seats
    if f.passengers > max_seats:
        max_seats = f.passengers
    return (potential, max_seats)

if __name__ == '__main__':
    flights = read_flights('FL.txt')
    for fl in flights:
        show_flight(fl)
        print(chain_potential(fl, flights))

def assign_operations(a):
    """Function assign_operations (a: airline)
    ===================================================
    Allocates the flights to each aircraft of the fleet
    a: object of class airline
    Created by Jonathan Pichel on May 9th 2020
    Tested by Pol Roca on May 9th 2020
    """
    try:
        # Copy the airline information
        name = a.name
        # We store the aircrafts based on their seats: if it has less seats, it goes first
        # This helps us assign flights more efficiently, since flights that has less passengers
        # will fit on the smaller aircrafts
        aircrafts = sorted(a.aircrafts, key=lambda ac: ac.seats)
        # We are also interested in storing the aircrafts by time of departure
        flights = flight.sort_flights(a.operations)
        assignments = []
    except AttributeError:
        print(" [ERROR] (assign_operations) Wrong Parameters, please provide an Assignment, an Aircraft and a Flight")
        return False

    # Create an assignment for each aircraft
    for i in range(len(aircrafts)):
        assig = assignment.Assignment()
        assignment.assign_aircraft(assig, aircrafts[i])
        assignments.append(assig)
    
    for fl in flights:
        fl.potential, fl.max_seats = flight.chain_potential(fl, flights)

    # We sort the flight by their "chain potential"
    sorted_flights = flight.sort_flights(flights, potential=True)
    for i in range(len(flights)):
        f = sorted_flights[i]
        for j in range(len(assignments)):
            assig = assignments[j]
            if assig.aircraft.seats >= f.max_seats:
                if assignment.assign_flight(assig, f):
                    break
        else:
            for j in range(len(assignments)):
                assig = assignments[j]
                if assignment.assign_flight(assig, f):
                    break
            else:
                # If the inner for loop finished without breaking, it means that the flight
                # was incompatible with all the assignments
                flight.show_flight(f)
                print("could not be assigned.")
    # Return the updated airline
    new = Airline()
    new.name = name
    new.aircrafts = aircrafts
    new.operations = flights
    new.assignments = assignments
    return new