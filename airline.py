import matplotlib.pyplot as plt

import aircraft, flight, assignment, airport

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
        print(" [ERROR] (show_airline) Wrong parameters. Provide an Airline object.")
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
        print(" [ERROR] (add_aircraft) Wrong parameters, please provide an Airline and an Aircraft")
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
        print(" [ERROR] (add_operation) Wrong parameters, please provide an Airline and a Flight")
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
        print(" [ERROR] (insert_delay) Wrong parameters.")
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
        print(" [ERROR] (check_operations) Wrong Parameters.")
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
    try:
        flight.plot_flights(a.operations, title=title)
    except AttributeError:
        print(" [ERROR] (plot_flights) Wrong Parameters, please provide an Airline")
        return

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
        print(" [ERROR] (plot_assignments) Wrong Parameters, please provide an Assignment")
        return False

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
        aircrafts = a.aircrafts[:]
        flights = a.operations[:]
        assignments = []
    except AttributeError:
        print(" [ERROR] (assign_operations) Wrong Parameters, please provide an Assignment, an Aircraft and a Flight")
        return False
    # Create an assignment for each aircraft
    for i in range(len(aircrafts)):
        assig = assignment.Assignment()
        assignment.assign_aircraft(assig, aircrafts[i])
        assignments.append(assig)
    sorted_flights = flight.sort_flights(flights)
    for i in range(len(flights)):
        f = sorted_flights[i]
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

def write_day_plan(a, f):
    """Function write_day_plan (a: Airline, f: str): bool
    ===================================================
    Reads from a file that contains the information about some airports, and creates them
    Writes the information about the assignments and operations of the day of an airline to a file.
    a: Airline, airline whose information will be stored
    f: str, name of the file where data is stored
    Returns: list containing the airports that were created
    Created by Jonathan Pichel on May 11th 2020
    """
    try:
        output = open(f, 'w')
        output.write(f"Today operations of {a.name}\n\n")
        for assig in a.assignments:
            output.write(assignment.write_assignment(assig))
        # Show also the unassigned flights
        unassigned = []
        for fl in a.operations:
            for assig in a.assignments:
                if fl in assig.flights:
                    break
            else:
                unassigned.append(fl)
        if unassigned:
            output.write(f"{len(unassigned)} flights not assigned:\n")
            for fl in unassigned:
                output.write(f"\t{flight.format_time(fl.time_dep, colon=False)} {flight.format_time(fl.time_arr, colon=False)}")
                output.write(f" {fl.dep} {fl.arr} {fl.passengers}\n")

        output.close()
        return True
    except PermissionError:
        print(" [ERROR] (write_day_plan) You don't have permissions over that file.")
        return False

def calculate_day_costs(a, vp):
    """Function calculate_day_costs(a,vp):
    ===================================================
    Calculates the total airport fees to be paid along the day
    a: object of class airline
    vp: list of aiports
    Created by Raúl Criado on May 11th 2020
    Fixed and tested by Jonathan Pichel on May 27th 2020
    """
    try:
        assignments = a.assignments
        total_cost = 0
        for assig in assignments:
            flights = flight.sort_flights(assig.flights)
            assig_cost = 0
            for i in range(1, len(flights) - 1):
                code = flights[i - 1].arr
                index = airport.search_airport_index(vp, code)
                if index == -1:
                    print(f" [ERROR] (calculate_day_costs) Airport {code} not found.")
                    return -1
                time = flights[i].time_dep - flights[i - 1].time_arr 
                if time < 0:
                    print(" [ERROR] (calculate_day_costs) There has been an error sorting the flights.")
                    return -1
                assig_cost += airport.calculate_fee(vp[index], time)
            # The last plane of the day will pay till 5 AM of the next day
            last = flights[-1]
            if last.time_dep > last.time_arr:
                # It crosses through midnight
                time = 5 * 60 - last.time_arr
            else:
                # It doesn't cross through midnight
                time = 24 * 60 - last.time_arr + 5 * 60
            index = airport.search_airport_index(vp, last.arr)
            if index == -1:
                print(f" [ERROR] (calculate_day_costs) Airport {last.arr} not found.")
                return -1
            if time < 0:
                print(" [ERROR] (calculate_day_costs) Error on the timing of the last flight.")
            assig_cost += airport.calculate_fee(vp[index], time)
            total_cost += assig_cost
        return total_cost
    except AttributeError:
        print(" [ERROR] (calculate_day_costs) Wrong Parameters, please provide an Assignment or an Airport")
        return False

def read_airline(f):
    """ Function read_airline (f: String):
    ===================================================
    this function reads the content of the file f to initialize a new airline with the data found
    f: String, the name of the file
    Created by Pol Roca on May 18th 2020
    Fixed and tested by Jonathan Pichel on May 25th
    """
    try:
        a = Airline()
        file = open(f, 'r')

        lines = [line.strip() for line in file.readlines()]
        if len(lines) != 3:
            print(" [ERROR] (read_airline) Wrong format.")
            return
        a.name = lines[0]
        a.aircrafts = aircraft.read_aircrafts(lines[1])
        a.operations = flight.read_flights(lines[2])
        if a.aircrafts == None or a.operations == None:
            print(" [ERROR] (read_airline) Wrong format or unreachable subfiles.")
            return
        return a
    except FileNotFoundError:
        print(" [ERROR] (read_airline) File couldn't be found.")
        return
    except PermissionError:
        print(" [ERROR] (read_airline) You don't have permissions over that file.")
        return
