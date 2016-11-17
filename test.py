import subprocess


subprocess.call(['cat','/data/logs/gmlog/net.log'],stdin=None, stdout=subprocess.STDOUT, stderr=None, shell=True)

arr = []
for x in range(20160901, 20160931):
    arr.append("%s" % x)
print arr
