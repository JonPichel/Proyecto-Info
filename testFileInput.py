import aircraft, flight, airline, assignment, airport

#Call the function read_airline to test the file AL:
print("READ AIRLINE")
input("Wrong filename:")
al = airline.read_airline("dafasdfsafa")
input("First wrong format:")
al = airline.read_airline("AP.txt")
input("Second wrong format:")
al = airline.read_airline("APC.txt")
airline.show_airline(al)
print("Right file:")
al = airline.read_airline("AL.txt")
input("AIRLINE INFORMATION:")
airline.show_airline(al)

#Call the function read_airports to test the file AP:
print("READ AIRPORTS")
input("Wrong filename:")
ap_list = airport.read_airports("dafasdfsafa")
input("First wrong format:")
ap_list = airport.read_airports("AL.txt")
input("Second wrong format:")
ap_list = airport.read_airports("APC.txt")
print("This should be an empty list:", ap_list)
input("Right file:")
ap_list=airport.read_airports("AP.txt")
for ap in ap_list:
    airport.show_airport(ap)

# Wrong filename
print("READ AIRPORT COSTS")
input("Wrong filename:")
airport.read_airport_costs(ap_list, "dfsafdfsf")
input("First wrong format:")
airport.read_airport_costs(ap_list, "AL.txt")
input("Second wrong format:")
airport.read_airport_costs(ap_list, "AP.txt")
#Call the function read_airport_costs to test the file APC:
input("Right file:")
airport.read_airport_costs(ap_list, "APC.txt")
for ap in ap_list:
    airport.show_airport(ap)
