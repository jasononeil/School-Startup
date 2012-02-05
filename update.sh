#!/bin/sh

# Check if a port is open, and if so, use a proxy
# Taken from http://www.carlowens.me/2010/04/bash-script-to-check-for-open-port/

HOSTIP='192.168.0.1'
PORT='3128'

if nc -zv -w 3 $HOSTIP $PORT
then
# Set the proxy
export http_proxy=http://$HOSTIP:$PORT
export https_proxy=http://$HOSTIP:$PORT
fi

# Now move into the directory and try to pull it down.
cd $1
git pull