#!/usr/bin/env python
import os
import sys

def test_something():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")
    from django.conf import settings
    print "Name:", settings.PROJECT_PATH
