from collections import defaultdict
import csv
from os import stat
import regionToState
import json

with open('./vehicles.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)

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

manufacturers = set([brand for state in stateToBrandToCount.keys() for brand in list(stateToBrandToCount[state].keys())])
stateToTotalVehicles = dict({state: sum(stateToBrandToCount[state].values()) for state in stateToBrandToCount.keys()})

stateBrandToPercent = defaultdict(lambda: defaultdict(lambda: 0))
for state in stateToBrandToCount.keys():
    for brand in stateToBrandToCount[state].keys():
        count: int = stateToBrandToCount[state][brand]
        stateBrandToPercent[state][brand] = count / stateToTotalVehicles[state] 
    

def BrandPercentages(stateBrandToPercent: dict, brand: str):
    stateId = 1
    results = sorted([
       {
        "id": state,
        "percentage": str(stateBrandToPercent[state][brand]),
        "val": str(idx+1) if idx+1 > 10 else f'0{idx+1}' 
       }  
        for idx, state in enumerate(sorted(stateBrandToPercent.keys())) 
      ], key=lambda x: x["percentage"])
    resJsonStr = json.dumps(results, indent=2)
    print(resJsonStr)
BrandPercentages(stateBrandToPercent, 'ford')
BrandPercentages(stateBrandToPercent, 'toyota')
# print("MI")
# print(stateBrandToPercent["MI"])
# print("NY")
# print(stateBrandToPercent["NY"])
# print("TX")
# print(stateBrandToPercent["TX"])

print('manufacturers')
print(manufacturers)



