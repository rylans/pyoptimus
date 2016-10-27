'''
Optimus data retrieval
'''

import urllib2
import json

class pyoptimus:
    def __init__(self):
        self.OPTIMUS_URL = 'http://optimus.van.tasktop.com'
        self.GET_RESULTS = '/build_results'

    def build_results(self):
        url = self.OPTIMUS_URL + self.GET_RESULTS
        response = urllib2.urlopen(url)
        data = json.load(response)
        return data

def main():
    instance = pyoptimus()
    print instance.build_results()

if __name__ == '__main__':
    main()
