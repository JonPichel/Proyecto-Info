import aircraft

ac1 = aircraft.Aircraft()

ac1.callsign = "AC430"
ac1.type = "A320"
ac1.seats = 80

ac2 = aircraft.Aircraft()

ac2.callsign = "C423F"
ac2.type = None
ac2.seats = 240

aircraft.show_aircraft(ac1)
aircraft.show_aircraft(ac2)