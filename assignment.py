import matplotlib.pyplot as plt

import flight

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
    # Plot every flight
    for f in assig.flights:
        plt.barh(assig.aircraft.callsign, flight.flight_duration(f), left=f.time_dep, color='lightblue')
    
    # Plot customization
    x_ticks = [60 * i for i in range(0, 24, 3)]
    x_labels = list(map(flight.format_time, x_ticks))
    plt.xticks(x_ticks, x_labels)
    plt.xlim(0, 60*24)

    if show:
        plt.show()

def plot_assignments(vector_assig):
    for assig in vector_assig:
        plot_assignment(assig, show=False)
    
    plt.show()

def assign_aircraft(assig,ac):
    """Function assign_aircraft (assig: Assignment, ac: Aircraft): Boolean
    ===================================================
    Assigns an aicraft to an assignment
    assig: Assignment, the assignment which aircraft shall be assigned
    ac: Aircraft, the aircraft that shall be assigned to the assignment
    Created by Adrià Vaquer on May 5th 2020
    """
    if type(assig) == Assignment and type(ac) == aircraft.Aircraft :
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
