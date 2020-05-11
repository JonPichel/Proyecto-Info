class Airport:

    def __init__(self):
        self.code = ""
        self.name = ""
        self.location = ""
        self.fees = 0
        self.free_hours = 0
        self.cost_per_hour = 0

def set_ap_info(ap, s1, s2, s3):
    """Function set_ap_info (ap: Airport, s1: str, s2: str, s3:str):
    ===================================================
    Given and airport and three strings containing the ICAO code (s1), the name (s2),
    and the location (s3) of the airport, it updates that airport information
    ap: Airport, airport to be updated
    s1: str, ICAO code of the airport
    s2: str, official name of the airport
    s3: str, coordinates of the airport
    """
    try:
        ap.code = s1
        ap.name = s2
        ap.location = s3
            
    except AttributeError:
        print("Wrong parameters. Provide an Airport object.")
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
        print("Wrong parameters. Provide an Airport object.")
        return False

def read_airports(f):
    """Function read_airports (f: str): list
    ===================================================
    Reads from a file that contains the information about some airports, and creates them
    f: str, name of the file where data is stored
    Returns: list containing the airports that were created
    Created by Jonathan Pichel on May 11th 2020
    """
    # We iterate through all the lines of the file
    airports = []
    # We enumerate the iteration to be able to communicate errors to the user
    for i, line in enumerate(open(f, 'r')):
        # We don't process the header, in case there is one
        if not line.startswith('AIRP'):
            words = line.split()
            try:
                code = words[0]
                location = words[1]
                name = " ".join(words[2:])
            except IndexError:
                print(f"Wrong format at line {i + 1}.")
            # If there was no errors, add the airport
            else:
                a = Airport()
                set_ap_info(a, code, name, location)
                airports.append(a)

    return airports

def show_airport(ap):
    """ Function show_airport (ap: Airport)
    ==================================================
    Prints on the screen the information about an airport
    ap: Airport, the Airport which data will be printed
    Created by Jonathan Pichel on April 11th 2020
    """
    try:
        code = ap.code
        name = ap.name
        location = ap.location
        fees = ap.fees
        free_hours = ap.free_hours
        cost_per_hour = ap.cost_per_hour
    except AttributeError:
        print("Wrong parameters. Provide an Airport object.")
        return
   	
    # Check if some information is missing
    if not code:
        code = 'UNKNOWN ICAO CODE'
    if not name:
        name = 'UNKNOWN NAME'
    if location:
        location = f"{location.split(',')[0]}º N, {location.split(',')[1]}º W"
    else:
        location = 'UNKNOWN LOCATION'
    
    # If the name contains Airport, we don't add that information
    if "Airport" in name:
        print(f"Information about {name}:")
    else:
        print(f"Information about {name} Airport:")
    print(f"\tICAO code: {code}")
    print(f"\tCoordinates: {location}")
    print(f"\tLanding fees: {fees}")
    print(f"\tFree parking hours: {free_hours}")
    print(f"\tAditional cost per hour: {cost_per_hour}")


if __name__ == '__main__':
    for ap in read_airports('error.txt'):
        show_airport(ap)
