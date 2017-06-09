#!/usr/bin/env bash

sudo cp /vagrant/scripts/SMT-http_emdc1sml01_dmz_local.repo /etc/yum.repos.d/

sudo yum -y --nogpgcheck update
sudo yum -y --nogpgcheck groupinstall development
sudo yum -y --nogpgcheck install httpd mod_ssl

sudo cp /vagrant/scripts/httpd.conf /etc/httpd/conf/

sudo iptables -I INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -I INPUT -p tcp --dport 5009 -j ACCEPT
sudo service iptables save

sudo /sbin/chkconfig httpd on
sudo /sbin/chkconfig --list httpd

wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
tar xzf Python-3.6.1.tgz
cd Python-3.6.1
./configure
make
sudo make install
cd ..
rm -rf Python-3.6.1.tgz Python-3.6.1

sudo /usr/local/bin/pip3 install --upgrade pip
sudo /usr/local/bin/pip3 install --upgrade setuptools
sudo /usr/local/bin/pip3 install --upgrade virtualenv

cd /vagrant
yes | ./venv_setup.sh

sudo mkdir -p /var/log/creativewebadmin
sudo chmod 777 /var/log/creativewebadmin
