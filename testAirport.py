import aircraft, flight, airline, assignment, airport

#Create a couple of airports
ap1=airport.Airport()
ap2=airport.Airport()


#Test the function set_ap_info:
input("TESTING FUNCTION SET_AP_INFO:")
airport.set_ap_info(ap1, "LEGE", "Girona-Costa Brava Airport", "41.900833,2.760556")
airport.set_ap_info(ap2, "LEVX", "Vigo Airport", "42.229167,-8.6275")
print("The ICAO code of the airports are: ",ap1.code," and ",ap2.code)
print("The compete name of the airports are: ",ap1.name," and ",ap2.name)
print("The location of the airports are: ",ap1.location," and ",ap2.location)


#Test the function set_costs:
input("TESTING FUNCTION SET_COSTS:")
airport.set_costs(ap1, 3000, 2, 1000)
airport.set_costs(ap2, 4000, 1, 2000)
print("The  costs of the runways are: ",ap1.fees," and ",ap2.fees)
print("The the numbers of free hours of parking are: ",ap1.free_hours," and ",ap2.free_hours)
print("The costs per hour of any additional parking are: ",ap1.cost_per_hour," and ",ap2.cost_per_hour)

#Test the function calculate_fee:
input("TESTING FUNCTION CALCULATE_FEE:")
fee1=airport.calculate_fee(ap1, 60)
fee2=airport.calculate_fee(ap2, 120)
print("The airport 1 fee is ", fee1)
print("The airport 2 fee is ", fee2)


#Test the function read_airports:
input("TESTING FUNCTION READ_AIRPORTS:")
vector_of_aircrafts=airport.read_airports("AP.txt")
cont=0
vector_of_icao=[]
for i in vector_of_aircrafts:
    vector_of_icao.append(vector_of_aircrafts[cont].code)
    cont+=1
print("The airports created with the information of the file are: ", vector_of_icao)


#Test the function search_airport_index:
input("TESTING FUNCTION SEARCH_AIRPORT_INDEX:")
position1=airport.search_airport_index(vector_of_aircrafts, "LGSA")
print("If the ICAO code is not in the vector the function returns -1")
position2=airport.search_airport_index(vector_of_aircrafts, "LEGE")
print("The position of the airport in the vector is: ",position1)
print("If the ICAO code is not in the vector the function returns: ",position2)


#Test the function read_airport_costs:
input("TESTING FUNCTION READ_AIRPORT_COSTS:")
airport.read_airport_costs(vector_of_aircrafts,"APC.txt")
cont=0
for i in vector_of_aircrafts:
    print("The airport ",vector_of_aircrafts[cont].code,"have a cost per hour of ",vector_of_aircrafts[cont].cost_per_hour)
    cont+=1
