===============
ansible-html
===============

An Ansible plugin for outputting logs to HTML, heavily WIP right now!

# Usage

Make a directory called `callback_plugins` next to your playbook and put `html_logs.py` inside of it

```bash
mkdir callback_plugins
cd callback_plugins
wget https://raw.githubusercontent.com/petems/ansible-html/master/callback_plugins/html_logs.py
```