import prettytable

import data

total_work_goals = {
    'pushups': 300,
    'chinups': 60
}

def print_report():
    total_work_done = {}
    
    for workout in data.get_workouts(7, total_work_goals.keys()):
        exercise = workout['exercise']
        total_work_done[exercise] = total_work_done.get(exercise, 0) + workout['sets'] * workout['reps']
    pt = prettytable.PrettyTable()
    pt.field_names = ['Exercise', 'Work done', 'Work remaining']
    for exercise in total_work_goals:
        work_done = total_work_done.get(exercise, 0)
        goal = total_work_goals.get(exercise, 0)
        pt.add_row([exercise, work_done, goal - work_done])

    print(pt)
