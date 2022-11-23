#   IMPORT
import re


#   FUNCTIONS
def convert_measurements(file):
    with open(file, "r") as f:
        measurements =[]
        for line in f:
            data_search = re.search(r"(\d+)x(\d+)x(\d+)", line)
            #searches for measurments and groups them
            data_ready = (int(data_search[1]),int(data_search[2]),int(data_search[3]))
            #converts found measurments into tulpe of int
            measurements.append(data_ready)
    return measurements


def calculate_wrap(measurements):
    total_wrap = 0
    for tulpe in measurements:
        l,w,h=tulpe
        tulpe=list(tulpe)
        spare1 = min(tulpe)
        tulpe.remove(spare1)
        spare2=min(tulpe)
        spare=spare1*spare2
        package=2*(l*w) + 2*(w*h) + 2*(h*l) +spare
        total_wrap += package
    return total_wrap


def calculate_ribbon(measurements):
    total_ribbon = 0
    for tulpe in measurements:
        l, w, h = tulpe
        tulpe = list(tulpe)
        side1 = min(tulpe)
        tulpe.remove(side1)
        side2 = min(tulpe)
        bow=l*w*h
        ribbon_per_present=bow+2*side1+2*side2
        total_ribbon += ribbon_per_present
    return total_ribbon


#   MAIN
measurements = convert_measurements("input_02_12.txt.txt")
print(calculate_wrap(measurements))
print(calculate_ribbon(measurements))