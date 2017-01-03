#!/bin/bash
if [ ! -d /mnt/logs ]; then
	chown ubuntu:ubuntu /mnt;
	mkdir -p /mnt/logs/hadoop;
	mkdir -p /mnt/logs/apps;
fi;
