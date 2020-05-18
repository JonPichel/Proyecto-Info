with open("KMLfinal.kml", "w") as f:
    f.write("<KML_File>\n")
    f.write("<Document>\n")
    row = ['BIKF',-22.6144444444,63.9869444444]
    f.write("\t<Placemark>")
    f.write("\t\t<decription>" + row[0] + "</description>")
    f.write("\t\t<Point>")
    f.write("\t\t\t<coordinates>" + str(row[2]) + str(row[1]) + "</coordinates>")
    f.write("\t\t</Point>")
    f.write("\t</Placemark>")
    f.write("</Document>\n")
    f.write("</kml>\n")