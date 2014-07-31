# Adapted from https://github.com/ansible/ansible/blob/devel/plugins/callbacks/log_plays.py
# And https://gist.github.com/cliffano/9868180

import os
import time
import json
from datetime import datetime

datenow = datetime.now()
datenow = datenow.strftime('%Y-%m-%d')

if not os.path.exists("/var/log/ansible/hosts/html"):
    os.makedirs("/var/log/ansible/hosts/html")

FIELDS = ['cmd', 'command', 'start', 'end', 'delta', 'msg', 'stdout', 'stderr']

def human_log(res, host):
  filnename = ("/var/log/ansible/hosts/html/"+host+datenow+".html")
  path = os.path.join(filnename)
  fd = open(path, "a")
  fd.write("<h1>"+host+" "+datenow+"</h1>")
  fd.close()
  if type(res) == type(dict()):
    for field in FIELDS:
      if field in res.keys():
        html_string = '<b>{0}</b>: <p>{1}</p>'.format(field, res[field])
        path = os.path.join(filnename)
        fd = open(path, "a")
        fd.write(html_string)
        fd.close()
  print("HTML log created at "+filnename)

class CallbackModule(object):
  """
    logs playbook results, per host, as a basic html file in /var/log/ansible/hosts/html/
  """

  def on_any(self, *args, **kwargs):
    pass

  def runner_on_failed(self, host, res, ignore_errors=False):
    human_log(res, host)

  def runner_on_ok(self, host, res):
    human_log(res, host)

  def runner_on_error(self, host, msg):
    pass

  def runner_on_skipped(self, host, item=None):
    pass

  def runner_on_unreachable(self, host, res):
    human_log(res, host)

  def runner_on_no_hosts(self):
    pass

  def runner_on_async_poll(self, host, res, jid, clock):
    human_log(res, host)

  def runner_on_async_ok(self, host, res, jid):
    human_log(res, host)

  def runner_on_async_failed(self, host, res, jid):
    human_log(res, host)

  def playbook_on_start(self):
    pass

  def playbook_on_notify(self, host, handler):
    pass

  def playbook_on_no_hosts_matched(self):
    pass

  def playbook_on_no_hosts_remaining(self):
    pass

  def playbook_on_task_start(self, name, is_conditional):
    pass

  def playbook_on_vars_prompt(self, varname, private=True, prompt=None, encrypt=None, confirm=False, salt_size=None, salt=None, default=None):
    pass

  def playbook_on_setup(self):
    pass

  def playbook_on_import_for_host(self, host, imported_file):
    pass

  def playbook_on_not_import_for_host(self, host, missing_file):
    pass

  def playbook_on_play_start(self, pattern):
    pass

  def playbook_on_stats(self, stats):
    pass