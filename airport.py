class Airport:

    def __init__(self):
        self.code = ""
        self.name = ""
        self.location = ""
        self.fees = 0
        self.free_hours = 0
        self.cost_per_hour = 0

def set_ap_info(ap, s1, s2, s3):
    """Function read_airports (ap: Airport, s1: str, s2: str, s3:str):
    ===================================================
    Given and airport and three strings containing the ICAO code (s1), the name (s2),
    and the location (s3) of the airport, it updates that airport information
    ap: Airport, airport to be updated
    s1: str, ICAO code of the airport
    s2: str, official name of the airport
    s3: str, coordinates of the airport
    La puso Jonathan aquí para poder llamar mi función mientras no está hecha
    """
    pass

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
                name = words[2:]
            except IndexError:
                print(f"Wrong format at line {i + 1}.")
            # If there was no errors, add the airport
            else:
                ap = Airport()
                set_ap_info(ap, code, name, location)
                airports.append(ap)

    return airports

if __name__ == '__main__':
    read_airports('error.txt')