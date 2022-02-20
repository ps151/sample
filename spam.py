import time, os, schedule, subprocess

def test():
	f = open("README.md", "a")
	f.write("a\n")
	f.close()
	subprocess.run(["git", "add", "*"])
	subprocess.run(["git", "commit", "-m", "a"])
	subprocess.run(["git", "push"])
	print('writed')
   
schedule.every(2).seconds.do(test)
while 1:
	schedule.run_pending()
	time.sleep(0)