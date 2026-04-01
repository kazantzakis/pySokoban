import os

with open(os.path.dirname(os.path.abspath(__file__)) + '/magic_sokoban6/magic_sokoban6.txt','r') as f:

	level = 0
	level_file = None

	for line in f:
		if line.strip() == "":
			level += 1
			print("Level " + str(level))
			if level_file is not None:
				level_file.close()
			level_file = open(os.path.dirname(os.path.abspath(__file__)) + '/magic_sokoban6/level' + str(level),'w')
		else:
			if level_file is not None:
				level_file.write(line)

	if level_file is not None:
		level_file.close()