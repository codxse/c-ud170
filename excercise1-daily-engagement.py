import unicodecsv as csv

def csv_importer(filename):
    with open(filename, 'rb') as f:
        reader = csv.DictReader(f)
        return list(reader)

enrollments = csv_importer('enrollments.csv')
daily_engagement = csv_importer('daily_engagement.csv')
project_submissions = csv_importer('project_submissions.csv')
