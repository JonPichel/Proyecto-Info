import matplotlib.pyplot as plt

import aircraft, flight

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
    except AttributeError:
        print("Wrong parameters. Provide an Airline object.")
        return
    print("Airline information:")
    print("\tName:", name)
    print("\tIt has a fleet of", len(aircrafts), "Aircraft:")
    for a in aircrafts:
        # The end='' tells prevents the print function to insert a newline
        print('\t' * 2, end='')
        aircraft.show_aircraft(a)
    print("\tOperations today are", str(len(operations)) + ":")
    for f in operations:
        # The end='' tells prevents the print function to insert a newline
        print('\t' * 2, end='')
        flight.show_flight(f)
     assignment.plot_assignments(assignments)

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
        n=len(a.aircrafts)      # m and n are used to see if there is no repetition in every single aircraft in a.aircrafts list
        m=0
        for i in a.aircrafts:   # for loop to see the entire a.aircrafts list
            if i == None:       # see if the a.aircraft is empty
                a.aircrafts.append(ac)
                return True
            else:
                if i.callsign != ac.callsign:   # condition for repeated aircraft
                    m+=1
        if m==n:                            # See if the aircraft we are trying to add isn't repeated
            a.aircrafts.append(ac) 
            return True
        else:
            return False       # If it's not repeated it returns True, if it's repeated it returns False 
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
        n=len(a.operations)
        m=0                                 # m and n are used to see if there is no repetition in every single operation in a.operations list
        for i in a.operations:              # for loop to see the enire a.operations list
            if i == None:                   # see if the a.operations is empty
                a.operations.append(f)
                return True
            else:
                if i.dep == f.dep and i.arr == f.arr and i.time_dep == f.time_dep:  # conditions for repeated operation
                    return False
                else:
                    m+=1
        if m==n:                    # See if the operation we are trying to add isn't repeated
            a.operations.append(f)
            return True
        else:
            return False        # If it's not repeated it returns True, if it's repeated it returns False
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
    d: object of class Airline, integer
    Return: True if the flight exists and update the time departure adding the delay.
    Created by Raul Criado on May 1st 2020
    Tested by Jonathan Pichel Carrera on May 4th 2020
    """
    try:
        a = a.assignments
        flights = a.flights
        for i in range(len(flights)):
            if flights[i].dep == depAp and flights[i].time_dep == depTm:    # Checks if the flight matches
                flight.delay_flight(flights[i], d)                          # We call the delay_flight function to apply it in that case
                return True
        return False                                                        # If the flight doesn't match returns False
    except AttributeError:
        print("Wrong parameters.")
        return False


def check_operations(a):
    """ Function check_operations(a)
    ==================================================
    This function checks if fights can be allocated
    a = object of class Airline
    This function has a boolean as output parameter
    Returns if a flight can be allocated or not and prints what is the error. Check if the    departure and arrival airport of consecutive flights are the same, if there is at least 60 min between arrival and departure and if passengers fit in the aircraft 
    Created by Raul Criado on May 1st 2020
    """
    try:
        a = a.assignments
        flights = a.flights
        for i in range(len(flights)):
            m = i + 1                                                                       # A variable that allows us to check the arrival and compare it with the previous departure
            if i.dep != m.arr:                                                              # Checks if the departure airport is the same of the next flight arrival airport
                print('Arrival airport m.arr not match with departure airport m.dep')
                return False

            elif i.seats < a.passengers:                                                    # Checks if the passengers of the flight fits in the aircraft assigned
                print('Flight passengers do not fit in the aircraft')
                return False

            elif (i.time_dep - i.time_arr) >= 60:                                           # Checks if the time difference between arrival and departure is over 60 minutes
                print('There are less than 60 min time between arrival and departure')
                return False

    except AttributeError:
        print("Wrong parameters, please provide an Airline and a Flight")
        return False

    
def plot_flights(a):
    """Function plot_flights (a: Airline()): none
    ==========================================
    Plots the list of flight operation of an airline
    a: object of class Airline, the airline which function shall plot the operations
    Return: none
    Created by Adrià Vaquer on May 5th 2020
    Tested by Raúl Criado on May 6th 2020
    """
    if type(a) == Airline:
        flight.plot_flights(a.operations)
    else:
        print("Wrong Parameters, please provide an Airline")


def plot_assignments(a):
    """Function plot_assignments (a: airline)
    ===================================================
    Plots a list of assignments
    a: object of class airline
    Created by Raúl Criado on May 6th 2020
    """
    plot_assignments(a.assignments)
    # We call the plot_assignments function to add it to the class airline


def assign_operations(a):
    # Copy the airline information
    aircrafts = a.aircrafts[:]
    flights = a.flights[:]
    assignments = []
    # Create an assignment for each aircraft
    for i in range(len(new.aircrafts)):
        assig = assignment.Assignment()
        assig.aircraft = new.aircrafts[i]
        new.assignments.append(assig)
    for i in range(len(new.flights)):
        flight = new.flights[i]
        for j in range(len(new.assignments)):
            assig = new.assignments[j]
            if assignment.assign_flight(assig, flight):
                break
        else:
            # If the inner for loop finished without breaking, it means that the flight
            # was incompatible with all the assignments
            print("Flight:", flight.show_flight(flight), "could not be assigned.")
    # Return the updated airline
    new = airline.Airline()
    new.aircrafts = aircrafts
    new.flights = flights
    new.assignments = assignments
    return new


