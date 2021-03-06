#!/usr/bin/python
#this is my automation for spinning up a django server using python

import os

#install python
os.system('yum -y install python-pip')

#install the version that allows for virtual instances
os.system('pip install virtualenv')

#Upgrade per the system prompt
os.system('pip install --upgrade pip')

#make a directory called /opt/django
os.mkdir('/opt/django')
os.chdir('/opt/django')

#putting it in our 3.6.6 version
os.system('yum -y install python36')
os.system('virtualenv -p python36 django')
#os.system('source /opt/django/django/bin/activate && pip install django')

#starts the first project
#os.chdir('/opt/django')
os.system('source /opt/django/django/bin/activate && pip install django' + \
          '&& django-admin --version ' + \
          '&& django-admin startproject project1')
          
#changing the ownership of project1 and django from root to be owned by the user
os.system('chown -R koda /opt/django')
#os.system('chown -R koda /opt/django/project1')

os.system("myip=$(curl -s checkip.dyndns.org | sed -e 's/.*Current IP Address: //' -e 's/<.*$//') && sed -i \"s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \[\'$myip\'\]/g\" /opt/django/project1/project1/settings.py")
os.system('sudo -u koda  sh -c "source /opt/django/django/bin/activate && python /opt/django/project1/manage.py runserver 0.0.0.0:8000&"')

#other notes: 
#make the firewall rule in google cloud
#then try to get to the page by deleting the s in https and add colon 8000 to the end of the line enter

#find the ALLOW command in project 1
#os.system('grep -iR ALLOWED /opt/django/project1')

#take the file and copy it:
#/opt/django/project1/project1/settings.py
#open the file to edit it with the allowed ip
