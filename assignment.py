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
    
def plot_assignment(assig, show=True):
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
    x_ticks = [60 * i for i in range(0, 24, 3)]         # Only set ticks every three hours
    x_labels = list(map(flight.format_time, x_ticks))   # List of strings, formatted with flight.format_time()
    plt.xticks(x_ticks, x_labels)
    plt.xlim(0, 60 * 24)

    # Show the plot if asked to
    if show:
        plt.show()

def plot_assignments(vector_assig):
    """Function plot_assignments (vector_assig: list of Assignments)
    ===================================================
    Plots a list of assignments
    vector_assig: list, list of Assignments to be plotted
    Created by Adrià Vaquer on May 5th 2020
    Tested by Raúl Criado on May 6th 2020
    """
    for assig in vector_assig:
        # We use plot_assignment with show set as False.
        plot_assignment(assig, show=False)
    
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
    if type(assig) == Assignment and type(ac) == aircraft.Aircraft:
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
    else:
        print("Wrong parameters, please provide an Assignment and an Aircraft")
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
    if flight.fits_flight_in_aircraft(f, assig.aircraft) and not flight.check_overlap_list(f, assig.flights):
        assig.flights.append(f)
        return True
    return False
