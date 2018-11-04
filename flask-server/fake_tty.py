import subprocess, pty, os

m, s = pty.openpty()
fm = os.fdopen(m, "rw")
p = subprocess.Popen(["np-prompt", "-p"], stdin=s, stdout=s, stderr=s)
p.communicate()
os.close(s)
print fm.read()