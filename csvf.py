import csv

def csv_writer(path, data):
    with open (path, "w") as csv_file:
        writer = csv.writer(csv_file)
        for line in data:
            writer.writerow(line)
