'''build statistics'''

import numpy as np
from pyoptimus import pyoptimus
from collections import defaultdict

def mean_std(arr):
    mean = float(np.mean(arr, axis=0))
    std = float(np.std(arr, axis=0))

    print "Mean={0:.2f}".format(mean)
    print "Std={0:.2f}".format(std)

pyopt_raw = pyoptimus('raw_list')
results = [r for r in pyopt_raw.build_results() if 'None' not in r]

# Which day of the month as the most test failures?
def failures_on_day(results):
    print "Which day of the month has the most test failures?"
    days = [str(i) for i in range(1, 32)]
    days_failures = defaultdict(int)

    for day in days:
        if len(day) == 1:
            day = '0' + day
        for result in results:
            if result[6] == day:
                days_failures[day] += int(result[2])

    failure_list1 = []
    for day in days:
        if len(day) == 1:
            day = '0' + day
        failure_list1.append(days_failures[day])
        print day, '|'*(days_failures[day]/500)
    mean_std(failure_list1)
    day_max = str(np.argmax(failure_list1)+1)
    print "Max=" + str(max(failure_list1)) + " failures on the " + day_max +"th day"

def failures_on_hour(results):
    print "Which hour of the day has the most test failures?"
    hours = [str(i) for i in range(24)]
    hours_failures = defaultdict(int)

    for hour in hours:
        if len(hour) == 1:
            hour = '0' + hour
        for result in results:
            if result[7] == hour:
                hours_failures[hour] += int(result[2])

    failure_list1 = []
    for hour in hours:
        if len(hour) == 1:
            hour = '0' + hour
        failure_list1.append(hours_failures[hour])
        print hour, '|'*(hours_failures[hour]/500)
    mean_std(failure_list1)
    hour_max = str(np.argmax(failure_list1))
    print "Max=" + str(max(failure_list1)) + " failures at " + hour_max + " AM"


#failures_on_day(results)
failures_on_hour(results)
