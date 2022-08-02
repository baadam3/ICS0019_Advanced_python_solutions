from csv import reader
import matplotlib.pyplot as plot
from mpl_toolkits.basemap import Basemap

def DrawMap():
    fig, ax = plot.subplots(figsize=(10, 10))
    m = Basemap(
        projection="merc",
        llcrnrlat=34,
        urcrnrlat=70,
        llcrnrlon=-30,
        urcrnrlon=40,
        resolution="l",
    )
    m.drawcoastlines()
    m.fillcontinents()
    m.drawcountries()

    mapB = csv("before_covid.csv")
    mapA = csv("after_covid.csv")


    DrawConnections(mapB,mapA, m)

    ax.set_title("Flight from Tallinn, before and After COVID-19 Balint Adam")
    plot.savefig("map.svg")
    plot.show()


def DrawConnections(mapB, mapA, flights):
    tll = [24.832799911499997, 59.41329956049999]

    for airport in mapB:
        if airport == "TLL":
            continue
        flightX = float(mapB[airport]["Longitude"])
        flightY = float(mapB[airport]["Latitude"])
        plot.annotate(airport, xy=flights(flightX,flightY), verticalalignment = "center", color= "black")

        x, y = flights(flightX, flightY)

        flights.plot(x, y, marker=".", color="blue", markersize=10)
        
        flights.drawgreatcircle(flightX, flightY, tll[0], tll[1], linewidth=2, color="blue")

    for airport in mapA:
        if airport == "TLL":
             continue
        flightX = float(mapA[airport]["Longitude"])
        flightY = float(mapA[airport]["Latitude"])

        plot.annotate(airport, xy=flights(flightX,flightY), verticalalignment = "center", color= "black")

        x, y = flights(flightX, flightY)

        flights.plot(x, y, marker=".", color="red", markersize=10)

        flights.drawgreatcircle(flightX, flightY, tll[0], tll[1], linewidth=2, color="red")

def GetAirportData(flight):
    airportData = []
    file = r"data/" + flight
    with open(file, "r", encoding="utf-8") as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:
            airportData.append(row[0].split(";")[1])  ## IATA

    return airportData

def csv(flight):
    ## Merge CSV files and filter out the ones that are not flying from Tallinn

    airportData = GetAirportData(flight)
    headers = [
        "ID",
        "Name",
        "City",
        "Country",
        "IATA",
        "ICAO",
        "Latitude",
        "Longitude",
        "Altitude",
        "Timezone",
        "DST",
        "DZ",
        "Type",
        "Source",
    ]

    airportDataDic = {}
    file = r"data/airports.csv"
    with open(file, "r", encoding="utf-8") as read_obj:
        csv_reader = reader(read_obj)
        for row in csv_reader:

            iata = row[4]  # Key
            if (iata in airportData):  
                airportDataDic[iata] = {}
                for counter, header in enumerate(headers):
                    airportDataDic[iata][header] = row[counter]

    return airportDataDic


def main():
    DrawMap()

if __name__ == "__main__":
    main()