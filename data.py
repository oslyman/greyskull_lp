import csv
from datetime import date, datetime    

def get_workouts(days, filter_exercises):
    today = date.today()
    workouts = []
    with open('data.csv') as data:
        rows = csv.reader(data)
        headers = next(rows)
        for row in rows:
            workout = dict(zip(headers, row))
            if workout['exercise'] not in filter_exercises:
                continue
            workout['date'] = datetime.strptime(workout['date'], '%Y-%m-%d').date()
            workout['sets'] = int(workout['sets'])
            workout['reps'] = int(workout['reps'])
            if (today - workout['date']).days < days:
                workouts.append(workout)
    return workouts