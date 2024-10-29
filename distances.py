# Makes a dictionary of distances of various spacecraft.
distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    # distance refers to every key in the dictionary, and the distances.values() function returns a list of all values associated with the key.
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")

    # for name in distances.keys():
        #print(f"{name} is {distances[name]} AU from Earth")


# Converts AU into Meters.
def convert(au):
    return au * 149597870700

main()
