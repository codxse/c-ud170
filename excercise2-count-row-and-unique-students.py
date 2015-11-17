import unicodecsv as csv

# Latihan 1: fungsi convert csv ke dictonary
def csv_importer(filename):
    with open(filename, 'rb') as f:
        reader = csv.DictReader(f)
        return list(reader)

enrollments = csv_importer('enrollments.csv')
daily_engagement = csv_importer('daily_engagement.csv')
project_submissions = csv_importer('project_submissions.csv')

# Latihan 2: print banyak row dan unique students
def count_unique_enrolled_students(list_of_dict, unique_key):
    unique_enrolled_students = set()
    for row in list_of_dict:
        unique_enrolled_students.add(row[unique_key])

    return len(unique_enrolled_students)

def get_unique_students(data):
    unique_students = set()
    for data_point in data:
        unique_students.add(data_point['account_key'])

    return unique_students

for engagement_record in daily_engagement:
    engagement_record['account_key'] = engagement_record['acct']
    del[engagement_record['acct']]


print len(enrollments)
print len(daily_engagement)
print len(project_submissions)
print '----------'
print count_unique_enrolled_students(enrollments, 'account_key')
print count_unique_enrolled_students(daily_engagement, 'account_key')
print count_unique_enrolled_students(project_submissions, 'account_key')
