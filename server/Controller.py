from pydualsense import pydualsense, TriggerModes

def cross_pressed(state):
    print(state)

def joystick(stateX, stateY):
    print(f'joystick {stateX} {stateY}')


ds = pydualsense() # open controller
ds.init() # initialize controller

ds.cross_pressed += cross_pressed
ds.light.setColorI(255,0,0) # set touchpad color to red
ds.triggerL.setMode(TriggerModes.Rigid)
ds.triggerL.setForce(1, 255)
ds.close() # closing the controller
ds.left_joystick_changed += joystick

