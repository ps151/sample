import time, os, schedule, subprocess
while True:
	count = 0
	f = open("README.md", "a")
	f.write("a\n")
	f.close()
	subprocess.run(["git", "add", "*"])
	subprocess.run(["git", "commit", "-m", "a"])
	subprocess.run(["git", "push"])
	print('==================',count+11,'====================')
   