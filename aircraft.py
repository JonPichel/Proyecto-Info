class Aircraft:
    """ Aircraft ()
    ===================================================
    Defines class Aircraft
    Attributes are:
    callsign: string, callsign of the aircraft
    type: string, type of the aircraft
    seats: integer, number of seats of the aircraft
    """
    def __init__(self):
        self.callsign = ""
        self.type = ""
        self.seats = 0
        
def show_aircraft(a):
    """ Function show_aircraft (a: Aircraft):
    ===================================================
    Prints on the screen the data of an aircraft
    a: Aircraft, the aircraft whose information will be printed
    Created by Raul Criado on April 17th 2020
    Tested by Jonathan Pichel on April 18th 2020
    """
    try:
        callsign = a.callsign
        atype = a.type
        seats = a.seats
    except AttributeError:
      print(" [ERROR] (show_aircraft) Wrong parameters. Provide an Aircraft object.")
      return
    # Check if some information is missing
    if not callsign:
        callsign = 'UNKNOWN CALLSIGN'
    if not atype:
        atype = 'UNKNOWN AIRCRAFT TYPE'
    
    print(callsign, '(' + atype, 'with', seats, 'seats)')
    
def read_aircrafts(f):
    """ Function read_aircrafts (f: String):
    ===================================================
    Reads each line of a file containing a list of aircraft and creates a vector with the data found
    f: String, the name of the file
    Created by Pol Roca on May 14th 2020
    Fixed and tested by Jonathan Pichel on May 25th 2020
    """
    # We iterate through all the lines of the file
    aircrafts = []

    # We enumerate the iteration to be able to communicate errors to the user
    try:
        for i, line in enumerate(open(f, 'r')):
            # We don't process the header, in case there is one
            if not line.startswith('CALLSIGN AC-TYPE SEATS'):
                words = line.split()
                try:
                    if len(words) != 3:
                        raise IndexError
                    callsign = words[0]
                    model = words[1]
                    seats = int(words[2])
                except (IndexError, ValueError) as format_exception:
                    print(f" [ERROR] (read_aircrafts) Wrong format at line {i + 1}.")
                # If there was no errors, add the aircraft
                else:
                    a = Aircraft()
                    a.callsign = callsign
                    a.type = model
                    a.seats = seats
                    aircrafts.append(a)

        return aircrafts
    except FileNotFoundError:
        print(" [ERROR] (read_aircrafts) File couldn't be found.")
        return
    except PermissionError:
        print(" [ERROR] (read_aircrafts) You don't have permissions over that file.")
        return
