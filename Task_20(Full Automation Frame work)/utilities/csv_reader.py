import csv

def get_credentials(path):
    with open(path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            return row['username'], row['password']
