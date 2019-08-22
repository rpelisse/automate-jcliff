#!/bin/bash

export ANSIBLE_NOCOLOR='True'

readonly JCLIFF_ROLE_NAME='redhat-cop.jcliff'
readonly PLAYBOOK='/work/ansible-fest-demo/ansible-fest-rhel8-jcliff.yml'

yum install ansible
ansible-galaxy install "${JCLIFF_ROLE_NAME}"
ansible-playbook -vvvv "${PLAYBOOK}"
