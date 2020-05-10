import aircraft,flight,airline,assignment

def createXicaAirline ():
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

if __name__ == '__main__':
    # main
    print("Phase1 test program")
    A = createXicaAirline()
    airline.show_airline(A)
    print("Phase1 test program end")

    ac1 = aircraft.Aircraft()
    ac1.callsign = 'AJ320'
    ac1.type = 'A320'
    ac1.seats = 280

    f1 = flight.Flight()
    f1.dep = "Barcelona"
    f1.arr = "Budapest"
    f1.time_dep = 8*60
    f1.time_arr = 11*60
    f1.passengers = 20

    f2 = flight.Flight()
    f2.dep = "Budapest"
    f2.arr = "Florencia"
    f2.time_dep = 13*60
    f2.time_arr = 16*60
    f2.passengers = 30

    f3 = flight.Flight()
    f3.dep = "Florencia"
    f3.arr = "Barcelona"
    f3.time_dep = 18*60
    f3.time_arr = 20*60
    f3.passengers = 10

    ass = assignment.Assignment()

    print(assignment.assign_aircraft(ass, ac1))
    print(assignment.assign_flight(ass, f1))
    print(assignment.assign_flight(ass, f2))
    print(assignment.assign_flight(ass, f3))

    assignment.plot_assignment(ass)
