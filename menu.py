import airline, aircraft, airport, assignment, flight

def initialize_data():
    while True:
        print("Reading options:\n")
        print("(l) airline")
        print("(p) airports")
        print("(d) airport data")
        print("(q) quit to main menu")

        option = input("What type of file do you want to read from?: ")
        # Initialize airline
        if option == 'l':
            filename = input("Name of the file to read from: ")
            al = airline.read_airline(filename)
            if al:
                airlines.append(airline.read_airline(filename))
                input("Airline correctly initialized.")
            else:
                input("There was an error reading the file.\n")
        # Initialize airport
        elif option == 'p':
            filename = input("Filename to read from: ")
            new_airports = airport.read_airports(filename)
            for ap in new_airports:
                if airport.search_airport_index(airports, ap.code) == -1:
                    print(f"Succesfully added airport: {ap.code}")
                    airports.append(ap)
        # Initialize airport data
        elif option == 'd':
            filename = input("Filename to read from: ")
            airport.read_airport_costs(airports, filename)
        elif option == 'q':
            break

def assign_flights():
    while True:
        name = input("Name of the airline (q to quit to main menu): ")
        if name == 'q':
            break
        al = [a for a in airlines if a.name == name]
        if al:
            airlines.remove(al[0])
            airlines.append(airline.assign_operations(al[0]))
            input(f"Operations of {name} assigned.")
        else:
            input(f"No airline found with name {name}.")

def kml_menu():
    print("(p) write kml of airports")
    print("(f) write kml of flights")
    print("(a) write kml of assignments")
    print("(q) quit to main menu")

    option = input("What do you want to save in kml?: ")
    if option == 'p':
        airport.map_airports(airports)
    elif option == 'f':
        name = input("Name of the airline to map flights: ")
        al, = (al for al in airlines if al.name == name)
        flight.map_flights(al.operations, airports)
    elif option == 'a':
        pass
    elif option == 'q':
        pass
    
def plot_menu():
    print("Plot menu options:\n")
    print("(a) plot all of the assignments of an airline")
    print("(s) plot a single assignment (by aircraft's callsign)")
    print("(f) plot airline operations")
    print("(q) quit to main menu")

    option = input("What do you want to plot?: ")
    if option == 'a':
        name = input("Name of the airline: ")
        al = [a for a in airlines if a.name == name]
        if al:
            input(f"Plotting flights for {al[0].name}...")
            airline.plot_assignments(al[0], title=f"Assignments of {al[0].name}")
        else:
            input("No airline found with name", name)
    elif option == 's':
        name = input("Name of the airline: ")
        callsign = input("Aircraft's callsign: ")
    elif option == 'f':
        name = input("Name of the airline: ")
        al = [a for a in airlines if a.name == name]
        if al:
            input(f"Plotting flights for {al[0].name}...")
            airline.plot_flights(al[0], title=f"Flights of {al[0].name}")
        else:
            input("No airline found with name", name)
    elif option == 'q':
        pass


def view_information():
    while True:
        print("Viewing options:\n")
        print("(l) airlines")
        print("(p) airports")
        print("(f) search for a flight")
        print("(q) quit to main menu")
        
        option = input("What information do you want to display?: ")
        if option == 'l':
            if airlines:
                for al in airlines:
                    airline.show_airline(al)
                    if input('--more-- (q to break)') == 'q':
                        break
            else:
                print("No airlines in memory.\n")
        elif option == 'p':
            if airports:
                for ap in airports:
                    airport.show_airport(ap)
                    if input('--more-- (q to break)') == 'q':
                        break
            else:
                print("No airports in memory.\n")
        elif option == 'f':
            while True:
                print("Searching options (you can combine them):\n")
                print("(l) provide airline name")
                print("(p) provide departure and/or arrival airports")
                print("(t) provide departure and/or arrival times")
                print("(q) return to view menu")
                option = input("Choose parameter to search from: ")
                if 'q' in option:
                    break
                if 'l' in option:
                    al = input("Airline name: ")
                else:
                    al = ""
                if 'p' in option:
                    dep = input("Departure airport: ")
                    arr = input("Arrival airport: ")
                else:
                    dep = ""
                    arr = ""
                if 't' in option:
                    time_dep = input("Departure time: ")
                    time_arr = input("Arrival time: ")
                else:
                    time_dep = ""
                    time_arr = ""
                if al:
                    results = {fl: line.name for line in airlines for fl in line.operations if line.name == al}
                    if not results:
                        print("No airline stored with the name", al)
                        continue
                else:
                    results = {fl: line.name for line in airlines for fl in line.operations}
                if dep:
                    results = {fl: results[fl] for fl in results if fl.dep == dep}
                if arr:
                    results = {fl: results[fl] for fl in results if fl.arr == arr}
                if time_dep:
                    results = {fl: results[fl] for fl in results if fl.time_dep == time_dep}
                if time_arr:
                    results = {fl: results[fl] for fl in results if fl.time_arr == time_arr}
                print(len(results), "results found.")
                lines = {name: [fl for fl in results if results[fl] == name] for name in set(results.values())}
                for line in lines:
                    if input(f"From {line} (enter to show, q to break):") == 'q':
                        break
                    for fl in lines[line]:
                        flight.show_flight(fl)
                    print()
                print()
                


        elif option == 'q':
            break

    

def print_options():
    print('Users menu OPTIONS:\n')
    print('\t--initialize --')
    print('(i) read all data from the input files into the necessary main variables\n')
    print('\t--modification options--')
    print('(a) assign flights to the airline aircraft')
    print('(c) calculate current operational cost related to airports services') 
    print('(d) enter a delay and check assignments\n')
    print('\t--output options--')
    print('(s) show airline information in the screen and the cost of the day operations') 
    print('(k) write KML files of airports, flights and assignments')
    print('(p) plot the flights and the assignments of the airline')
    print('(v) view information about some object')
    print('(w) write current airline assignment into a file\n')
    print('\t--end option--')
    print('(e) end program\n')
    return input('Please, select an option entering one of the letters: ')

# Every option is mapped to a function
OPTIONS = {
    'i': initialize_data,
    'a': assign_flights,
    'c': None,
    'd': None,
    's': None,
    'k': kml_menu,
    'p': plot_menu,
    'v': view_information,
    'w': None
}

airlines = []
airports = []

# Main loop
while True:
    option = print_options()
    if option in OPTIONS:
        if OPTIONS[option]:
            OPTIONS[option]()
        else:
            # If not yet implemented, we show a message
            input('Not yet implemented. :)\n')
    elif option == 'e':
        break
    else:
        input('Invalid option\n')