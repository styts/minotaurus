#!/usr/bin/env python

import os
#import requ st
from subprocess import call
from fabric.api import local
#from cuisine import file_link

project_name = "my_project"


def test_33():
    pass


def test_newproject():
    # create project
    if not os.path.exists("./" + project_name):
        local('django-admin.py startproject --template=project_template ' +
            project_name)

    # * run runserver
    local('python %s/manage.py runserver' % project_name)
    # * get http index
    # * check request content

    #content = request.content
    #assert "bootstrap.less" in content

    # this comes at the end
    local('rm -rf ' + project_name)
