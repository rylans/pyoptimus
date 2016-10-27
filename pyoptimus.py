'''
Optimus data retrieval

timestamp -> month, day, hour
'''

import urllib2
import json

class pyoptimus:
    def __init__(self, serializer=None):
        self.OPTIMUS_URL = 'http://optimus.van.tasktop.com'
        self.GET_RESULTS = '/build_results?from=2014-01-01'
        self.serializer = serializer

    def build_results(self, connector=None):
        url = self.OPTIMUS_URL + self.GET_RESULTS
        response = urllib2.urlopen(url)
        if connector:
            data = [c for c in json.load(response) if connector in c['connector_kind']]
        else:
            data = json.load(response)
        return [self.serialize_build(b) for b in data]

    def serialize_build(self, build):
        if self.serializer is 'csv':
            return self.serialize_build_as_csv(build)
        elif self.serializer is 'floats':
            return self.serialize_build_as_floats(build)
        return build

    def schema(self):
        return ['connector_id', 'pass_count', 'fail_count', 'skip_count',
                'duration', 'timestamp_month', 'timestamp_day', 'timestamp_hour']

    def timestamp_part(self, label, timestamp):
        if label == 'timestamp_month':
            return timestamp.split('-')[1]
        elif label == 'timestamp_day':
            return timestamp.split('-')[2].split('T')[0]
        elif label == 'timestamp_hour':
            return timestamp.split('T')[1].split(':')[0]
        else:
            raise RuntimeError('Invalid timestamp part label')

    def serialize_build_as_csv(self, build):
        csv_items = []
        for key in self.schema():
            if 'timestamp_' in key:
                value = self.timestamp_part(key, build['timestamp'])
            else:
                value = build[key]
            csv_items.append(str(value))
        return ','.join(csv_items)

    def serialize_build_as_floats(self, build):
        connector_id = int(build['connector_id'])
        pass_count = int(build['pass_count'])
        fail_count = int(build['fail_count'])
        skip_count = int(build['skip_count'])
        duration = int(build['duration'])

        count = float(pass_count + fail_count + skip_count)

        return [float(connector_id), pass_count/count, fail_count/count, skip_count/count, float(duration)]

def main():
    instance = pyoptimus('csv')
    results = instance.build_results()
    print len(results)
    print instance.schema()
    print results[:3]

if __name__ == '__main__':
    main()
