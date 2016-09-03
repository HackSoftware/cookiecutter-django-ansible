Cookiecutter Django Ansible
===========================
[![Build Status](https://travis-ci.org/HackSoftware/cookiecutter-django-ansible.svg?branch=travisCI)](https://travis-ci.org/HackSoftware/cookiecutter-django-ansible)

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), Cookiecutter Django Ansible is a framework for jumpstarting an ansible project for provisioning a server that is ready for your [cookiecutter-django](https://github.com/pydanny/cookiecutter-django) application.

Features
--------
- Works with latest cookiecutter-django
- Fully automates the provisioning project
    - Sets up a postgres server
    - Sets up a NGINX server
    - Sets up a upstart job
    - Sets up env files
    - Sets up ability to separate db server from application server. For easier scaling.
    - Sets up staging and production server. For easier development cycle.
    - Sets up celery with rabbitmq-server
    - Sets up a letsencrypt configuration (Comming soon!)
- Works for
    - Ubuntu 14.04

Requirements
------------
Install `cookiecutter` command line: `pip install cookiecutter`

Usage
-----
Generate a new Cookiecutter template layout: `cookiecutter gh:HackSoftware/cookiecutter-django-ansible`

License
-------
This project is licensed under the terms of the [MIT License](/LICENSE)
