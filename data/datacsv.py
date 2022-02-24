from asyncore import write
import csv

with open("heart.dat") as dat_file, open("heart.csv", 'w') as csv_file:
    o = csv.writer(csv_file)
    for line in dat_file:
        o.writerow(line.split())
        


print("here")
