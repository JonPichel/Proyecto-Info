import airline, aircraft, airport, assignment, flight

def prompt(*vargs):
    """ Function prompt(*vargs: list): string
    Asks the user for information, it will normalize the prompt style of the menu
    vargs: list, list of strings to print in screen with input
    Return: str, the user input to later process
    Created by Jonathan Pichel on May 25th 2020
    """
    msg = " [P]"
    for arg in vargs:
        msg += f" {arg}"
    msg += ": "
    return input(msg)

def success(*vargs, disrupt=True):
    """ Function success(*vargs: list, disrupt: bool):
    Prints a success message
    vargs: list, list of arguments that will form the message to print in screen
    disrupt: bool, if set to True it will use input(), otherwise it will use print()
    Created by Jonathan Pichel on May 25th 2020
    """
    msg = " [S]"
    for arg in vargs:
        msg += f" {arg}"
    if disrupt:
        input(msg)
    else:
        print(msg)

def failure(*vargs, disrupt=True):
    """ Function failure(*vargs: list, disrupt: bool):
    Prints a failure message
    vargs: list, list of arguments that will form the message to print in screen
    disrupt: bool, if set to True it will use input(), otherwise it will use print()
    Created by Jonathan Pichel on May 25th 2020
    """
    msg = " [F]"
    for arg in vargs:
        msg += f" {arg}"
    if disrupt:
        input(msg)
    else:
        print(msg)

def verbose(*vargs):
    """ Function verbose(*vargs: list):
    Prints non critical messages on screen
    vargs: list, list of strings to print in screen
    Created by Jonathan Pichel on May 25th 2020
    """
    print(" [*]", *vargs)

def wrong_option():
    """ Function wrong_option():
    Prints invalid option error on screen
    Created by Jonathan Pichel on May 25th 2020
    """
    input("Invalid option")

def search_airline(name):
    """ Function search_airline(name: string):
    Given a name, it returns all the airlines with that name in the airlines list
    name: string, name of the airline
    Return: list, list of Airlines with that name
    Created by Jonathan Pichel on May 26th 2020
    """
    return [a for a in airlines if a.name == name]

def show_airlines():
    """ Function search_airline():
    Shows available airlines in memory
    Created by Jonathan Pichel on May 26th 2020
    """
    success("Available airlines:", disrupt=False)
    for al in airlines:
        print(f" - {al.name}")

# DONE
def show_help(screen):
    """ Function show_help(screen: string):
    screen: string, name of the menu
    Created by Jonathan Pichel on May 25th 2020
    """
    if screen == 'main':
        print("Users menu OPTIONS:\n")
        print("\t--initialize --")
        print("(i) read all data from the input files into the necessary main variables\n")
        print("\t--modification options--")
        print("(a) assign flights to the airline aircraft")
        print("(c) calculate current operational cost related to airports services") 
        print("(d) enter a delay and check assignments\n")
        print("\t--output options--")
        print("(s) show airline information in the screen and the cost of the day operations") 
        print("(k) write KML files of airports, flights and assignments")
        print("(p) plot the flights and the assignments of the airline")
        print("(v) view information about some object")
        print("(w) write current airline assignment into a file\n")
        print("\t--end option--")
        print("(e) end program")
        print("(h) show this help screen")
    if screen == 'read':
        print("Reading options:")
        print("(l) airline")
        print("(p) airports")
        print("(c) airports costs")
        print("\nOther options:")
        print("(h) show this help screen")
        print("(q) quit to main menu")
    elif screen == 'assign':
        print("Assign flights to the aircrafts:")
        print("\t(1) choose an airline")
        print("\nOther options:")
        print("(l) show a list of the available airlines")
        print("(h) show this help screen")
        print("(q) return to main menu")
    elif screen == 'costs':
        print("Calculate operational costs of an airline:")
        print("\t(1) choose an airline")
        print("\nOther options:")
        print("(l) show a list of the available airlines")
        print("(h) show this help screen")
        print("(q) return to main menu")
    elif screen == 'delay':
        print("Delay a flight:")
        print("\t(1) Choose the flight")
        print("\t(2) Choose a delay")
        print("\nPrompt options:")
        print("(y) delay a flight")
        print("(n) return to main menu")
        print("(h) show this help screen")
        print("(q) return to main menu")
    elif screen == 'kml':
        print("KML options:")
        print("(p) write kml of airports")
        print("(f) write kml of flights")
        print("(a) write kml of assignments")
        print("\nOther options:")
        print("(h) show this help screen")
        print("(q) quit to main menu")
    elif screen == 'plot':
        pass
    elif screen == 'show':
        print("Viewing options:")
        print("(l) airlines")
        print("(p) airports")
        print("(f) flight")
        print("\nOther options:")
        print("(h) show this help screen")
        print("(q) quit to main menu")
    elif screen == 'write':
        print("Write day plan for an airline:")
        print("\t(1) choose an airline")
        print("\t(2) choose filename")
        print("\nOther OPTIONS:")
        print("(h) show this help screen")
        print("(q) return to main menu")
    elif screen == 'flights':
        print("Search options:")
        print("(airline) airline name")
        print("(dep) departure airport")
        print("(arr) arrival airport")
        print("(tdep) departure time")
        print("(tarr) arrival time")
        print("\nOther options")
        print("(h) show this help screen")
        print("(s) show current results")
        print("(c) show current set params.")
        print("(q) return to previous screen")
        print("\nTIPS:")
        print(" - If you want to unset a parameter, choose that search option and leave it blank")
        print(" - If you are choosing a flight to delay, press q when the candidates correspond to the flight you want")

# DONE
def read_menu():
    """ Function read_menu():
    Shows the help for each menu
    Menu that provides reading functionalities
    Created by Jonathan Pichel on May 22th 2020
    """
    # Show help the first time
    print()
    show_help('read')
    # Read menu loop
    while True:
        # Ask for an option
        print("\n[Main -> Read Menu]")
        option = prompt("Type of file you want to read from")
        # Initialize airline
        if option == 'l':
            print("\n[Main -> Read Menu -> Airline]")
            filename = prompt("Filename")
            al = airline.read_airline(filename)
            if al:
                # If there is one of more airlines with the same name already stored
                duplicates = search_airline(al.name)
                if duplicates:
                    # We delete them and append the new/actualized one
                    verbose("Removing previous instances of airline", al.name)
                    for a in duplicates:
                        airlines.remove(a)
                airlines.append(al)
                success("Airline correctly initialized.")
            else:
                failure("There was an error reading the file.")
        # Initialize airports
        elif option == 'p':
            print("\n[Main -> Read Menu -> Airports]")
            filename = prompt("Filename")
            new_airports = airport.read_airports(filename)
            if new_airports:
                for ap in new_airports:
                    old_index = airport.search_airport_index(airports, ap.code)
                    if old_index == -1:
                        airports.append(ap)
                        verbose(f"Succesfully added airport: {ap.code}")
                    else:
                        old_ap = airports[old_index]
                        if old_ap.location != ap.location or old_ap.name != ap.name:
                            verbose(f"Updating data on airport: {ap.code}")
                            airports[old_index].location = ap.location
                            airports[old_index].name = ap.name
                success("Airports correctly initialized.")
            else:
                failure("Couln't initialize any airport.")
        # Initialize airports costs
        elif option == 'c':
            print("\n[Main -> Read Menu -> Airport Costs]")
            filename = prompt("Filename")
            # We store the airports data to compare which airports have changed
            old_data = [[ap.fees, ap.free_hours, ap.cost_per_hour] for ap in airports]
            airport.read_airport_costs(airports, filename)
            num = 0
            for i in range(len(airports)):
                if (old_data[i][0] != airports[i].fees or old_data[i][1] != airports[i].free_hours or
                    old_data[i][2] != airports[i].cost_per_hour):
                    verbose(f"Updated the costs for {airports[i].code}.")
                    num += 1
            if num:
                success(f"Updated the costs for {num} airports.")
            else:
                failure("Couldn't update any airport.")
        # Show help screen
        elif option == 'h':
            show_help('read')
        # Break to main menu
        elif option == 'q':
            break
        else:
            wrong_option()

# DONE
def assign_menu():
    """ Function assign_menu():
    Menu that provides assigning functionalities
    Created by Jonathan Pichel on May 22th 2020
    """
    # Show help the first time
    print()
    show_help('assign')
    # Assign loop
    while True:
        print("\n[Main -> Assign]")
        name = prompt("Airline's name")
        if not name:
            continue
        if name == 'l':
            if not airlines:
                failure("No airlines in memory.")
                continue
            show_airlines()
        elif name == 'h':
            show_help('assign')
        elif name == 'q':
            break
        else:
            if not airlines:
                failure("No airlines in memory.")
                continue
            al = search_airline(name)
            if al:
                airlines.remove(al[0])
                airlines.append(airline.assign_operations(al[0]))
                success(f"Operations of {name} assigned.")
            else:
                failure(f"No airline found with name {name}.")

# DONE
def costs_menu():
    """ Function costs_menu():
    Menu for calculating costs
    Created by Jonathan Pichel on May 22th 2020
    """
    # Show help the first time
    print()
    show_help('costs')
    # Costs loop
    while True:
        print("\n[Main -> Assign]")
        name = prompt("Name of the airline")
        if name == 'l':
            show_airlines()
        elif name == 'h':
            show_help('costs')
        elif name == 'q':
            break
        else:
            al = search_airline(name)
            if al:
                if al[0].assignments:
                    # We save the costs inside the object
                    costs = airline.calculate_day_costs(al[0], airports)
                    if costs != -1:
                        if costs == 0:
                            verbose("Total cost of 0. You may have not initialized airport costs.")
                        al[0].costs = costs
                        success(f"Day costs for {name} calculated.")
                    else:
                        failure("An error has occurred. Make sure you initialize airports and airports' costs before trying this.")
                else:
                    failure(f"You have to assign the operations in {name} first!")
            else:
                failure(f"No airline found with name {name}.")
                
# DONE
def delay_menu():
    """ Function delay_menu():
    Menu for delaying flights
    Created by Jonathan Pichel on May 22th 2020
    """
    # Show help the first time
    print()
    show_help('delay')
    # Delay loop
    while True:
        print("\n[Main -> Delay]")
        option = prompt("Do you want to delay a flight?")
        if option == 'y':
            results = search_flights('delay')
            if not results:
                failure("No results.")
                continue
            elif len(results) == 1:
                target = results[0]
            else:
                failure("More than one result.")
                continue
            print("\n[Main -> Delay]")
            try:
                delay = int(prompt("Delay time (in minutes)"))
            except ValueError:
                failure("Enter a number.")
            if flight.delay_flight(target, delay):
                success("Flight successfully delayed.")
            else:
                failure("Couldn't delay the flight.")
        if option == 'n' or option == 'q':
            break

# DONE
def show_menu():
    """ Function show_menu():
    Menu that provides information viewing functionalities
    Created by Jonathan Pichel on May 22th 2020
    """
    # Show help the first time
    print()
    show_help('show')
    # Show loop
    while True:
        print("\n[Main -> Show]")
        option = prompt("What information do you want to display?")
        if option == 'l':
            if airlines:
                name = prompt("Airline's name (\"all\" to show them all)")
                if name == 'all':
                    for al in airlines:
                        airline.show_airline(al)
                        if input('--more-- (q to break)') == 'q':
                            break
                else:
                    al = search_airline(name)
                    if al:
                        airline.show_airline(al[0])
                    else:
                        failure(f"No airline named {name}.")
            else:
                failure("No airlines in memory.")
        elif option == 'p':
            if airports:
                code = prompt('ICAO code ("all" to show them all)')
                if code == 'all':
                    for ap in airports:
                        airport.show_airport(ap)
                        if input('--more-- (q to break)') == 'q':
                            break
                else:
                    al = search_airline(name)
                    if al:
                        airline.show_airline(al[0])
                    else:
                        failure(f"No airline named {name}.")
            else:
                failure("No airports in memory.")
        elif option == 'f':
            search_flights('show')
        elif option == 'q':
            break
        else:
            wrong_option()

# DONE
def search_flights(mode):
    if mode == 'show':
        text = '\n[Main -> Show -> Flight]'
    elif mode == 'delay':
        text = '\n[Main -> Delay -> Search]'
    params = {'airline': None, 'dep': None, 'arr': None, 'tdep': None, 'tarr': None}
    all_flights = {fl: al.name for al in airlines for fl in al.operations}
    results = all_flights.copy()
    # Show help the first time
    print()
    show_help('flights')
    # Searching loop
    while True:
        print(text)
        param = prompt("Search parameter ('s' to show current results)")
        if param == 'airline':
            al = prompt("Airline name")
            if al:
                params['airline'] = al
            else:
                params['airline'] = None
        elif param == 'dep':
            dep = prompt("Departure airport")
            if dep:
                params['dep'] = dep
            else:
                params['dep'] = None
        elif param == 'arr':
            arr = prompt("Arrival airport")
            if arr:
                params['arr'] = arr
            else:
                params['arr'] = None
        elif param == 'tdep':
            tdep = prompt("Time of departure (HHMM format)")
            if tdep:
                params['tdep'] = tdep
            else:
                params['tdep'] = None
        elif param == 'tarr':
            tarr = prompt("Time of arrival (HHMM format)")
            if tarr:
                params['tarr'] = tarr
            else:
                params['tarr'] = None
        elif param == 's':
            success(f"{len(results)} candidates")
            alines = {name: [fl for fl in results if results[fl] == name] for name in set(results.values())}
            for al in alines:
                if input(f" {len(alines[al])} from {al} (enter to show, q to break):") == 'q':
                    break
                for fl in alines[al]:
                    print("\t", end='')
                    flight.show_flight(fl)
        elif param == 'c':
            for p in params:
                print(f"{p} -> {params[p]}")
        elif param == 'h':
            show_help('flights')
        elif param == 'q':
            candidate = [fl for fl in results]
            return candidate
        results = all_flights.copy()
        if params['airline']:
            results = {fl: results[fl] for fl in results if results[fl] == params['airline']}
        if params['dep']:
            results = {fl: results[fl] for fl in results if fl.dep == params['dep']}
        if params['arr']:
            results = {fl: results[fl] for fl in results if fl.arr == params['arr']}
        if params['tdep']:
            results = {fl: results[fl] for fl in results if fl.time_dep == flight.convert_time(params['tdep'])}
        if params['tarr']:
            results = {fl: results[fl] for fl in results if fl.time_arr == flight.convert_time(params['tarr'])}

# TODO
def kml_menu():
    """ Function kml_menu():
    Menu that provides kml saving functionalities
    Created by Jonathan Pichel on May 22th 2020
    """
    # Show help the first time
    print()
    show_help('kml')
    # KML loop
    while True:
        print("\n[Main -> KML]")
        option = prompt("What do you want to save in kml?")
        if option == 'p':
            if airport.map_airports(airports):
                success(f"Map of the airports written to Airports.kml")
            else:
                failure(f"Couldn't map the airports.")
        elif option == 'f':
            print("\n[Main -> KML Menu]")
            name = prompt("Name of the airline to map flights")
            if name:
                al = search_airline(name)
                if flight.map_flights(al[0].operations, airports):
                    success(f"Map of the flights on {name} written to Operations.kml")
                else:
                    failure(f"Couldn't map the flights on {name}.")
        elif option == 'a':
            name = prompt("Airline name")
            if name:
                al = search_airline(name)
                if al:
                    callsign = prompt("Aircraft's callsign") 
                    assig = [assig for assig in al[0].assignments if assig.aircraft.callsign == callsign]
                    if assig:
                        if assignment.map_assignment(assig[0], airports):
                            success(f"Map of the flights for {callsign} written to {callsign}.kml")
                        else:
                            failure(f"Couldn't map the flights assigned to {callsign}.")
                    else:
                        failure(f"No aircraft {callsign} for {name}.")
                else:
                    failure(f"No airline named {name}.")
        elif option == 'h':
            show_help('kml')
        elif option == 'q':
            break
        else:
            wrong_option()

# TODO
def plot_menu():
    """ Function plot_menu():
    Menu that provides plotting functionalities
    Created by Jonathan Pichel on May 22th 2020
    """
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

# TODO
def write_menu():
    """ Function write_menu():
    Menu that provides writing functionalities
    Created by Jonathan Pichel on May 22th 2020
    """
    # Show help the first time
    show_help('write')
    # Write menu loop
    while True:
        # Ask for airline's name
        name = input("Name of the airline: ")
        # Show help screen
        if name == 'h':
            show_help('write')
        # Break to main loop
        elif name == 'q':
            break
        else:
            # This list will return the results
            al = [al for al in airlines if al.name == name]
            if al:
                filename = input("File to write to: ")
                if airline.write_day_plan(al[0], filename):
                    input(f"Day plan for {name} saved to {filename}")
                else:
                    input(f"An error has occurred.")
            else:
                input(f"No airline named {name}.")

# Every option of main menu is mapped to a function
OPTIONS = {
    'i': read_menu,
    'a': assign_menu,
    'c': costs_menu,
    'd': delay_menu,
    's': show_menu,
    'k': kml_menu,
    'p': plot_menu,
    'w': write_menu
}

airlines = []
airports = []

# Main loop
show_help('main')
while True:
    print("\n[Main]")
    option = prompt("Please, select an option entering one of the letters")
    if option in OPTIONS:
        if OPTIONS[option]:
            OPTIONS[option]()
        else:
            # TODO: If not yet implemented, we show a message
            wrong_option()
    elif option == 'e':
        print("Goodbye :)")
        break
    elif option == 'h':
        show_help('main')
    else:
        wrong_option()