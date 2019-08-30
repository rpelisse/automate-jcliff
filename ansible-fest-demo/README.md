README
====

What do I need to run this playbook successfully?
---

* A RHEL host, properly registered into RHN
* Install ansible
* Enable repository for EAP7 in /etc/yum.repos.d/redhat
* Install the redhat-cop.jcliff role:

```
# ansible-galaxy install redhat-cop.jcliff
```
* Run the playbook:

```
# ansible-playbook -vvvv "${PLAYBOOK}"
```

This playbook was tested with the following software versions:

* Red Hat Enterprise Linux Server release 7.7 (Maipo)
* ansible-playbook 2.8.4
  config file = /etc/ansible/ansible.cfg
  configured module search path = [u'/root/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python2.7/site-packages/ansible
  executable location = /usr/bin/ansible-playbook
  python version = 2.7.5 (default, Jun 11 2019, 14:33:56) [GCC 4.8.5 20150623 (Red Hat 4.8.5-39)]

