#!/bin/bash

dockerInfo=$(docker info 2>&1)

if [[ $dockerInfo != *"Swarm: active"* ]]
then
	swarminit=$(docker swarm init --advertise-addr $1)
	if [[ $swarminit != *"Swarm initialized"* ]]
	then
		echo $swarminit
		exit 1
	fi
fi

exit 0
