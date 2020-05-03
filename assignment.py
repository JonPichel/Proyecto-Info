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
    
def plot_assignment(assig):
    # Plot every flight
    for f in assig.flights:
        plt.barh(1, flight.flight_duration(f), height=1.6, left=f.time_dep, color='orange')
    
    # Plot customization
    x_ticks = [60 * i for i in range(0, 24, 3)]
    x_labels = list(map(flight.format_time, x_ticks))
    y_ticks = [1]
    y_labels = [assig.aircraft.callsign]
    plt.xticks(x_ticks, x_labels)
    plt.yticks(y_ticks, y_labels)
    plt.xlim(0, 60*24)
    plt.ylim(0, 2)

    plt.show()