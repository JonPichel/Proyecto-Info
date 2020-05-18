with open("Airport_map.kml", "w") as f:
    f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
    f.write("<Document>\n")
    ap = ['BIKF',63.9869444444,-22.6144444444,'Airport of Reykjavik']
    f.write("  <Placemark>"+' '+"<name>"+ap[0]+"</name>\n")
    f.write("    <description>"+ ap[3] + "</description>\n")
    f.write("    <Point>\n")
    f.write("     <coordinates>\n")
    f.write('       '+str(ap[2])+','+str(ap[1])+'\n')
    f.write("     </coordinates>\n")
    f.write("    </Point>\n")
    f.write("  </Placemark>\n")
    f.write("</Document>\n")
    f.write("</kml>\n")
