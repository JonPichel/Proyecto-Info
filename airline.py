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

def add_aircraft(a,ac):
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
        m=0                         # m and n are used to see if there is no repetition in every single operation in a.operations list
        for i in a.operations:      # for loop to see the enire a.operations list
            if i == None:           # see if the a.operations is empty
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