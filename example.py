'''usage example'''

# import
from pyoptimus import pyoptimus

# instantiate an instance
instance = pyoptimus()

# get the most recent build result
print instance.build_results()[0]
