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
      print("Wrong parameters. Provide an Aircraft object.")
      return
    # Check if some information is missing
    if not callsign:
        callsign = 'UNKNOWN CALLSIGN'
    if not atype:
        atype = 'UNKNOWN AIRCRAFT TYPE'
    
    print(callsign, '(' + atype, 'with', seats, 'seats)')