# fun-with-mr-tez
Some of my scripts to evaluate MR and Tez on TPC-DS benchmark.

* start_vms.sh - This script starts all my Azure VMs after they logging in with my Azure credentials.
* copyScript.sh - Script to aggregate the statistics from all the VMs to my local machine.
* parseDiskStats.py - Parses the /proc/diskstats files and creates a csv with the disk read/write statistics.
* parseNetStats.py - Parses the /proc/net/dev files and creates a csv with the net read/write statistics.
* create_req_dirs.sh - Creates the necessary directories to run hadoop and hive on the cluster.
