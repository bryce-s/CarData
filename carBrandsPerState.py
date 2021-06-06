from collections import defaultdict
import csv
import regionToState



with open('./vehicles.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)

    import collections
    stateToBrandToCount = defaultdict(lambda: defaultdict(lambda: 0))
     
    for row in csv_reader:
        location: str = row[2]
        manufacturer: str = row[6]
        if not (None in [location, manufacturer] or '' in [location, manufacturer]):
            state = ''
            try:
                state = regionToState.regionToStateMapping[location]
            except:
                print(f'failed to map {location} to a state abbrev.')
            if state != '' :
                stateToBrandToCount[state][manufacturer] += 1
            

print(stateToBrandToCount.keys())
print(stateToBrandToCount)
print("CA")
print(stateToBrandToCount["CA"])
print("MI")
print(stateToBrandToCount["MI"])
print("FL")
print(stateToBrandToCount["FL"])



