import random

import aircraft, flight

def createFlights():
    # creates first flight with some values
    f1 = flight.Flight()
    f1.dep = "Barcelona"
    f1.arr = "Budapest"
    f1.time_dep = 8*60
    f1.time_arr = 11*60
    f1.passengers = 54

    # creates second flight with some values
    f2 = flight.Flight()
    f2.dep = "Barcelona"
    f2.arr = "Istambul"
    f2.time_dep = 9*60
    f2.time_arr = 12.5*60
    f2.passengers = 154

    # creates third flight with some values
    f3 = flight.Flight()
    f3.dep = "Istambul"
    f3.arr = "Budapest"
    f3.time_dep = 17*60
    f3.time_arr = 19.25*60
    f3.passengers = 140

    # creates fourth flight with some values
    f4 = flight.Flight()
    f4.dep = "Budapest"
    f4.arr = "Barcelona"
    f4.time_dep = 12*60
    f4.time_arr = 15*60
    f4.passengers = 97

    # creates fifth flight with some values
    f5 = flight.Flight()
    f5.dep = "Barcelona"
    f5.arr = "Vigo"
    f5.time_dep = 20.75*60
    f5.time_arr = 23*60
    f5.passengers = 113

    # creates sixth flight with some values
    f6 = flight.Flight()
    f6.dep = "Vigo"
    f6.arr = "Barcelona"
    f6.time_dep = 4*60
    f6.time_arr = 5.25*60
    f6.passengers = 278

    return f1, f2, f3, f4, f5, f6

if __name__ == '__main__':
    # Create some flights
    flights = [f1, f2, f3, f4, f5, f6] = createFlights()

    # Create an aircraft
    ac = aircraft.Aircraft()
    ac.callsign = "AC320F"
    ac.type = "A320"
    ac.seats = 220

    print("=" * 5,"PHASE 1 TEST PROGRAM", "=" * 5, "\n")
    print("Functions this week:")
    funcs = ["format_time", "show_flight", "fits_flight_in_aircraft", "flight_duration", "delay_flight"]
    for f in funcs:
        print(f"\t{f}")

    input("\n - PRESS ENTER TO TEST SHOW_FLIGHT, FLIGHT_DURATION AND FORMAT_TIME:")
    # Show all the initial values
    for f in flights:
        flight.show_flight(f)
        # As you can see, format_time returns a nice string with the time in HH:MM format
        print("Flight duration:", flight.format_time(flight.flight_duration(f)) + 'h\n')

    # Delay flights
    input(" - PRESS ENTER TO TEST DELAY_FLIGHT:")
    delays = [30, -30, 50.54, 180, -200, 60000]
    for i in range(len(flights)):
        if flight.delay_flight(flights[i], delays[i]):
            print(f"Flight f{i+1} could be delayed.")
        else:
            print(f"Couldn't delay Flight f{i+1}.")

    input("\n - PRESS ENTER TO TEST FITS_FLIGHT_IN_AIRCRAFT:")
    for f in flights:
        if flight.fits_flight_in_aircraft(f, ac):
            print("Flight from", f.dep, "to", f.arr, "fits in aircraft.")
        else:
            print("Flight from", f.dep, "to", f.arr, "doesn't fit in aircraft.")

    print("=" * 5,"PHASE 1 TEST PROGRAM END", "=" * 5, "\n")

    print("=" * 5,"PHASE 2 TEST PROGRAM", "=" * 5, "\n")
    print("Functions this week:")
    funcs = ["check_overlap", "check_overlap_list", "check_inner_overlap", "plot_flight", "plot_flights", "sort_flights", "check_airport"]
    for f in funcs:
        print(f"\t{f}")

    input("\n - PRESS ENTER TO TEST ALL CHECK_OVERLAP FUNCTIONS:")
    print("check_overlap:")
    pairs = ["1-2", "1-4", "3-6", "4-5"]
    for pair in pairs:
        a = int(pair[0]) - 1
        b = int(pair[2]) - 1
        if flight.check_overlap(flights[a], flights[b]):
            print(f"Flights {pair} collide in time")
        else:
            print(f"Flights {pair} are adequately spaced in time")

    print("check_overlap_list:")
    if flight.check_overlap_list(f1, flights):
        print("List flights overlaps with f1, because f1 is contained in flights")
    else:
        print("If this shows up, there is a problem with the function")

    if flight.check_overlap_list(f1, [f3, f5]):
        print("List of f3 and f5 overlaps with f1")
    else:
        print("List of f3 and f5 doesn't overlap with f1")

    print("check_inner_overlap:")
    lists = ["13", "456", "126"]
    for l in lists:
        ff = [flights[int(c) - 1] for c in l]
        if flight.check_inner_overlap(ff):
            print("List with flights", l, "has inner overlap.")
        else:
            print("Flights in", l, "don't collide.")

    input("\n - PRESS ENTER TO TEST SORT_FLIGHTS:")

    print("Here the flights are unordered:")
    for f in flights:
        print('\t', flight.format_time(f.time_dep), sep='')

    print("As we can see, flights are now ordered by time of departure:")
    for f in flight.sort_flights(flights):
        print('\t', flight.format_time(f.time_dep), sep='')


    input("\n - PRESS ENTER TO TEST CHECK_AIRPORTS:")
    lists = [[f1, f4], [f2, f3, f4]]
    for l in lists:
        mess = ""
        for f in flight.sort_flights(l):
            mess += f"{f.dep}-{f.arr}, "
        mess += "does it make sense?:"
        print(mess, flight.check_airports(l))

    input("\n - PRESS ENTER TO TEST PLOT_FLIGHT:")
    # Test plot_flight
    print("Plotting f1...")
    flight.plot_flight(f1)

    input("\n - PRESS ENTER TO TEST PLOT_FLIGHTS:")
    # Test plot_flights
    print("Plotting flights...")
    print("This function always plots the flights ordered by time of departure")
    flight.plot_flights(flights)