
#%%

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:33:29 2019

@author: René, Adna and Carmen
"""
import os
wdir=os.getcwd()

from netpyne.support import morphology
from netpyne import sim
from neuron import h
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import platform
import neuron as nrn
if platform.system() == 'Windows':
    nrn.load_mechanisms(os.path.join(wdir + 'Morph_practice', 'modfiles'))
    import sys
    sys.path.append('C:', 'nrn', 'lib', 'python')
    sys.path.append('D:', 'Okinawa', 'Python')
    sys.path.append(wdir + 'Morph_practice', 'modfiles')

#load cell as mycell
#    def getmorph(self):
myCell= morphology.Cell()
morphology.load(filename=os.path.join(wdir,'SWC', 'AA_0266.swc'), cell=myCell)

#plot loaded cell
fig = plt.figure()
ax = plt.axes(projection='3d')
morphology.shapeplot(h, ax)
           
#get the sections from the cell
secs=list(h.allsec());
secs_all = secs
soma = []
axon = []
dend = []


    #get the sections fro soma, axon and dend
    #def getset(self):
for sec in secs:
    name = sec.name()   
    if name[0:4] == 'soma':
        soma.append(sec)
    if name[0:4] == 'axon':
        axon.append(sec)
    if name[0:4] == 'dend':
        dend.append(sec)


class TC_cell():

    def __init__(self):
            
            self.add_biophys_all()
            self.add_biophys_axon()
            self.add_biophys_soma()
            self.add_biophys_dend()
            #self.getmorph()
            #self.getset()
    
    def add_biophys_all(self):
        for sec in secs_all:
            sec.Ra = 178 #add a axial resistance of 100ohm per square cm
            sec.cm = 0.8 # Membrane capacitance in micro Farads / cm^2

    #give the cell biphys props
    def add_biophys_soma(self):       
        for sec in soma:
            sec.insert('hh')
            #sec.insert('na')
            #sec.insert('kv')
            
    
    def add_biophys_axon(self):   
        for sec in axon:
            sec.insert('hh')
            #sec.insert('na')
            #sec.insert('kv')
        
    def add_biophys_dend(self):       
        for sec in dend:
            sec.insert('pas')
        
    add_biophys_all(secs_all)     
    add_biophys_soma(soma)
    add_biophys_axon(axon)
    add_biophys_dend(dend)


def MakeCell():
    TC = TC_cell()
    return TC
