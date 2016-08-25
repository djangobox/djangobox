#!/bin/bash


django-admin startproject $1
cd $1
./manage.py startapp myapp
