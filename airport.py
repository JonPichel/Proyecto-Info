class Airport:

    def __init__(self):
        self.code = ""
        self.name = ""
        self.location = ""
        self.fees = 0
        self.free_hours = 0
        self.cost_per_hour = 0

def set_ap_info(ap, s1, s2, s3):
    """Function set_ap_info (ap: Airport, s1: str, s2: str, s3:str): bool
    ===================================================
    Given and airport and three strings containing the ICAO code (s1), the name (s2),
    and the location (s3) of the airport, it updates that airport information
    ap: Airport, airport to be updated
    s1: str, ICAO code of the airport
    s2: str, official name of the airport
    s3: str, coordinates of the airport
    Created by Raúl Criado on May 15th 2020
    Tested by Jonathan Pichel on May 20th 2020
    """
    try:
        ap.code = s1
        ap.name = s2
        ap.location = s3
    except AttributeError:
        print(" [ERROR] (set_ap_info) Wrong parameters. Provide an Airport object and data in strings.")
        return

def set_costs(ap, c1, c2, c3):
    """ Function set_costs(ap, c1, c2, c3)
    ==================================================
    Updates the information of an airport related to fees.
    ap: object of class Airport
    c1: number of the runway cost
    c2: number of the free parking hours
    c3: number of the additional parking fees per hour
    Created by Raúl Criado on May 11th 2020
    Tested by Jonathan Pichel on May 20th 2020
    """
    try:
        ap.fees = c1
        ap.free_hours = c2
        ap.cost_per_hour = c3
            
    except AttributeError:
        print(" [ERROR] (set_costs) Wrong parameters. Provide an Airport object and data in strings.")
        return

def read_airports(f):
    """Function read_airports (f: str): list
    ===================================================
    Reads from a file that contains the information about some airports, and creates them
    f: str, name of the file where data is stored
    Returns: list containing the airports that were created
    Created by Jonathan Pichel on May 11th 2020
    """
    try:
        # We iterate through all the lines of the file
        airports = []
        # We enumerate the iteration to be able to communicate errors to the user
        for i, line in enumerate(open(f, 'r')):
            # We don't process the header, in case there is one
            if not line.startswith('AIRP'):
                words = line.split()
                try:
                    if len(words) < 3:
                        raise ValueError
                    code = words[0]
                    if len(code) != 4:
                        raise ValueError
                    location = words[1]
                    if len(location.split(',')) != 2:
                        raise ValueError
                    # Check if coordinates are numbers
                    float(location.split(',')[0])
                    float(location.split(',')[1])
                    name = " ".join(words[2:])
                except (ValueError, IndexError) as format_error:
                    print(f"Wrong format at line {i + 1}.")
                # If there was no errors, add the airport
                else:
                    a = Airport()
                    set_ap_info(a, code, name, location)
                    airports.append(a)
        return airports
    except FileNotFoundError:
        print("File couldn't be found.")
        return
    except PermissionError:
        print("You don't have permissions over that file.")
        return

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


def map_airports(v):
    """ Function map_airports (v: vector of airports)
    ==================================================
    Creates a kml file that located all the airports from the vector introduced
    v: vector of airports extracted from the file
    Created by Raúl Criado on May 18th 2020
    Fixed and tested by Jonathan Pichel on May 28th 2020
    """
    try:
        with open("Airports.kml", "w") as f:
            f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
            f.write("<Document>\n")
            for ap in v:
                coords = ap.location.split(',')
                if len(coords) != 2:
                    print(f" [ERROR] (map_airports) Wrong location data on airport {ap.code}.")
                    return False
                try:
                    float(coords[0])
                    float(coords[1])
                except ValueError:
                    print(f" [ERROR] (map_airports) Wrong location data on airport {ap.code}.")
                    return False
                f.write("\t<Placemark>"+' '+"<name>"+ap.code+"</name>\n")
                f.write("\t\t<description>"+ ap.name + "</description>\n")
                f.write("\t\t<Point>\n")
                f.write("\t\t\t<coordinates>\n")
                f.write("\t" * 4 +str(ap.location)+"\n")
                f.write("\t\t\t</coordinates>\n")
                f.write("\t\t</Point>\n")
                f.write("\t</Placemark>\n")
            f.write("</Document>\n")
            f.write("</kml>\n")
            return True
    except AttributeError:
        print(" [ERROR] (map_airports) Wrong parameters. Provide a list of Airports.")
        return False
    except IOError:
        print(" [ERROR] (map_airports) Couldn't create the file.")
        return False

def search_airport_index(v, s):
    """ Function search_airport_index (v: vector of Airport, s: String)
    =================================================
    Search the index of the desired airport
    v: vector of Airport, the vector which are our airports
    s: string, the ICAO code of the airport
    Return: integer, the index on the vector
    Created by Adrià Vaquer on 11th May 2020
    """
    try:
        for i in range(len(v)):
            if v[i].code == s:
                return i
        return -1
    except AttributeError:
        print(" [ERROR] (search_airport_index) Wrong Parameters, please provide a vector of airports")

def calculate_fee(ap, t):
    """ Function calculate_fee (ap: Airport, t: Integer)
    =================================================
    Calculates the cost of the airport
    ap: Airport, the airport we want to know its costs
    t: integer, the number of minutes we want to leave the aircraft
    Return: integer, the total cost
    Created by Adrià Vaquer on May 11th 2020
    Tested by Jonathan Pichel on May 27th 2020
    """
    try:    
        if t < 0:
            print(" [ERROR] (calculate_fee) Negative time interval.")
            return
        cost = ap.fees
        total_hours = t / 60
        if total_hours > ap.free_hours:
            paid_hours = total_hours - ap.free_hours
            extra_cost = paid_hours * ap.cost_per_hour
            cost += extra_cost
        return cost
    except AttributeError:
        print(" [ERROR] (calculate_fee) Wrong Parameters, please provide an Airport")
        return

def read_airport_costs(v, f):
    """ Function read_airport_costs (v: vector of airports, f: string):
    ===================================================
    this function reads the content of the file f to sets the costs of the airports in the vector v. 
    f: String, the name of the file
    v: Vector of airports
    Created by Pol Roca on May 18th 2020
    Fixed and tested by Jonathan Pichel on May 25th
    """
    try:
        # We enumerate the iteration to be able to communicate errors to the user
        for i, line in enumerate(open(f, 'r')):
            # We don't process the header, in case there is one
            if not line.startswith('AIRP'):
                words = line.split()
                try:
                    if len(words) != 4:
                        raise IndexError
                    code = words[0]
                    runway = int(words[1])
                    free = int(words[2])
                    cph = int(words[3])
                except (IndexError, ValueError) as format_error:
                    print(f" [ERROR] (read_airport_costs) Wrong format at line {i + 1}.")
                    continue
                # If there was no errors, add the airport
                else:
                    position = search_airport_index(v, code)
                    if position != -1:
                        set_costs(v[position], runway, free, cph)
    except FileNotFoundError:
        print("[ERROR] (read_airport_costs) File couldn't be found.")
        return
    except PermissionError:
        print(" [ERROR] (read_airport_costs) You don't have permissions over that file.")
        return