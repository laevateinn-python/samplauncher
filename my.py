from pathlib import Path
import sys
import os
import subprocess

s = "127.0.0.1"
p = "7777"
n = "vladgf"

args = [direc,"-c","-h",s,"-p",p,"-n",n]

p = subprocess.run(args,stdout=subprocess.PIPE)

print(p.stdout)