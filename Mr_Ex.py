import os, sys
os.system("git pull")
try:
    __import__("Mr_Ex").danger_menu()
except Exception as e:
    exit(str(e))
