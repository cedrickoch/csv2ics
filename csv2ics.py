import csv
from ics import Calendar, Event
from datetime import datetime
import pytz

# Create a new calendar
calendar = Calendar()

# Read the CSV file
with open('examples/calendar.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    # Iterate through each row in the CSV file
    for row in csvreader:
        # Exlude all Jungschützen events
        if row['Art'] != 'JS' and row['Anlass'] != 'Theorie JS':
            # Combine the date and time fields
            datefrom = datetime.strptime(row['Datum'] + ' ' + row['Von'], '%d/%m/%Y %H:%M')
            dateto = datetime.strptime(row['Datum'] + ' ' + row['Bis'], '%d/%m/%Y %H:%M')
            # Set the timezone to Europe/Zurich
            datefrom = datefrom.replace(tzinfo=pytz.timezone('Europe/Zurich'))
            dateto = dateto.replace(tzinfo=pytz.timezone('Europe/Zurich'))

            # Create an event
            event = Event()
            event.name = row['Anlass']
            event.begin = datefrom
            event.end = dateto
            event.location = row['Anderer Ort']

            # Add the event to the calendar
            calendar.events.add(event)

            print('Event added: ' + row['Anlass'] + ' ' + row['Art'] + ' ' + datefrom.strftime('%Y/%m/%d %H:%M') + ' ' + dateto.strftime('%Y/%m/%d %H:%M') + ' ' + row['Anderer Ort'])
        else:
            continue

# Generate an iCalendar file
with open('calendar.ics', 'w') as f:
    f.writelines(calendar)

print("Calendar created successfully!")
