import csv
import time
import datetime
from calendar import monthrange
import os

class Event:
    def __init__(self, name, time, location, recurring):
        self.name = name
        self.time = time
        self.location = location
        self.recurring = recurring

class Task:
    def __init__(self, name, time, completed, recurring, time_sensitive):
        self.name = name
        self.time = time
        self.completed = completed
        self.recurring = recurring
        self.time_sensitive = time_sensitive

def getEvents(year, month):
    events = []
    # with open("./projects/calendar_py/events.csv", newline='') as eventsfile:
    with open("./events.csv", newline='') as eventsfile:
        reader = csv.reader(eventsfile);
        next(reader)
        for row in reader:
            name = str(row[0])
            stime = str(row[1])
            time_object = datetime.datetime.strptime(stime, '%m/%d/%Y %H:%M:%S')
            location = str(row[2])
            recurring = int(row[3])
            events.append(Event(name=name, time=time_object, location=location, recurring=recurring))
    
    events_in_month = [event.time.day for event in events if event.time.year == year and event.time.month == month]
    events_dict = {day:events_in_month.count(day) for day in events_in_month}

    return events_dict

def getTasks(year, month):
    tasks = []
    # with open("./projects/calendar_py/tasks.csv", newline='') as eventsfile:
    with open("./tasks.csv", newline='') as tasks_file:
        reader = csv.reader(tasks_file);
        next(reader)
        for row in reader:
            name = str(row[0])
            stime = str(row[1])
            time_object = datetime.datetime.strptime(stime, '%m/%d/%Y %H:%M:%S')
            completed = bool(row[2])
            recurring = int(row[3])
            time_sensitive = bool(row[4])
            tasks.append(Task(name=name, time=time_object, completed=completed, recurring=recurring, time_sensitive=time_sensitive))
    
    tasks_in_month = [task.time.day for task in tasks if task.time.year == year and task.time.month == month]
    tasks_dict = {day:tasks_in_month.count(day) for day in tasks_in_month}

    return tasks_dict

def printCalendar(year, month):

    events_dict = getEvents(year, month)
    tasks_dict = getTasks(year, month)

    days_in_month = monthrange(year, month)

    calendar = ""
    calendar += "+-----------+-----------+-----------+-----------+-----------+-----------+-----------+\n"
    calendar += "| Sunday    | Monday    | Tuesday   | Wednesday | Thursday  | Friday    | Saturday  |\n"
    calendar += "|___________|___________|___________|___________|___________|___________|___________|\n"

    start_day = days_in_month[0] + 1
    if start_day == 6:
        start_day = 0
    else:
        start_day += 1

    month_length = days_in_month[1]

    for week in range(0, (days_in_month[0] + days_in_month[1]) // 7 + (days_in_month[1] % 7 > 0)):

        calendar_day = ""
        calendar_events = ""
        calendar_tasks = ""


        for day in range(1, 8):
            
            calendar_index = week * 7 + day
            day_of_month = calendar_index - start_day + 1


            if calendar_index < start_day or calendar_index >= month_length + start_day:
                calendar_day += '|           '
                calendar_events += '|           '
                calendar_tasks += '|           '
            else:
                events_on_day = events_dict.get(day_of_month)
                tasks_on_day = tasks_dict.get(day_of_month)

                calendar_day += f"|{day_of_month}{' ' * (10 - ((day_of_month) // 10 > 0 ))}"

                if events_on_day:
                    calendar_events += f"|{events_on_day} events{' ' * (11 - len(str(events_on_day)) - len(' events'))}"
                else:
                    calendar_events += '|           '

                if tasks_on_day:
                    calendar_tasks += f"|{tasks_on_day} tasks{' ' * (11 - len(str(tasks_on_day)) - len(' tasks'))}"
                else:
                    calendar_tasks += '|           '

            if day == 7:
                calendar_day += "|\n"
                calendar_events += "|\n"
                calendar_tasks += "|\n"

        calendar += calendar_day
        calendar += calendar_events
        calendar += calendar_tasks
        calendar += "|___________|___________|___________|___________|___________|___________|___________|\n"

   
    print(calendar, end='')

def createEvent():
    with open("./events.csv", "a") as events_file:
        tmpstr = f"{input('Name: ')},{input('Time (mm/dd/yyyy hh/mm/ss): ')},{input('Location: ')},{input('Recurring interval (0 if not recurring): ')}\n"
        events_file.write(tmpstr)

def createTask():
    with open("./tasks.csv", "a") as tasks_file:
        tmpstr = f"{input('Name: ')},{input('Time (mm/dd/yyyy hh/mm/ss): ')},{0},{input('Recurring interval (0 if not recurring): ')},{input('Time sensitive: ')}\n"
        tasks_file.write(tmpstr)

def removeEvent(name):
    rows = []
    with open("./events.csv", 'r') as events_file:
        reader = csv.reader(events_file)
        for row in reader:
            if row[0] != name:
                rows.append(row)
    with open("./events.csv", 'w') as events_file:
        writer = csv.writer(events_file)
        for row in rows:
            writer.writerow(row)

def removeTask(name):
    rows = []
    with open("./tasks.csv", 'r') as tasks_file:
        reader = csv.reader(tasks_file)
        for row in reader:
            if row[0] != name:
                rows.append(row)
    with open("./tasks.csv", 'w') as tasks_file:
        writer = csv.writer(tasks_file)
        for row in rows:
            writer.writerow(row)

def prompt():
    print('e: create event | t: create task | re: remove event | rt: remove task | cal: show calendar')
    answer = input()
    
    if answer == 'e':
        createEvent()
    elif answer == 't':
        createTask()
    elif answer == 're':
        removeEvent(input("Event name:"))
    elif answer == 'rt':
        removeTask(input("Task name:"))
    elif answer == 'cal':
        printCalendar(int(input("Year: ")), int(input("Month: ")))

def main():
    stop = False;
    while stop != True:
        prompt()
    
main()
# print(events[0].name, type(events[0].name))
# print(events[0].time, type(events[0].time))
# print(events[0].location, type(events[0].location))
# print(events[0].recurring, type(events[0].recurring))