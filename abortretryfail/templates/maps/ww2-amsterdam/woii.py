import csv
import json

csv_reader = csv.DictReader(open('WOII.csv', 'r'))
csvfile = open('WOII.csv', 'r')

fieldnames = csv_reader.fieldnames
jsonfile = open('woii.json', 'w')

reader = csv.DictReader(csvfile, fieldnames)
jsonfile.write('var data = [')
count = 0
for row in reader:
    if row:
        count += 1
        if count > 1:
            json.dump(row, jsonfile)
            jsonfile.write(',')
jsonfile.write('];')
jsonfile.close()