#!/bin/bash
rootDir=/var/www/oxal.org
appDir=$rootDir/public
nginxConf=oxal.org.conf

# First time set up root directory
if [ ! -d "$appDir" ]; then
    sudo mkdir -p $appDir
    sudo chown -R `whoami`:www-data $rootDir
    cd $appDir
    echo "Rsync now and run this again"
    exit
fi

# Copies nginx files and symlinks
if [ ! -f "/etc/nginx/sites-available/$nginxConf" ]; then
    sudo cp $rootDir/conf/$nginxConf /etc/nginx/sites-available/$nginxConf
fi

# -h is for checking symlinks
if [ ! -h "/etc/nginx/sites-enabled/$nginxConf" ]; then
    sudo ln -s /etc/nginx/sites-available/$nginxConf /etc/nginx/sites-enabled/$nginxConf
fi

# Pull changes, copy configs, reload config
cd $appDir
#git pull
#pip3 install -r requirements.txt
sudo cp $rootDir/conf/$nginxConf /etc/nginx/sites-available/$nginxConf
sudo nginx -t && \
    sudo nginx -s reload || \
    echo "Error in configuration / nginx"
