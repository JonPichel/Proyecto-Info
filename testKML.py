import airport,flight,assignment,aircraft,airline
import webbrowser
import time
#map_airports, map flights, map_assignment
#We make a vector of airports with the function read_airports of a text file
vector_airports=airport.read_airports("AP.txt")

#We make a vector of flights with the function read_flights of a text file
vector_flights=flight.read_flights("FL.txt")

#We make an assignment for the map_assignment
#We make an aircraft for the assignment
ac=aircraft.Aircraft()
ac.callsign="N978CP"
ac.seats=300
ac.type="B777"
assig=assignment.Assignment()
assignment.assign_aircraft(assig, ac)
for i in vector_flights:
    assignment.assign_flight(assig, i)

def airport_map():
    if airport.map_airports(vector_airports):
        print("\nYour Airports.kml file has been created")
        time.sleep(0.5)
        print("Import it on Google Earth")
        time.sleep(0.5)
        print("Opening Google Earth...")
        time.sleep(2.25)
        webbrowser.open("https://earth.google.com/web/@46.50730675,19.96957568,88.42801288a,3659981.51193509d,30y,0h,0t,0r")
    else:
        print("There have been some errors")

def flight_map():
    if flight.map_flights(vector_flights, vector_airports):
        print("\nYour Operations.kml file has been created")
        time.sleep(0.5)
        print("Import it on Google Earth")
        time.sleep(0.5)
        print("Opening Google Earth...")
        time.sleep(2.25)
        webbrowser.open("https://earth.google.com/web/@46.50730675,19.96957568,88.42801288a,3659981.51193509d,30y,0h,0t,0r")
    else:
        print("There have been some errors")

def assig_map():
    if assignment.map_assignment(assig, vector_airports):
        print("\nYour {callsign}.kml file has been created".format(callsign=ac.callsign))
        time.sleep(0.5)
        print("Import it on Google Earth")
        time.sleep(0.5)
        print("Opening Google Earth...")
        time.sleep(2.25)
        webbrowser.open("https://earth.google.com/web/@46.50730675,19.96957568,88.42801288a,3659981.51193509d,30y,0h,0t,0r")
    else:
        print("There have been some errors")

#Main
print("PHASE 4 TEST")
time.sleep(0.75)
repeat = True
while repeat == True:    
    print("FUNCTIONS TO TEST:")
    time.sleep(0.5)
    print("\t1. map_airports")
    print("\t2. map_flights")
    print("\t3. map_assignment")
    time.sleep(0.75)
    choice=eval(input("Which function do u want to test? (1,2,3):"))
    invalid=False
    if choice != 1:
        if choice != 2:
            if choice != 3:
                invalid = True
    while invalid == True:
        print("Invalid answer, please provide a correct answer")
        choice=eval(input("Which function do u want to test? (1,2,3):"))
        if choice != 1:
            if choice != 2:
                if choice != 3:
                    invalid = True
                else:
                    invalid = False
            else:
                invalid = False
        else:
            invalid = False
    if choice == 1:
        airport_map()
    elif choice == 2:
        flight_map()
    elif choice == 3:
        assig_map()
    time.sleep(5)
    choice2=input("Do you want to test another function? (y/n):".lower())
    if choice2 == "y":
        repeat = True
    elif choice2 == "n":
        repeat = False
print("\nTEST TERMINATED")
time.sleep(0.5)
print("Closing test program")
time.sleep(0.5)
print("Hope I see you again")
time.sleep(0.5)
print("""
           |      |
           |      |

       __            __
         |__      __|
            |____|    
""")