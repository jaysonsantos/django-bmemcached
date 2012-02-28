#!/bin/bash
nosetests --version
DJANGO_SETTINGS_MODULE=tests.settings nosetests --with-coverage --cover-package=django_bmemcached
exit $?

