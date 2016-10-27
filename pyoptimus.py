'''
Optimus data retrieval
'''

import urllib2
import json

OPTIMUS_URL = 'http://optimus.van.tasktop.com'
GET_RESULTS = '/build_results'

def build_results():
    url = OPTIMUS_URL + GET_RESULTS
    response = urllib2.urlopen(url)
    data = json.load(response)
    return data

def main():
    print build_results()

def sample_build_results():
    for result in build_results()[:6]:
        print result

if __name__ == '__main__':
    #main()
    sample_build_results()

