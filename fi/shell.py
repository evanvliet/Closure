'''
Created on Mar 10, 2012

@author: ericvanvliet
'''
import subprocess, sys
subprocess.call(
    ['bash', '--login'], 
    stdin=sys.__stdin__, 
    stdout=sys.__stdout__,
    stderr=sys.__stderr__,
    )