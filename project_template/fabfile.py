from fabric.api import run, cd, local, env
from cuisine import *

env.hosts = ['new']
env.user = 'root'

# prefix for activating virtualenv
prefix = "source /home/horsly/%s/env/bin/activate &&"

# cuisine setup
select_package("apt")


def tail():
    run('tail -f /home/horsly/production/logs/error.log')


def run_venv(cmd, env='production'):
    run(prefix % env + " " + cmd)


def uninstall():
    if fabric.contrib.console.confirm(
        "!!! ACHTUNG this will delete all data! Continue?", default=False):
        run('service apache2 stop')
        if user_check('horsly'):
            user_remove('horsly')
            run('rm -rf /home/horsly')
        file_unlink('/etc/apache2/sites-enabled/horsly')
        run('rm -rf /etc/apache2/sites-available/horsly')
        run('service apache2 start')


def setup_system():
    user_ensure('horsly', home='/home/horsly')
    if not dir_exists('/home/horsly/production'):
        with cd('/home/horsly'):
            run('git clone file:///root/repos/horsly.git production')
            run('git clone file:///root/repos/horsly.git staging')
            with cd('production'):
                run('virtualenv env')
                run_venv('pip install -r assets/requirements.txt',
                         env='production')
                with cd('horsly/settings'):
                    file_link('production.py', '__init__.py')
                run('mkdir -p logs')
                run('chown horsly:horsly logs -R')
                run('chmod o+wx logs -R')
                run('mkdir -p static')
                run_venv('./manage.py collectstatic --noinput',
                         env="production")
            with cd('staging'):
                run('virtualenv env')
                run_venv('pip install -r assets/requirements.txt',
                         env='staging')
                with cd('horsly/settings'):
                    file_link('staging.py', '__init__.py')
                run('mkdir -p logs')
                run('chown horsly:horsly logs -R')
                run('chmod o+wx logs -R')
                run('mkdir -p static')
                run_venv('./manage.py collectstatic --noinput',
                         env="staging")


def setup_apache():
    # apache: vhost
    file_upload('/etc/apache2/sites-available/horsly', 'assets/vhost.conf')
    file_link('/etc/apache2/sites-available/horsly',
              '/etc/apache2/sites-enabled/horsly')

    # apache: enable mod_rewrite
    run('a2enmod rewrite')

    # apache: restart
    run('service apache2 restart')


def setup():
    # user, home, clone
    setup_system()

    # vhost, reload
    setup_apache()


def pip_update_reqs():
    local('pip freeze -r assets/requirements.txt | \
grep -v "git-remote-helpers" > assets/requirements.txt')


def deploy(env='production'):
    local('git push')
    with cd('/home/horsly/%s' % env):
        run('git pull')
        run_venv('./manage.py collectstatic --noinput', env=env)
        run('touch horsly/wsgi.py')


def stage():
    deploy(env='staging')

#def deploy(big=False):
    #local('git push')
    #with cd('/home/horsly/horsly'):
        #run('git pull')
        #with cd('horsly'):
            #if big:
                #run('%s pip install -r assets/requirements.txt' % pref)
                #run('%s ./manage.py syncdb' % pref)
                #run('%s ./manage.py migrate' % pref)
            #run('touch horsly/wsgi.py')
