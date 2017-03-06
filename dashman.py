'''dashboard manager'''

from pyjenkins import pyjenkins
from pyoptimus import pyoptimus

import getpass
import schedule
import time

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='log_dashman.log')

class DashboardManager:
    def __init__(self, username, password):
        self.log_lines = []
        self.jenkins = pyjenkins(username, password)
        self.optimus = pyoptimus('raw_list')
        assert self.jenkins.login()
        self._log_line("Login successful. [" + username + "]")

    def _log_now(self):
        from time import localtime, strftime
        return strftime("%Y-%m-%d %H:%M:%S", localtime())

    def _log_line(self, string):
        self.log_lines.append(self._log_now() + ': ' + string)
        logging.debug(string)
        print string

    def _internal_manage(self):
        self._log_line("internal manage")

        irise = ('com.tasktop.connector.irise', 'connector-irise')
        pivotal = ('com.tasktop.connector.pivotal.tracker', 'connector-pivotal-tracker')

        # too many http 500s
        #leankit = ('com.tasktop.connector.leankit', 'connector-leankit')

        cons = [irise, pivotal]

        for con in cons:
            self._log_line("triggering " + con[1])
            self.jenkins.trigger(con[1])

    def manage(self):
        self._log_line("CALL manage")

        schedule.every().day.at("14:41").do(self._internal_manage)

        for job in schedule.jobs:
            self._log_line(str(job))

        while True:
            schedule.run_pending()
            time.sleep(1)

    def result(self):
        return self.log_lines

if __name__ == '__main__':
    username = raw_input('Username: ')
    password = getpass.getpass('Password: ')
    dashman = DashboardManager(username, password)
    try:
        dashman.manage()
    except KeyboardInterrupt:
        for k in dashman.result():
            print k
