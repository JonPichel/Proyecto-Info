import airline, aircraft, airport, assignment, flight

def initialize_data():
    while True:
        print("Reading options:\n")
        print("(l) airline")
        print("(p) airports")
        print("(d) airport data")
        print("(q) quit to main menu")

        option = input("What type of file do you want to read from?: ")
        if option == 'l':
            filename = input("Filename to read from: ")
            airlines.append(airline.read_airline(filename))
        elif option == 'p':
            filename = input("Filename to read from: ")
            new_airports = airport.read_airports(filename)
            for ap in new_airports:
                if airport.search_airport_index(airports, ap.code) == -1:
                    print(f"Succesfully added airport: {ap.code}")
                    airports.append(ap)
        elif option == 'd':
            filename = input("Filename to read from: ")
            airport.read_airport_costs(airports, filename)
        elif option == 'q':
            break

def assign_flights():
    name = input("Name of the airline (q to quit to main menu): ")
    if name == 'q':
        return
    al, = (a for a in airlines if a.name == name)
    airline.assign_operations(al)
    print("Operations assigned.")

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
    print("(a) plot airline assignments")
    print("(f) plot airline operations")
    print("(q) quit to main menu")

    option = input("What do you want to plot?: ")
    if option == 'a':
        name = input("Name of the airline: ")
        al, = (a for a in airlines if a.name == name)
        airline.plot_assignments(al, title=f"Assignments of {al.name}")
    elif option == 'f':
        name = input("Name of the airline: ")
        al, = (a for a in airlines if a.name == name)
        airline.plot_flights(al, title=f"Flights of {al.name}")
    elif option == 'q':
        pass


def view_information():
    while True:
        print("Viewing options:\n")
        print("(l) airlines")
        print("(p) airports")
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
    print('(v) view information about some variable')
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
        print('Invalid option\n')