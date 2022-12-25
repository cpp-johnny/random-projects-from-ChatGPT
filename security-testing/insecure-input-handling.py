import sys

def run_command(command):
    os.system(command)

command = sys.argv[1]
run_command(command)
