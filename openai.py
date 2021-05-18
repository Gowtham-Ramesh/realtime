import os 
import subprocess

subprocess.run(['ls -lrt {}'.format(os.getcwd())], shell=True)
