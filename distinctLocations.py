import csv
import regionToState


unique_locations = set()

with open('./vehicles.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    unique_locations.add(row[2] for row in csv_reader if row[2] is not None and row[2] != '')
    
    # for row in csv_reader:
        # if row[2] is not None and row[2] != '':
            # unique_locations.add(row[2])

print(list(unique_locations))

