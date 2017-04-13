#!/usr/bin/env bash
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install python3
sudo apt-get -y install python3-dev
sudo apt-get -y install python3-pip
sudo pip3 install flask
sudo pip3 install twilio
sudo pip3 install uwsgi
sudo apt-get -y install nginx
sudo service nginx start
sudo apt-get -y install emacs
