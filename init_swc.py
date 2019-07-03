
#%%



#import neuron
#import neuron.hoc
#import neuron.hclass3
#import neuron.psection
#import cfg


from netpyne import sim

# read cfg and netParams from command line arguments if available; otherwise use default
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='cfg_swc.py', netParamsDefault='netParams_swc.py')					

# Create network and run simulation
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)

