import aircraft,flight,airline,assignment

def createXicaAirline():
    """ Function createXicaAirline
    ==============================
    This function has no input parameters
    Returns an airline with 2 aircraft and 4 flights
    """ 
    # creates first aircraft with some values
    AC1 = aircraft.Aircraft()
    AC1.callsign = "EC234"
    AC1.type = "A320"
    AC1.seats = 280
    # creates a second aircraft with other values
    AC2 = aircraft.Aircraft()
    AC2.callsign = "EC504"
    AC2.type = "A321"
    AC2.seats = 310

    # creates first flight with some values
    FL1 = flight.Flight()
    FL1.dep = "Barcelona"
    FL1.arr = "Budapest"
    FL1.time_dep = 8*60
    FL1.time_arr = 11*60
    FL1.passengers = 54
    # creates second flight with some values
    FL2 = flight.Flight()
    FL2.dep = "Barcelona"
    FL2.arr = "Istambul"
    FL2.time_dep = 9*60
    FL2.time_arr = 12.5*60
    FL2.passengers = 154
    # creates third flight with some values
    FL3 = flight.Flight()
    FL3.dep = "Istambul"
    FL3.arr = "Budapest"
    FL3.time_dep = 17*60
    FL3.time_arr = 19.25*60
    FL3.passengers = 140
    # creates fourth flight with some values
    FL4 = flight.Flight()
    FL4.dep = "Budapest"
    FL4.arr = "Barcelona"
    FL4.time_dep = 20*60
    FL4.time_arr = 23*60
    FL4.passengers = 97

    # creates the airline
    Xica = airline.Airline()
    Xica.name = "Xica Airline"
    airline.add_aircraft(Xica, AC1)
    airline.add_aircraft(Xica, AC2)
    airline.add_operation(Xica, FL1)
    airline.add_operation(Xica, FL2)
    airline.add_operation(Xica, FL3)
    airline.add_operation(Xica, FL4)
    return Xica

def createAirline(x=False, y=False):
    """ Function createXicaAirline
    ==============================
    This function has no input parameters
    Returns an airline with 2 aircraft and 4 flights
    """ 
    # creates first aircraft with some values
    AC1 = aircraft.Aircraft()
    AC1.callsign = "EC234"
    AC1.type = "A320"
    AC1.seats = 280

    # creates a second aircraft with other values
    AC2 = aircraft.Aircraft()
    AC2.callsign = "EC504"
    AC2.type = "A321"
    AC2.seats = 310
    
    # creates a third wrong aircraft with the same values of AC2
    AC3 = aircraft.Aircraft()
    AC3.callsign = "EC504"
    AC3.type = "A321"
    AC3.seats = 310

    # creates first flight with some values
    FL1 = flight.Flight()
    FL1.dep = "Barcelona"
    FL1.arr = "Budapest"
    FL1.time_dep = 8*60
    FL1.time_arr = 11*60
    FL1.passengers = 54

    # creates second flight with some values
    FL2 = flight.Flight()
    FL2.dep = "Budapest"
    FL2.arr = "Florencia"
    FL2.time_dep = 13*60
    FL2.time_arr = 16*60
    FL2.passengers = 154

    # creates third flight with some values
    FL3 = flight.Flight()
    FL3.dep = "Florencia"
    FL3.arr = "Barcelona"
    FL3.time_dep = 18*60
    FL3.time_arr = 20*60
    FL3.passengers = 140

    # creates fourth flight with some values
    FL4 = flight.Flight()
    FL4.dep = "Madrid"
    FL4.arr = "Sevilla"
    FL4.time_dep = 8*60
    FL4.time_arr = 9*60
    FL4.passengers = 97

    # creates fifth flight with some values
    FL5 = flight.Flight()
    FL5.dep = "Sevilla"
    FL5.arr = "Vigo"
    FL5.time_dep = 12*60
    FL5.time_arr = 16*60
    FL5.passengers = 113

    # creates sixth flight with some values
    FL6 = flight.Flight()
    FL6.dep = "Vigo"
    FL6.arr = "Madrid"
    FL6.time_dep = 18*60
    FL6.time_arr = 20*60
    FL6.passengers = 200
    
    # creates seventh wrong flight with the same values of FL3
    FL7 = flight.Flight()
    FL7.dep = "Florencia"
    FL7.arr = "Barcelona"
    FL7.time_dep = 18*60
    FL7.time_arr = 20*60
    FL7.passengers = 140
    
    if y == True:
        FL8 = flight.Flight()
        FL8.dep = "Florencia"
        FL8.arr = "Barcelona"
        FL8.time_dep = 20.5*60
        FL8.time_arr = 21*60
        FL8.passengers = 140
    
    if x==True:
        # creates first assignment with some values
        ASS1=assignment.Assignment()
        assignment.assign_aircraft(ASS1,AC1)
        assignment.assign_flight(ASS1,FL1)
        assignment.assign_flight(ASS1,FL2)
        assignment.assign_flight(ASS1,FL3)
        
        # creates a second assignment with some values
        ASS2=assignment.Assignment()
        assignment.assign_aircraft(ASS2,AC2)
        assignment.assign_flight(ASS2,FL4)
        assignment.assign_flight(ASS2,FL5)
        assignment.assign_flight(ASS2,FL6)


    # creates the airline
    Xica = airline.Airline()
    Xica.name = "Xica Airline"
    airline.add_aircraft(Xica, AC1)
    airline.add_aircraft(Xica, AC2)
    airline.add_aircraft(Xica, AC3)
    airline.add_operation(Xica, FL1)
    airline.add_operation(Xica, FL2)
    airline.add_operation(Xica, FL3)
    airline.add_operation(Xica, FL4)
    airline.add_operation(Xica, FL5)
    airline.add_operation(Xica, FL6)
    airline.add_operation(Xica,FL7)
    if y ==True:
        airline.add_operation(Xica,FL8)
    flight.sort_flights(Xica.operations)
    if y == True:
        Xica=airline.assign_operations(Xica)
    return Xica

if __name__ == "__main__":
    print("=" * 5, "PHASE 1 TEST PROGRAM", "=" * 5, "\n")
    print("Functions this week:")
    funcs = ["show_airline", "add_aircraft", "add_operation"]
    for f in funcs:
        print(f"\t{f}")
    
    input("\n - PRESS ENTER TO TEST SHOW_AIRLINE, ADD_AIRCRAFT ADD_OPERATION:")
    
    A = createAirline(False,False)
    airline.show_airline(A)
    
    print("=" * 5, "PHASE 1 TEST PROGRAM END", "=" * 5, "\n")
    print("=" * 5, "PHASE 2 TEST PROGRAM", "=" * 5, "\n")
    print("Functions this week:")
    funcs = ["show_airline(updated)", "plot_flights", "assign_operations", "plot_assignments", "insert_delay", "check_operations"]
    for f in funcs:
        print(f"\t{f}")
    
    input("\n - PRESS ENTER TO TEST SHOW_AIRLINE(UPDATED) and ASSIGN_OPERATIONS FUNCTIONS:")
    A = createAirline(True, False)
    B = airline.assign_operations(A)
    airline.show_airline(B)
    
    input("\n - PRESS ENTER TO TEST PLOT_FLIGHTS FUNCTION:")
    airline.plot_flights(B)
    input("\n - PRESS ENTER TO TEST PLOT_ASSIGNMENTS FUNCTION:")
    airline.plot_assignments(B)
    input("\n - PRESS ENTER TO TEST INSERT_DELAY FUNCTION:")
    delay = [30, -30, 50.54, 180, -200, 60000]
    for i in delay:
        if airline.insert_delay(B,"Barcelona",8*60,i):
            print("The flight can be delayed")
        else:
            print("Couldn't delay flight")
    input("\n - PRESS ENTER TO TEST CHECK_OPERATIONS FUNCTION:")
    C=createAirline(True,True)
    for i in C.operations:
        if airline.check_operations(B):
            print("The flight", i.dep,"-", i.arr, "can be allocated")
        else:
            print("The flight", i.dep, "-", i.arr, "can not be allocated")
