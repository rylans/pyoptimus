'''
Optimus data retrieval
'''

import urllib2
import json

class pyoptimus:
    def __init__(self):
        self.OPTIMUS_URL = 'http://optimus.van.tasktop.com'
        self.GET_RESULTS = '/build_results'

    def build_results(self, connector=None):
        url = self.OPTIMUS_URL + self.GET_RESULTS
        response = urllib2.urlopen(url)
        if connector:
            data = [c for c in json.load(response) if connector in c['connector_kind']]
        else:
            data = json.load(response)
        return data

    def serialize_build(self, build):
        connector_id = int(build['connector_id'])
        pass_count = int(build['pass_count'])
        fail_count = int(build['fail_count'])
        skip_count = int(build['skip_count'])
        duration = int(build['duration'])

        count = float(pass_count + fail_count + skip_count)

        return [float(connector_id), pass_count/count, fail_count/count, skip_count/count, float(duration)]


def main():
    instance = pyoptimus()
    results = instance.build_results()
    print results[0]
    print instance.serialize_build(results[0])

if __name__ == '__main__':
    main()
