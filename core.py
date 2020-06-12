import data

def next_workout():
    workouts = data.get_workouts(7, ['squat', 'deadlift', 'bench_press', 'press'])
    workouts = sorted(workouts, key=lambda x: x['date'], reversed=True)
