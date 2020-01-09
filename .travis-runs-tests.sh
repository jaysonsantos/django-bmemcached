#!/bin/bash
sudo service memcached start
tox
exit $?
