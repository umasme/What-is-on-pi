
import time
import linearactuator
import LightSabers 
# import cancancan
from sshkeyboard import listen_keyboard
from pysabertooth import Sabertooth

## dictionary that holds our telemtry
telemetry_data = {}
LA = linearactuator.linearactuator()


# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# -----------------------Helper Functions--------------------------------
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------

# Key release function
def release(key):
    print("\rPress a key!                    ",end = "")
    print("\rPress a key!                    ",end = "")
    LA.stop()
    Rego.stop()
    Derive.stop()
    # telemetry_data = cancancan.read_can(telemetry_data)
# Key press function
def press(key):
    lin_speed:int  = 30
    turn_speed:int = 50
    dig_speed:int  = 100

    print(f"\rYou pressed {key}!",end = "")
    
    
    key = key.lower()
    if  key == 'w':    
        Derive.linear_motion(-lin_speed)
    elif key == 's':
        Derive.linear_motion(lin_speed)
    elif key == 'a':
        Derive.turn_motion(-turn_speed)
    elif key == 'd':
    	Derive.turn_motion(turn_speed)
    elif key == "e":
        LA.move(+1)
    elif key == "q":
        LA.move(-1)
    elif key == "space":
        Rego.dig(dig_speed)
    elif key == "r":
        Rego.deposition()
    else: 
        print("\rN3RD!                  ",end = "") 

# -----------------------------------------------------------------------
# -----------------------------------------------------------------------
# --------------------------Entering Main--------------------------------
# -----------------------------------------------------------------------
# -----------------------------------------------------------------------


if __name__ == '__main__':
    # Lynn    = Actuator.linearactuator()
    Derive  = LightSabers.DriveTrain()
    Rego    = LightSabers.CheeseGrater()

    print("-"*15)
    print("-"*15)
    print("Starting The Fun!")
    
    time.sleep(0.05)
    while True:
            listen_keyboard(on_press=press, on_release=release, sequential=True)
            time.sleep(0.001)
