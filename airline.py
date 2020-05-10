import matplotlib.pyplot as plt

import aircraft, flight, assignment

class Airline:
    """ Airline ()
    ===================================================
    Defines class Airline
    Attributes are:
    name: string, name of the airline
    aircrafts: list, aircrafts of the airline
    operation: list, operations made by the airline (flights)
    assignments: list, the relations between flights and aircrafts
    """
    def __init__(self):
        self.name = ""
        self.aircrafts = []
        self.operations = []
        self.assignments = []

def show_airline(a):
    """ Function show_airline (f)
    ==================================================
    Prints on the screen the information of an airline
    a: Airline, the flight data will be printed
    Created by Jonathan Pichel on April 21th 2020
    Tested by Pol Roca on April 22th 2020
    """
    try:
        name = a.name
        aircrafts = a.aircrafts
        operations = a.operations
        assignments = a.assignments
    except AttributeError:
        print("Wrong parameters. Provide an Airline object.")
        return
    print("Airline information:")
    print("Name:", name)
    print("It has a fleet of", len(aircrafts), "Aircraft:")
    for a in aircrafts:
        # The end='' tells prevents the print function to insert a newline
        print('\t', end='')
        aircraft.show_aircraft(a)
    print("Operations today are", str(len(operations)) + ":")
    for f in operations:
        # The end='' tells prevents the print function to insert a newline
        print('\t', end='')
        flight.show_flight(f)
    for assig in assignments:
        # The end='' tells prevents the print function to insert a newline
        assignment.show_assignment(assig)

def add_aircraft(a, ac):
    """ Function add_aircraft (a: Airline(), ac: Aircraft()): Boolean
    ===================================================
    Adds an aircraft to the airline if it isn't added yet
    a: object of class Airline, the airline which function shall add the aircraft
    ac: object of class Aircraft, the aircraft which function shall add to the airline
    Return: boolean, True if the addition is correct, False if its being added a repeated aircraft
    Created by Adrià Vaquer on April 21st 2020
    Tested by Raúl Criado on April 22nd 2020
    """
    try:
        for i in a.aircrafts:   # for loop to see the entire a.aircrafts list
            if i.callsign == ac.callsign:   # condition for repeated aircraft
                return False # If it's repeated it returns False 
        # If it didn't break the loop, we can add the aircraft
        a.aircrafts.append(ac)
        return True
    except AttributeError:
        print("Wrong parameters, please provide an Airline and an Aircraft")
        return False
        
def add_operation(a,f):
    """ Function add_operation (a: Airline(), f: Flight()): Boolean
    ===================================================
    Adds an operation to the airline if it isn't added yet
    a: object of class Airline, the airline which function shall add the operation
    f: object of class Flight, the operation which function shall add to the airline
    Return: boolean, True if the addition is correct, False if its being added a repeated operation
    Created by Adrià Vaquer on April 21st 2020
    Tested by Raúl Criado on April 22nd 2020
    """
    try:
        for i in a.operations:              # for loop to see the enire a.operations list
            if i.dep == f.dep and i.arr == f.arr and i.time_dep == f.time_dep and i.time_arr == f.time_arr:  # conditions for repeated operation
                return False
        # If it didn't break the loop, we can add the aircraft
        a.operations.append(f)
        return True
    except AttributeError:
        print("Wrong parameters, please provide an Airline and a Flight")
        return False

def insert_delay(a, depAp, depTm, d):
    """ Function insert_delay (a, depAp, depTm, d) -> bool
    ==================================================
    Checks if it exists a flight, and adds a delay to it.
    a: Airline
    depAp: string, name of the airport
    depTm: int, time of departure
    d: int, time delayed in minutes
    Return: True if the flight exists and update the time departure adding the delay.
    Created by Raul Criado on May 1st 2020
    Tested by Jonathan Pichel on May 4th 2020
    """
    try:
        flights = a.operations
        for i in range(len(flights)):
            if flights[i].dep == depAp and flights[i].time_dep == depTm:    # Checks if the flight matches
                flight.delay_flight(flights[i], d)                          # We call the delay_flight function to apply it in that case
                return True
        return False                                                        # If the flight doesn't match returns False
    except AttributeError:
        print("Wrong parameters.")
        return False

def check_operations(a, interval=60):
    """ Function check_operations(a)
    ==================================================
    This function checks if fights can be allocated
    a = object of class Airline
    interval: int, minimum number of minutes that must exist between the flights
    This function has a boolean as output parameter
    Returns if a flight can be allocated or not and prints what is the error. Check if the departure and 
    arrival airport of consecutive flights are the same, if there is at least 60 min between arrival and
    departure and if passengers fit in the aircraft 
    Created by Raul Criado on May 1st 2020
    Tested by Jonathan Pichel on May 9th 2020
    """
    try:
        for assig in a.assignments:
            # Check if all the flights fit in the aircraft
            for f in assig.flights:
                if not flight.fits_flight_in_aircraft(f, assig.aircraft):
                    print("Flight:", flight.show_flight(f), "doesn't fit in the aircraft", aircraft.show_aircraft(assig.aircraft))
                    return False

            # Check if they are adequately spaced in time
            if flight.check_inner_overlap(assig.flights, interval=interval):
                print("Flights overlap in time.")
                return False
        
            # Check if the airports' order is logical
            if not flight.check_airports(assig.flights):
                print("The airport's order doesn't make sense.")
                return False
            return True
    except AttributeError:
        print("Wrong Parameters.")
        return False
    
def plot_flights(a, title=None):
    """Function plot_flights (a: Airline()): none
    ==========================================
    Plots the list of flight operations of an airline
    a: object of class Airline, the airline which function shall plot the operations
    title: str, if provided, it will set the title of the plot
    Created by Adrià Vaquer on May 5th 2020
    Tested by Raúl Criado on May 6th 2020
    """
    if type(a) == Airline:
        flight.plot_flights(a.operations, title=title)
    else:
        print("Wrong Parameters, please provide an Airline")

def plot_assignments(a, title=None):
    """Function plot_assignments (a: airline)
    ===================================================
    Plots a list of assignments
    a: object of class airline
    title: str, if provided, it will set the title of the plot
    Created by Raúl Criado on May 6th 2020
    Tested by Jonathan Pichel on May 9th 2020
    """
    try:
        # We call the plot_assignments function to add it to the class airline
        assignment.plot_assignments(a.assignments, title=title)
    except AttributeError:
        print("Wrong Parameters, please provide an Assignment")
        return False

def assign_operations(a):
    """Function assign_operations (a: airline)
    ===================================================
    Allocates the flights to each aircraft of the fleet
    a: object of class airline
    The function keeps on assigning even if it founds an incompatibility, in that case it prints a message informing about the flight that cannot be assigned
    Created by Jonathan Pichel on May 9th 2020
    Tested by Pol Roca on May 9th 2020
    """
    try:
        # Copy the airline information
        name = a.name
        aircrafts = a.aircrafts[:]
        flights = a.operations[:]
        assignments = []
    except AttributeError:
        print("Wrong Parameters, please provide an Assignment, an Aircraft and a Flight")
        return False
    # Create an assignment for each aircraft
    for i in range(len(aircrafts)):
        assig = assignment.Assignment()
        assig.aircraft = aircrafts[i]
        assignments.append(assig)
    for i in range(len(flights)):
        f = flight.sort_flights(flights)[i]
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
