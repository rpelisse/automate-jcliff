#!/bin/bash
# A simple test suite, designed to be run by a ci-server
set -e

export ANSIBLE_NOCOLOR='True'
ansible-playbook -vvvv /work/wildfly-setup.yml
ansible-galaxy install redhat-cop.jcliff
# temporary fix
readonly ROLE_DIR='/root/.ansible/roles/redhat-cop.jcliff/tasks'
mkdir "${ROLE_DIR}"
cp '/work/tasks/main.yml' "${ROLE_DIR}"
# end of tmp fix

ansible-playbook -vvvv /work/tune-wildfly-with-jcliff.yml --extra-vars "custom_rules_folder=/work/files/custom_rules"
rm -rf /work/*
