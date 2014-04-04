from csv import DictReader
from datetime import datetime

with open('data/schedule.csv') as document:
    reader = DictReader(document)
    for row in reader:
        day = datetime.strptime(row.get('START_DATE'), '%m/%d/%y')
        if 'PNC' in row.get('LOCATION') and day.weekday() > 4:
            print 'HOME WEEKEND GAME!! %s on %s' % (
                row.get('SUBJECT'), row.get('START_DATE'))
