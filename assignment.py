import matplotlib.pyplot as plt

import flight, aircraft

class Assignment:
    """ Assignment ()
    ===================================================
    Defines class Assignment
    Attributes are:
    aircraft: Aircraft, an Aircraft object to which flights are assigned
    flights: list, the list of flights assigned to the aircraft
    """
    def __init__(self):
        self.aircraft = None
        self.flights = []
    
def plot_assignment(assig, show=True, title=None):
    """ Function plot_assignment (assig: Assignment, show: bool)
    =================================================
    Plots the flights of an Assignment
    assig: Assignment, an Assigment object
    show: bool, flag to control whether to show the plot or not. True by default.
    Created by Jonathan Pichel on April 4rd 2020
    """
    # Plot every flight
    for f in assig.flights:
        plt.barh(assig.aircraft.callsign, flight.flight_duration(f), left=f.time_dep, color='lightblue')
    
    # Plot customization
    # Set the ticks and give them labels
    x_ticks = [60 * i for i in range(0, 24)]         # Only set ticks every three hours
    x_labels = list(map(flight.format_time, x_ticks))   # List of strings, formatted with flight.format_time()
    plt.xticks(x_ticks, x_labels)
    plt.tick_params(which='major', axis='x', rotation=45, labelsize='x-small')
    plt.grid(which='major', axis='x', color='gray', linestyle='--', linewidth=0.5)
    plt.xlim(0, 60 * 24)

    # Show the plot if asked to
    if show:
        plt.show()
    if title:
        plt.title(title)

def plot_assignments(vector_assig, title=None):
    """Function plot_assignments (vector_assig: list of Assignments)
    ===================================================
    Plots a list of assignments
    vector_assig: list, list of Assignments to be plotted
    Created by Adrià Vaquer on May 5th 2020
    Tested by Raúl Criado on May 6th 2020
    """
    for assig in vector_assig:
        # We use plot_assignment with show set as False.
        plot_assignment(assig, show=False, title=title)
    
    # We show the plot once all of them are plotted.
    plt.show()

def assign_aircraft(assig, ac):
    """Function assign_aircraft (assig: Assignment, ac: Aircraft): bool
    ===================================================
    Assigns an aicraft to an assignment
    assig: Assignment, the assignment which aircraft shall be assigned
    ac: Aircraft, the aircraft that shall be assigned to the assignment
    Created by Adrià Vaquer on May 5th 2020
    """
    try:
        if assig.aircraft == None:
            if assig.flights == []:
                assig.aircraft = ac
                return True
            else:
                print("There is a flight already assigned.")
                return False
        else:
                print("There is an aircraft already assigned.")
                return False
    except AttributeError:
        print("Wrong Parameters, please provide an Assignment and an Aircraft")
        return False

def assign_flight(assig, f):
    """ Function assign_flight (assig: Assignment, f: flight): bool
    =================================================
    Checks if a flight is compatible with the aircraft and the flights of an assignment.
    If it is, adds the flight to the assigment and returns True. If not, it returns False.
    assig: Assignment, an Assigment object
    f: Flight, a Flight object
    Return: bool, True if it was possible to add the flight, False otherwise
    Created by Jonathan Pichel on April 5rd 2020
    """
    time_dep = f.time_dep
    # If it is the first flight, compare it with the last flight
    # Especial case, Check if the list is empty first
    if assig.flights:
        prev = flight.sort_flights(assig.flights)[-1].arr
        for fl in flight.sort_flights(assig.flights):
            if fl.time_dep > time_dep:
                break
            prev = fl.arr
        # Especial case, If it didn't break the loop, then our flight will be the last of the day
        else:
            if flight.sort_flights(assig.flights)[0].dep != f.arr:
                return False
    else:
        prev = f.dep

    if flight.fits_flight_in_aircraft(f, assig.aircraft):
        if not flight.check_overlap_list(f, assig.flights):
            if prev == f.dep:
                print(prev, f.dep)
                assig.flights.append(f)
                return True
    return False

def show_assignment(assig):
    """ Function show_assignment (assig: Assignment)
    =================================================
    Prints in the screen the data of the assignment assig
    assig: Assignment, an Assignment object
    Created by Pol Roca on April 6th 2020
    Tested by Adrià Vaquer on April 8th 2020
    """
    try:
        print("The aircraft in this assignment is: ", end='')
        aircraft.show_aircraft(assig.aircraft)
        print("The flights in this assignment are:")
        for flights in assig.flights:
            print('\t', end='')
            flight.show_flight(flights)

    except AttributeError:
        print("Wrong parameters, introduce a valid assignment")
