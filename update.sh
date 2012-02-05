#!/bin/sh

# Check if a port is open, and if so, use a proxy
# Taken from http://www.carlowens.me/2010/04/bash-script-to-check-for-open-port/

HOSTIP='192.168.0.1'
PORT='3128'

# If host is up
ping -c 1 -t 1 192.168.1.1 > /dev/null 2> /dev/null  # ping and discard output
if [ $? -eq 0 ]; then  # check the exit code
    # And If host has port open
    if nc -zv -w 3 $HOSTIP $PORT; then
		# Set the proxy
		export http_proxy=http://$HOSTIP:$PORT
		export https_proxy=http://$HOSTIP:$PORT
	fi
fi


# Now move into the directory and try to pull it down.
cd $1
git pull