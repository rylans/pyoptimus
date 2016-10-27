'''python jenkins
build trigger api'''

import requests
from requests.auth import HTTPBasicAuth
import getpass

class pyjenkins:
    trigger_url_start = 'https://ci-comp.tasktop.com/job/'
    trigger_url_end = '/build?delay=0sec'

    def __init__(self):
        self.start = pyjenkins.trigger_url_start
        self.end = pyjenkins.trigger_url_end

    def trigger(self, connector_job_name, username, password):
        print "Triggering connector: " + connector_job_name
        full_url = self.start + connector_job_name + self.end
        print full_url
        resp = requests.post(full_url, auth=HTTPBasicAuth(username, password))
        return resp

if __name__ == '__main__':
    username = raw_input('Username: ')
    password = getpass.getpass('Password: ')
    connector_name = raw_input('Connector job name to trigger: ')

    jenkins = pyjenkins()
    print jenkins.trigger(connector_name, username, password)
