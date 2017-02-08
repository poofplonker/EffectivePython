""" Lesson One of Effective: Python, Know your version! """

#Know which version you are using

#python --version does this in the command line#

from os import system
from sys import version
system("python --version")
print version

#Automatically prints to the command line.
#Calling this script with python prints python2 info because that is the
#default.
