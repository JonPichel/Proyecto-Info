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
    

def read_aircrafts(f):
    """ Function read_aircrafts (f: String):
    ===================================================
    Reads each line of a file containing a list of aircraft and creates a vector with the data found
    f: String, the name of the file
    Created by Pol Roca on May 14th 2020
    """

     try:

        F=open(f,'r')

        file_content=F.readlines()
        file_content=file_content[1:]

        contador=0
        vector_aircrafts=[]

        for i in file_content:
            try:
                y=file_content[contador].split()
                z=y[2].replace('/n','')
                callsign=y[0]
                actype=y[1]
                seats=int(y[2])
                contador+=1
            except:
                print("The format of the line " contador+1 " is not valid")
                contador+=1
                continue
            vector_aircrafts.append(file_content[contador-1])
        return vector_aircrafts

    except FileNotFoundError:
        print("This file doesn't exist, please enter a correct file")
        return []
