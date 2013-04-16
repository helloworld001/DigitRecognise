'''
Created on 2013-4-16

@author: golden_zhang
'''
from Tkinter import *
from neuron import *
from ttk import *
import random
import copy

class digitGUI(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        