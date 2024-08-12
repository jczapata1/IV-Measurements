# Tools
from time import sleep
import numpy as np

#-------------------------------------------------------------------------------------------

# Current
def current_(start_current, stop_current, n_points):
    '''
    Generate a list of currents uniformly spaced between a starting and ending value.
    
    -       start_current(float): Inicial Current
    -        stop_current(float): Final Current
    -              n_points(int): Number of Points

    Output:
    - current(float, ndarray[?]): Current-List
    '''

    current = np.linspace(start_current, stop_current, n_points) # Current-List

    return current

#-------------------------------------------------------------------------------------------

# Current Up-Down
def current_up_down_(start_current, stop_current, n_points):
    '''
    Generate a list of currents uniformly spaced between a starting and ending value.
    
    -       start_current(float): Inicial Current
    -        stop_current(float): Final Current
    -              n_points(int): Number of Points

    Output:
    - current(float, ndarray[?]): Current-List
    '''

    current_up   = current_(start_current, stop_current, n_points) # Current Up
    current_down = current_(stop_current, start_current, n_points) # Current Down
    current      = np.concatenate([current_up, current_down])      # Currents-List

    return current

#-------------------------------------------------------------------------------------------

# Voltage
def voltage_(sourcemeter, current, delay=1.0):
    '''
    Measure the voltage using a current-voltage source.

    Input:
    - sourcemeter(GPIBInstrument): Current-Voltage Source
    -  current(float, ndarray[?]): Current-List
    -                delay(float): Delay
    
    Output:
    -  voltage(float, ndarray[?]): Voltages-List
    '''

    time    = np.zeros(len(current)) # Times-List
    voltage = np.zeros(len(current)) # Voltages-List
    
    # Mesurement
    for i in range(len(current)):

        sourcemeter.write(f'SOUR:CURR {current[i]:.8f}')               # Set Output Current
        sleep(delay)                                                   # System Stabilization
        voltage[i] = float(sourcemeter.query('MEAS:VOLT:DC?').strip()) # Measure Voltage 
    
    return voltage