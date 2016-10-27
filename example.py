'''usage example'''

# import
from pyoptimus import pyoptimus

# instantiate an instance
instance = pyoptimus()

# get recent build results
res = instance.build_results()

# print a build result
print res[0]

# print number of build results retrieved
print "Total build results: ", len(res)

# grab build results for a certain connector
sp_results = instance.build_results('sharepoint')
print "Sharepoint build results: ", len(sp_results), sp_results[0]


# Get a few rally build results and serialize as csv
csv_instance = pyoptimus('csv')
print csv_instance.schema()
print csv_instance.build_results('jira')[:4]
