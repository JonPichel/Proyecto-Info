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
