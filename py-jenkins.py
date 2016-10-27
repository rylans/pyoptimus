'''python jenkins
how to trigger a build'''

import requests
from requests.auth import HTTPBasicAuth
import sys
import getpass

username = raw_input('Username: ')
password = getpass.getpass('Password: ')

trigger_url_start = 'https://ci-comp.tasktop.com/job/'
trigger_url_end = '/build?delay=0sec'

connector_name = 'connector-atlassian-jira'

def trigger_build(con, username, password):
    print "Connector Name: " + con
    full_url = trigger_url_start + con + trigger_url_end
    print full_url
    resp = requests.post(full_url , auth=HTTPBasicAuth(username, password))
    print resp

trigger_build(connector_name, username, password)
