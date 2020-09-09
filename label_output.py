import csv

with open('output.csv', 'r') as f, open('outputnew.csv', 'w', newline='') as out:
    reader = csv.reader(f)
    writer = csv.writer(out, quotechar=None)
    for r in reader:
        for i in r:
            writer.writerow(i.split(':'))