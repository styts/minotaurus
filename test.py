#!/usr/bin/env python

import os
from fabric.api import local

project_name = "example"


def test_0_newproject():
    # delete output if exists
    if os.path.exists("./" + project_name):
        local('rm -rf ' + project_name)

    # create project from template
    local('django-admin.py startproject --template=templates/project ' +
        project_name)

    # create settings link
    ln_cmd = 'ln -s development.py\
          %(p)s/%(p)s/settings/__init__.py' % {"p": project_name}
    local(ln_cmd)

    # test that index page loads
    local('py.test %s/tests.py -x -s' % project_name)

    # * get http index
    # * check request content

    #content = request.content
    #assert "bootstrap.less" in content

    # this comes at the end
    #local('rm -rf ' + project_name)
