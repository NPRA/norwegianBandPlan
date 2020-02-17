import csv

f=open("BandPlan.xml", "a+")

f.write('<ArrayOfRangeEntry xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n')

with open('nasjonalfrekvensplan.csv', newline='\n') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    color = 'red'
    for row in spamreader:
        if row[0].count(' ') > 0:
            low = float(row[0].split(' ')[0])
            high = float(row[0].split(' ')[2])
            desc = row[2]
            if row[0].split(' ')[3].strip() == 'kHz':
                low = low * 1000
                high = high * 1000
            elif row[0].split(' ')[3].strip() == 'MHz':
                low = low * 1000*1000
                high = high * 1000*1000
            elif row[0].split(' ')[3].strip() == 'GHz':
                low = low * 1000*1000*1000
                high = high * 1000*1000*1000
            f.write('<RangeEntry minFrequency="{0:.0f}" maxFrequency="{1:.0f}" mode="NFM" step="12500" color="{3}">{2}</RangeEntry>\n'.format(low, high, desc, color))
        if color == 'red': 
            color = 'blue'
        elif color == 'blue':
            color = 'green'
        elif color == 'green':
            color = 'yellow'
        elif color == 'yellow':
            color = 'red'

f.write('<RangeEntry minFrequency="1575400000" maxFrequency="1575450000" mode="NFM" step="12500" color="blue">GPS (L1)</RangeEntry>\n')

f.write('</ArrayOfRangeEntry>\n')