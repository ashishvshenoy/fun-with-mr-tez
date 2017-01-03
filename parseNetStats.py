import sys
import glob
import os
path = "latest_first_class"
total_network_read = 0
total_network_write = 0
queryList = ["12","21","50","71","85"]
vmList = ["vm1","vm2","vm3","vm4"]
frameWork = ["mr","tez"]
outputFile = open('netstats.csv','w')
start_time = -1
outputString = ""
for jobType in frameWork :
	for query in queryList :
		for vm in vmList :
			netStatFile = open(path+"/query"+query+"/"+vm+"/"+jobType+"/after/after_net_stats")
			lines = [line.rstrip('\n') for line in netStatFile]
			vmNetRead = 0
			vmNetWrite = 0

			for line in lines :
				if "eth0" in line :
					wordList = line.split()
					vmNetRead+=int(wordList[1])
					vmNetWrite+=int(wordList[9])
			netStatFileBefore = open(path+"/query"+query+"/"+vm+"/"+jobType+"/before/before_net_stats")

			lines = [line.rstrip('\n') for line in netStatFileBefore]
			for line in lines :
				if "eth0" in line :
					wordList = line.rsplit()
					vmNetRead-=int(wordList[1])
					vmNetWrite-=int(wordList[9])
			print "\n Net read for vm  "+vm+" : "+vmNetRead+" Net write for vm "+vm+" : "+vmNetWrite
			total_network_read+=vmNetRead
			total_network_write+=vmNetWrite
		total_network_write = total_network_write/pow(10,6)
		total_network_read = total_network_read/pow(10,6)
		outputString+="\nQuery"+query+","+jobType+","+str(total_network_read)+","+str(total_network_write)
		total_network_read = 0
		total_network_write = 0

outputFile.write(outputString)