#!/usr/bin/env python

import os
import subprocess
from fabric.api import local

project_name = "example"


def test_33():
    pass


def test_0_newproject():
    # create project
    #if not os.path.exists("./" + project_name):
        #local('django-admin.py startproject --template=project_template ' +
            #project_name)
    if os.path.exists("./" + project_name):
        local('rm -rf ' + project_name)
    local('django-admin.py startproject --template=project_template ' +
        project_name)

    # * run runserver
    #local('python %s/manage.py runserver' % project_name)
    ln = 'ln -s development.py\
          %(p)s/%(p)s/settings/__init__.py' % {"p": project_name}
    print ln
    local(ln)
    local('py.test %s/tests.py' % project_name)
    #process = subprocess.Popen(['python',
          #project_name,
          #'manage.py',
          #'runserver'],
         #stdout=subprocess.PIPE)
    #process.communicate()
    # * get http index
    # * check request content

    #content = request.content
    #assert "bootstrap.less" in content

    # this comes at the end
    #local('rm -rf ' + project_name)
