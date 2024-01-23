import os, sys
os.system("git pull")
try:
    __import__("MR_EX").danger()
except Exception as e:
    exit(str(e))
