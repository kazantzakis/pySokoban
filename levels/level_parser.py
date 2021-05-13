import os

with open(os.path.dirname(os.path.abspath(__file__)) + '/magic_sokoban6/magic_sokoban6.txt','r') as f:
	
	level = 0
	
	for line in f:
		if line.strip() == "":
			level += 1
			print("Level " + str(level)
			level_file = open(os.path.dirname(os.path.abspath(__file__)) + '/magic_sokoban6/level' + str(level),'w')
		else :
			level_file.write(line)