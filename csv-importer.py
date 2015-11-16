import unicodecsv as csv

# cara1, manual close
enrollments = []
f = open('enrollments.csv', 'rb')
reader = csv.DictReader(f)

for row in reader:
    enrollments.append(row)

f.close()

enrollments[0]

# cara2, automatic close
enrollments = []
with open('enrollments.csv', 'rb') as f:
    reader = csv.DictReader(f)

    for row in reader:
        enrollments.append(row)

enrollments[0]

# cara3, without loop
with open('enrollments.csv', 'rb') as f:
    reader = csv.DictReader(f)
    enrollments = list(reader)

enrollments[0]
