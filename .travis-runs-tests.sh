#!/bin/bash
nosetests --version
DJANGO_SETTINGS_MODULE=tests.settings nosetests
exit $?

