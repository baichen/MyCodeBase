# Source: https://stackoverflow.com/questions/380870/make-sure-only-a-single-instance-of-a-program-is-running

# The following program assures that only one running instance for a python script

from tendo import singleton
me = singleton.SingleInstance() # will sys.exit(-1) if other instance is running

# The above method rely on the tendo library, which seems not supported by PyInstaller
# So, if we want to use pyinstaller to package our program, use the following implementation instead
import fcntl, sys
def singleton():
    pid_file = 'program.pid'
    fp = open(pid_file, 'w')
    try:
        fcntl.lockf(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
        # another instance is running
        sys.exit(0)
