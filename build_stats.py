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
days = [str(i) for i in range(1, 32)]
days_failures = defaultdict(int)

for day in days:
    if len(day) == 1:
        day = '0' + day
    for result in results:
        if result[6] == day:
            days_failures[day] += int(result[2])

print "Which day of the month has the most test failures?"
failure_list1 = []
for day in days:
    if len(day) == 1:
        day = '0' + day
    failure_list1.append(days_failures[day])
    print day, days_failures[day]
mean_std(failure_list1)
