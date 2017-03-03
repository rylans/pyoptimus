'''python jenkins
build trigger api'''

import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError
import getpass

class pyjenkins:
    login_url = 'https://ci-comp.tasktop.com/me/my-views/view/All/'
    trigger_url_start = 'https://ci-comp.tasktop.com/job/'
    trigger_url_end = '/build?delay=0sec'

    def __init__(self, username, password):
        self.start = pyjenkins.trigger_url_start
        self.end = pyjenkins.trigger_url_end
        self.username = username
        self.password = password

    def login(self):
        return self._check_login()

    def _check_login(self):
        r = requests.get(pyjenkins.login_url, auth=HTTPBasicAuth(self.username, self.password))
        try:
            r.raise_for_status()
        except HTTPError as e:
            print e
            return False
        return True

    def _url_builder(self, connector_job_name):
        if 'connector-' in connector_job_name:
            return self.start + connector_job_name + self.end
        else:
            return self.start + 'connector-' + connector_job_name + self.end

    def trigger(self, connector_job_name):
        print "Triggering connector: " + connector_job_name
        full_url = self._url_builder(connector_job_name)
        #full_url = self.start + connector_job_name + self.end
        print full_url
        resp = requests.post(full_url, auth=HTTPBasicAuth(self.username, self.password))
        resp.raise_for_status()
        return True

if __name__ == '__main__':
    username = raw_input('Username: ')
    password = getpass.getpass('Password: ')

    jenkins = pyjenkins(username, password)

    if jenkins.login():
        connector_name = raw_input('Connector job name to trigger: ')
        print jenkins.trigger(connector_name)
