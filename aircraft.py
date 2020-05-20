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

    vector_aircrafts=[]

    try:
        F=open(f,'r')

        vector_aircrafts=F.readlines()
        vector_aircrafts=vector_aircrafts[1:]

        contador=0
        errorinline=[]
    
        for i in vector_aircrafts:
                
            vector_aircrafts[contador]=i[:-1]

            test=vector_aircrafts[contador].split()
            try:
                test[2]=int(test[2])
            except ValueError:
                errorinline.append(contador)
                    
            contador+=1
                
            if contador+1==len(vector_aircrafts):
                break

        test=vector_aircrafts[-1].split()
        try:
            test[2]=int(test[2])
        except ValueError:
            errorinline.append(contador)

        contador=0
        for i in errorinline:
            vector_aircrafts.pop(errorinline[contador])
            contador2=0
            for o in errorinline:
                errorinline[contador2]=errorinline[contador2]-1
                contador2+=1
            contador+=1

        return vector_aircrafts

    except FileNotFoundError:
        print("This file doesn't exist, please enter a correct file")
        return vector_aircrafts
