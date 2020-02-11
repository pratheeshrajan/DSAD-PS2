# How to run: Open the shell and enter the command: python Mobile_Manufacturing.py
# input file inputPS1 should be in the same folder location

import sys
class Mobile_Manufacturing:
	# Initializing variables
	def __init__(self):
		self.itemList = [];
		self.orderList = [];
		self.totalTime = 0;
		self.idleTime = 0;
		
	# Reading the input file
	def readFile(self):
		try:
			with open('inputPS1.txt', 'r') as file:
				for line in file:
					#print(line);
					data = line.split('/');
					productId = data[0].strip();
					self.itemList.append({
						'productId' : int(data[0].strip()), 
						'parts_manufacturing_time' : int(data[1].strip()), 
						'assembling_time' : int(data[2].strip())
					});
			if len(self.itemList) is 0:
				print("Empty File");
				print("Done");
				sys.exit();
		except (OSError) as e:
			print("Error in reading file");
			print("Done");
			sys.exit();
			
	# Finding the minimal time using greedy algo
	def findOptimalSolution(self):
		sortedItemList = sorted(self.itemList, key=lambda k: k['parts_manufacturing_time']);
	
		#Adding the first products manufacturing time to the idle time
		idleTime = sortedItemList[0]['parts_manufacturing_time'];
		assemblingTime = 0;

		for i in range(len(sortedItemList)):
			self.orderList.append(str(sortedItemList[i]['productId']));
			# Finding assembling time and idle time based on the assembling time and next manufacturing time
			if( i < len(sortedItemList) - 1  and sortedItemList[i]['assembling_time'] + assemblingTime <  sortedItemList[i+1]['parts_manufacturing_time']):
				idleTime = idleTime + sortedItemList[i+1]['parts_manufacturing_time'] - sortedItemList[i]['assembling_time'];
			assemblingTime = assemblingTime + sortedItemList[i]['assembling_time'];
			
		self.idleTime = idleTime;
		self.totalTime = idleTime + assemblingTime;
		
	# Writing to the output file
	def writeOutput(self):
		outfile = open("outputPS1.txt", "w");
		outfile.write("Mobiles should be produced in the order : " + ','.join(self.orderList) + "\n");
		outfile.write("Total production time for all mobiles is : " +str(self.totalTime) + "\n");
		outfile.write("Idle Time of Assembly unit : " +str(self.idleTime) + "\n");
		outfile.close()
		
	
if __name__ == '__main__':
	print("Started Execution");
	mobileManufacturing = Mobile_Manufacturing();
	mobileManufacturing.readFile();
	mobileManufacturing.findOptimalSolution();
	mobileManufacturing.writeOutput();
	print("Done");
	
