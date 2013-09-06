#!/usr/bin/env python

from subprocess import call

project_name = "my_project"

def test_newproject():
    """ i want to start a project"
    call(["django-admin.py",
        "startproject",
        "--template=project_template",
        project_name])
    call(["rm", "-rf", project_name])
