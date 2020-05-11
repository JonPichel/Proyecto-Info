class Airport:

    def __init__(self):
        self.code = ""
        self.name = ""
        self.location = ""
        self.fees = 0
        self.free_hours = 0
        self.cost_per_hour = 0


def set_ap_info(ap, s1, s2, s3):
    """ Function set_ap_info(ap, s1, s2, s3)
    ==================================================
    Updates the information of an airport.
    ap: object of class Airport
    s1: string of the ICAO code of the airport
    s2: string of the official name of the airport
    s3: string of the geographical coordinates of the airport
    Created by Raúl Criado on May 11th 2020
    """
    try:
        ap.code = s1
        ap.name = s2
        ap.location = s3
            
    except AttributeError:
        print("Wrong parameters. Provide an Airline object.")
        return False


def set_costs(ap, c1, c2, c3):
    """ Function set_costs(ap, c1, c2, c3)
    ==================================================
    Updates the information of an airport related to fees.
    ap: object of class Airport
    c1: number of the runway cost
    c2: number of the free parking hours
    c3: number of the additional parking fees per hour
    Created by Raúl Criado on May 11th 2020
    """
    try:
        ap.fees = c1
        ap.free_hours = c2
        ap.cost_per_hour = c3
            
    except AttributeError:
        print("Wrong parameters. Provide an Airline object.")
        return False
