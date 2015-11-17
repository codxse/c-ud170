import unicodecsv as csv

# Latihan 1: fungsi convert csv ke dictonary
def csv_importer(filename):
    with open(filename, 'rb') as f:
        reader = csv.DictReader(f)
        return list(reader)

enrollments = csv_importer('enrollments.csv')
daily_engagement = csv_importer('daily_engagement.csv')
project_submissions = csv_importer('project_submissions.csv')
