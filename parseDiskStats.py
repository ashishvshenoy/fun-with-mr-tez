import sys
import glob
import os
path = sys.argv[1]
total_disk_read = 0
total_disk_write = 0
queryList = ["12","50"]
vmList = ["vm1","vm2","vm3","vm4"]
frameWork = ["tez"]
outputFile = open('diskstats.csv','w')
start_time = -1
outputString = ""
for jobType in frameWork :
	for query in queryList :
		for vm in vmList :
			diskStatFile = open(path+"/query"+query+"/"+vm+"/"+jobType+"/after/after_disk_stats")
			lines = [line.rstrip('\n') for line in diskStatFile]
			vmDiskRead = 0
			vmDiskWrite = 0

			for line in lines :
				if "sdc1" in line or "sdb1" in line or "sda1" in line :
					wordList = line.split()
					print "\n***"+wordList[5]
					vmDiskRead += int(wordList[5])
					vmDiskWrite += int(wordList[9])
			diskStatFileBefore = open(path+"/query"+query+"/"+vm+"/"+jobType+"/before/before_disk_stats")
			lines = [line.rstrip('\n') for line in diskStatFileBefore]
			for line in lines :
				if "sdc1" in line or "sdb1" in line or "sda1" in line :
					wordListBefore = line.split()
					print "\n***Before"+wordListBefore[5]
					vmDiskRead -= int(wordListBefore[5])
					vmDiskWrite -= int(wordListBefore[9])
			print "\nQuery : "+query+" VM : "+vm+" type : "+jobType+" Disk Read : "+str(vmDiskRead)+" Disk Write :"+str(vmDiskWrite)
			total_disk_read+=vmDiskRead
			total_disk_write+=vmDiskWrite
		
		total_disk_read = (total_disk_read*512)/pow(10,6)

		total_disk_write = (total_disk_write*512)/pow(10,6)

		print "\n***Total Disk Write For Query : "+query+jobType+" is "+str(total_disk_write)
		print "\n***Total Disk Read For Query :"+query+jobType+" is "+str(total_disk_read)
		outputString += "Query"+query+","+jobType+","+str(total_disk_read)+","+str(total_disk_write)+"\n"
		total_disk_write = 0
		total_disk_read = 0

outputFile.write(outputString)

