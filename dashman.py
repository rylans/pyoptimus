'''dashboard manager'''

from pyjenkins import pyjenkins
from pyoptimus import pyoptimus

import getpass
import schedule
import time

class DashboardManager:
    def __init__(self, username, password):
        self.jenkins = pyjenkins(username, password)
        self.optimus = pyoptimus('raw_list')
        assert self.jenkins.login()

    def _internal_manage(self):
        print "internal manage..."

        irise = ('com.tasktop.connector.irise', 'connector-irise')
        leankit = ('com.tasktop.connector.leankit', 'connector-leankit')
        pivotal = ('com.tasktop.connector.pivotal.tracker', 'connector-pivotal-tracker')

        cons = [irise, leankit, pivotal]

        for con in cons:
            print "triggering: " + con[1]
            self.jenkins.trigger(con[1])

    def manage(self):
        print "managing..."

        schedule.every().day.at("14:41").do(self._internal_manage)
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == '__main__':
    username = raw_input('Username: ')
    password = getpass.getpass('Password: ')
    DashboardManager(username, password).manage()
