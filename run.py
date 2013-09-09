#!/usr/bin/env python

import os
from fabric.api import local

project_name = "example"


def main():
    # delete output if exists
    if os.path.exists("./" + project_name):
        local('rm -rf ' + project_name)

    # clear env var
    local('export DJANGO_SETTINGS_MODULE=')

    # create project from template
    local('django-admin.py startproject --template=templates/project ' +
        project_name)

    # create settings link
    ln_cmd = 'ln -s development.py\
          %(p)s/settings/__init__.py' % {"p": project_name}
    local(ln_cmd)

    # create main app from template
    local('mkdir %s/main' % project_name)
    local('django-admin.py startapp --template=templates/main_app main\
 %s/main' % project_name)

    local('createdb %s' % project_name)

    # run the main app tests
    local('export DJANGO_SETTINGS_MODULE=settings')
    local('cd %(p)s; export DJANGO_SETTINGS_MODULE=settings;\
          python manage.py test main' % {"p": project_name})

    local('dropdb %s' % project_name)

    # this comes at the end
    local('rm -rf ' + project_name)

if __name__ == '__main__':
    main()
