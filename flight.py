import matplotlib.pyplot as plt

class Flight:
    """ Flight ()
    ===================================================
    Defines class Flight
    Attributes are:
    dep: string, departure airport of the flight
    arr: string, arrival airport of the flight
    time_dep: integer, the time of departure (number of minutes from midnight)
    time_arr: integer, the time of arrival (number of minutes from midnight)
    passengers: integer, number of occupied seats of the flight
    """
    def __init__(self):
        self.dep = ""
        self.arr = ""
        self.time_dep = 0
        self.time_arr = 0
        self.passengers = 0

def format_time(t, colon=True):
    """ Function format_time (t: int): str
    ==================================================
    t: integer, the number of minutes from midnight
    colon: bool, if False it will use the format HHMM instead
    Return: str, time in HH:MM format
    Created by Jonathan Pichel and Raúl Criado on April 18th 2020
    Tested by Raúl Criado and Jonathan Pichel on April 19th 2020
    """
    try:
        # If the input is not of the correct type
        if type(t) != float and type(t) != int:
            return "WRONG TIME"
    
        hours = int(t // 60)
        mins = int(t % 60)
    
        # We use string formatting to avoid unnecessary code
        if colon:
            return f"{hours:02}:{mins:02}"
        else:
            return f"{hours:02}{mins:02}"
    except AttributeError:
        print(" [ERROR] (format_time) Wrong Parameters, provide an integer")
        return False
    
def convert_time(hhmm):
    """Function convert_time (hhmm: str)
    ===================================================
    Given a string with a time in HHMM format, it converts it to our minutes from midnight format
    hhmm: str, time in HHMM format
    Returns: the time in number of minutes since midnight
    Created by Jonathan Pichel on May 11th 2020
    """
    try:
        # We use lstrip to remove the starting zeros in case
        # there is one, to avoid an invalid literal error
        hours = int(hhmm[:2].lstrip('0')) if hhmm[:2].lstrip('0') else 0
        mins = int(hhmm[2:].lstrip('0')) if hhmm[2:].lstrip('0') else 0
    except (ValueError, IndexError) as format_error:
        # This will be printed if there is an IndexError too
        print(f" [ERROR] (convert_time) Wrong data format: {hhmm}. Provide a hour in HHMM format.")
        return

    # Return the number of minutes
    return hours * 60 + mins

def show_flight(f):
    """ Function show_flight(f: Flight)
    ==================================================
    Prints on the screen the data of a flight
    f: Flight, the flight data will be printed
    Created by Raul Criado on April 18th 2020
    Tested by Jonathan Pichel on April 18th 2020
    """
    try:
        time_dep = format_time(f.time_dep)
        time_arr = format_time(f.time_arr)
        dep = f.dep
        arr = f.arr
        passengers = f.passengers
    except AttributeError:
        print(" [ERROR] (show_flight) Wrong parameters. Provide a Flight object.")
        return
   	
    # Check if some information is missing
    if not dep:
        dep = 'UNKNOWN LOCATION'
    if not arr:
        arr = 'UNKNOWN LOCATION'
    
    print(time_dep, dep, 'to', time_arr, arr, 'with', passengers, 'passengers')

def fits_flight_in_aircraft(f, a):
    """ Function fits_flight_in_aircraft (f: Flight, a: Aircraft): bool
    ==================================================
    Test if the passengers of a flight fit inside an aircraft
    f: Flight, it will see if it fits on the plane
    a: Aircraft, we will compare its number of seats
    Return: bool, True if the plane has enough seats; False otherwise
    Created by Jonathan Pichel on April 18th 2020
    Tested by Pol Roca on April 19th 2020
    """
    try:
        if f.passengers <= a.seats:
            return True
        else:
            return False
    except AttributeError:
        print(" [ERROR] (fits_flight_in_aircraft) Wrong parameters. Provide a Flight and an Aircraft objects.")
        return
    except TypeError:
        print(" [ERROR] (fits_flight_in_aircraft) Aircraft seats and flight passengers must be integers.")
        return

def flight_duration(f):
    """ Function flight_duration (f: Flight): int
    =================================================
    Calculates the duration of the flight
    f: Flight, it will calculate its duration
    Return: int, the duration of the flight in minutes
    Created by Pol Roca on April 21th 2020
    Tested by Adrià Vaquer on April 21st 2020
    """
    try:
        # We define a variable called duration that will record the difference between the arrival and departure times
        if f.time_arr >= f.time_dep:
            duration = f.time_arr - f.time_dep
        else:
            duration = f.time_arr + (24 * 60 - f.time_dep)
    except AttributeError:
        print(" [ERROR] (flight_duration) Wrong parameters. Provide a Flight object.")
        return
    
    return duration

def delay_flight(f, d):
    """ Function delay_flight (f: Flight, d: int): bool
    =================================================
    Adds to the departure and arrival times the delay minutes given by parameter d
    f: Flight, to get the delay added to the departure and arrival times
    d: int, the delay in minutes
    Return: bool, False if any of the resulting times is not within the number of
    minutes of 1 day, True if the delay can be added correctly
    Created by Pol Roca on April 21th 2020
    Tested by Adrià Vaquer on April 21st 2020
    """
    try:
        # Compares the resulting times with the number of minutes of 1 day
        if (0 < f.time_dep + d < 1440) and (0 < f.time_arr + d < 1440):
            # Adds the delay to the departure and arrival times
            f.time_dep = f.time_dep + d
            f.time_arr = f.time_arr + d
            return True
        else:
            return False
    except AttributeError:
        print(" [ERROR] (delay_flight) Wrong parameters. Please provide a Flight object and an integer.")
        return False
    
def check_overlap(f1, f2, interval=60):
    """ Function check_overlap (f1: Flight, f2: Flight): bool
    =================================================
    Checks if the time ranges of two flights overlap
    f1: Flight, first flight to check
    f2: Flight, second flight to check
    interval: int, minimum number of minutes that must exist between the flights
    Return: bool, False if they don't overlap, True if they do
    Created by Jonathan Pichel on April 5rd 2020
    Tested by Pol Roca on May 9th 2020
    """
    try:
        # Normal case: none of the aircrafts crosses through midnight
        if f1.time_dep <= f1.time_arr and f2.time_dep <= f2.time_arr:
            if ((f1.time_dep <= f2.time_dep - interval and f1.time_arr <= f2.time_dep - interval) or
                (f1.time_dep >= f2.time_arr + interval and f1.time_arr >= f2.time_arr + interval)):
                return False
            else:
                return True
        # Especial cases: any of the aircrafts crosses through midnight
        # If its the first one who crosses
        elif f1.time_dep > f1.time_arr:
            if f2.time_arr <= f1.time_dep - 60 and f2.time_dep >= f1.time_arr + 60:
                return False
            else:
                return True
        # If its the second one who crosses
        elif f1.time_dep <= f1.time_arr and f2.time_dep > f2.time_arr:
            if f1.time_arr <= f2.time_dep - 60:
                return False
            else:
                return True
        # If both cross, they of course collide
        else:
            return True

    except AttributeError:
        print(" [ERROR] (check_overlap) Wrong Parameters, please provide a Flight")
        return False
    
def check_overlap_list(f, vector_flight, interval=60):
    """ Function check_overlap_list (f: Flight, vector_flight: list): bool
    =================================================
    Checks if one flight overlaps with any other one from a list of flights
    f: Flight, a Flight object
    vector_flight: list, a list of Flight objects
    interval: int, minimum number of minutes that must exist between the flights
    Return: bool, False if they don't overlap, True if they do
    Created by Jonathan Pichel on May 5rd 2020
    Tested by Pol Roca on May 9th 2020
    """
    try:
        for flight in vector_flight:
            if check_overlap(f, flight, interval=interval):
                return True
        return False
    except AttributeError:
        print(" [ERROR] (check_overlap_list) Wrong Parameters, please provide a Flight")
        return False
    
def check_inner_overlap(vector_flight, interval=60):
    """ Function check_inner_overlap (vector_flight: list): bool
    =================================================
    Checks if there exists any overlap between the flights of a list
    vector_flight: list, a list of Flight objects
    interval: int, minimum number of minutes that must exist between the flights
    Return: bool, True if there's any overlap, False otherwise
    Created by Jonathan Pichel on May 5rd 2020
    Tested by Pol Roca on May 9th 2020
    """
    try:
        for i in range(len(vector_flight)):
            if check_overlap_list(vector_flight[i], vector_flight[i+1:], interval=interval):
                return True
        return False
    except AttributeError:
        print(" [ERROR] (check_inner_overlap) Wrong Parameters, please provide a Flight")
        return False
    
def plot_flight(f, show=True, title=None):
    """ Function plot_flight (f: Flight, show: bool)
    =================================================
    Plots a flight
    f: Flight, a Flight object
    show: bool, flag to control whether to show the plot or not. True by default.
    title: str, if provided it will set the title of the plot
    Created by Pol Roca on May 6th 2020
    Tested by Adrià Vaquer on May 9th 2020
    """
    try:
        # Plot the flight
        if f.time_dep <= f.time_arr:
            # Normal case
            plt.barh(f"{f.dep}\n{f.arr}", flight_duration(f), left=f.time_dep, color='lightblue')
        else:
            # Maybe it crosses through midnight
            plt.barh(f"{f.dep}\n{f.arr}", 24 * 60 - f.time_dep, left=f.time_dep, color='lightblue')
            plt.barh(f"{f.dep}\n{f.arr}", f.time_arr, left=0, color='lightblue')
    
        # Plot customization
        # Set the ticks and give them labels
        x_ticks = [60 * i for i in range(0, 24)]
        x_labels = list(map(format_time, x_ticks))   # List of strings, formatted with flight.format_time()
        plt.xticks(x_ticks, x_labels)
        plt.tick_params(which='major', axis='x', rotation=45, labelsize='x-small')
        plt.grid(which='major', axis='x', color='gray', linestyle='--', linewidth=0.5)
        plt.xlim(0, 60 * 24)

        if title:
            plt.title(title)
        # Show the plot if asked to
        if show:
            plt.show()
    except AttributeError:
        print(" [ERROR] (plot_flight)Wrong Parameters, please provide a Flight")
        return

def plot_flights(vf, title=None):
    """Function plot_flights (vf: list of Flights)
    ===================================================
    Plots a list of flights
    vf: list, list of Flights to be plotted
    title: str, if provided it will set the title of the plot
    Created by Jonathan Pichel on May 5th 2020
    Tested by Pol Roca on May 9th 2020
    """
    try:
        for flight in sort_flights(vf):
            # We use plot_assignment with show set as False.
            plot_flight(flight, show=False, title=title)
        
        # We show the plot once all of them are plotted.
        plt.show()
    except AttributeError:
        print("Wrong Parameters, please provide a Flight list")
        return False

def sort_flights(vf):
    """Function sort_flights (vf: list of Flights)
    ===================================================
    Given a list of flights, it sorts the flights by time of departure and returns the sorted list
    vf: list, list of Flights to be sorted
    Returns: list, a list of flights ordered by time_dep
    Created by Jonathan Pichel on May 9th 2020
    Tested by Adriá Vaquer on May 9th 2020
    """
    try:
        # I use the sorted builtin to sort the flights by time of departure
        return sorted(vf, key=lambda f: f.time_dep)
    except AttributeError:
        print("Wrong Parameters, please provide a list of Flights")
        return
    
def check_airports(vf):
    """Function check_airports (vf: list of Flights)
    ===================================================
    Given a list of flights assigned to an aircraft, it checks that their airports' order makes sense.
    vf: list, list of Flights to be sorted
    Returns: False if it doesn't follow a logical order, True if it does
    Created by Jonathan Pichel on May 9th 2020
    Tested by Raúl Criado on May 9th 2020
    """
    try:
        # Iterate the sorted list of flights
        for i, f in enumerate(sort_flights(vf)):
            if not i == 0:
                # If the flights departure airport doesn't match the arrival airport of the previous flight
                if prev != f.dep:
                    # Return False
                    return False
            prev = f.arr
        if sort_flights(vf)[-1].arr != sort_flights(vf)[0].dep:
            return False
        # Else, return True
        return True
    except AttributeError:
        print("Wrong Parameters, please provide a list of Flights")
        return

def read_flights(f):
    """ Function read_flights (f: string)
    =================================================
    Read the flights of a text file
    f: string, the name of the text file
    Return: vector of flights, a vector with the flights of the text file
    Created by Adrià Vaquer on 11th May 2020
    """
    flights = []
    try:
        for i, line in enumerate(open(f, 'r')):
            if not line.startswith("TIMD TIMA"):
                fl = Flight()
                try:
                    data = line.split()
                    fl.time_dep = convert_time(data[0])
                    fl.time_arr = convert_time(data[1])
                    fl.dep = data[2]
                    fl.arr = data[3]
                    fl.passengers = int(data[4])
                except KeyError:
                    pass
                except ValueError:
                    print("[read_flights] Wrong format at line", i)
                else:
                    flights.append(fl)
        return flights
    except FileNotFoundError:
        print("[read_flights] File couldn't be found.")
        return
    except PermissionError:
        print("[read_flights] You don't have permissions over that file.")
        return

def map_flights(vf,va):
    """ Function map_flights (vf: vector of flights, va: vector of airports)
    ==================================================
    Creates a kml file that show the route of flights through the airports from the vector introduced
    vf: vector of flights
    va: vector of airports extracted from the file
    Created by Raúl Criado on May 19th 2020
    """
    try:
        with open("Operations.kml", "w") as f:
            f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
            f.write("<Document>\n")
            f.write(" <Placemark>\n")
            f.write("   <name>Route</name>\n")
            f.wrtie("   <LineString>")
            f.write("    <extrude>1</extrude>\n")
            f.write("     <coordinates>\n")
            m = 0
            for i in vf:
                for v in va:
                    if i.dep == v.code:    
                        f.write("       "+v.location+"\n")
                    else:
                        m+=1                                
            f.write("     </coordinates>\n")
            f.write("  </LineString>\n")
            f.write(" </Placemark>\n")
            f.write("</Document>\n")
            f.write("</kml>\n")

        if m == len(vf):
            print('Airport cannot be found')
            return False

    except AttributeError:
        print("Wrong parameters. Provide an Airport object.")
        return False

def map_flights(vf,va):
    """ Function map_flights (vf: vector of flights, va: vector of airports)
    ==================================================
    Creates a kml file that show the route of flights through the airports from the vector introduced
    vf: vector of flights
    va: vector of airports extracted from the file
    Created by Raúl Criado on May 19th 2020
    """
    try:
        with open("Operations.kml", "w") as f:
            f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
            f.write("<Document>\n")
            f.write(" <Placemark>\n")
            f.write("   <name>Route</name>\n")
            f.wrtie("   <LineString>")
            f.write("    <extrude>1</extrude>\n")
            f.write("     <coordinates>\n")
            m = 0
            for i in vf:
                for v in va:
                    if vf[i].dep == va[v].code:    
                        f.write("       "+va[v].location+"\n")
                    else:
                        m+=1                                
            f.write("     </coordinates>\n")
            f.write("  </LineString>\n")
            f.write(" </Placemark>\n")
            f.write("</Document>\n")
            f.write("</kml>\n")

        if m == len(vf):
            print('Airport cannot be found')
            return False

    except AttributeError:
        print("Wrong parameters. Provide an Airport object.")
        return False
