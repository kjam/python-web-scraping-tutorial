import xlrd
from datetime import datetime

wb = xlrd.open_workbook('data/crunchbase.xlsx')
companies = wb.sheet_by_name('Companies')

# let's see the first row
print companies.row(0)

# let's iterate the rest of the rows in a generator
rows = [companies.row(index) for index in range(companies.nrows)]
for r in rows:
    if r[3].value == 'news':
        date = datetime(*xlrd.xldate_as_tuple(r[16].value, 0)[:3])
        print 'News company: %s from %s raised %s with last funding %s' % (
            r[1].value, r[9].value, r[4].value, date.strftime('%m/%d/%Y'))
