#!/usr/bin/env python

from subprocess import call

project_name = "my_project"
domain = "project.my"

call(["django-admin.py",
      "startproject",
      "--template=project_template",
      project_name,
      "--domain",
      domain])
call(["rm", "-rf", project_name])
