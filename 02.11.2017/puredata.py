import os,sys,subprocess
sub = subprocess.Popen(["pd"],stdin=subprocess.PIPE,
	stdout=subprocess.PIPE)
print(sub.poll())
print(sub.stdin)
#print(sub.communicate("a = 12\nprint(a)\n"))
#print(sub.poll())
#print(sub.communicate("print(a)\n"))
#sub.kill()