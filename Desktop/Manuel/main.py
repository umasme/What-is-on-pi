
import time
import linearactuator
import LightSabers 
# import cancancan
from sshkeyboard import listen_keyboard
from pysabertooth import Sabertooth


## Speed Controlls
lin_speed:int  = 30
turn_speed:int = 50
dig_speed:int  = 100

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
    global lin_speed,turn_speed,dig_speed

    
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
    
    if key == "e":
        LA.move(+1)
    elif key == "q":
        LA.move(-1)
        
    if key == "space":
        Rego.dig(dig_speed)
    if key == "r":
        Rego.deposition()

    if key == "1":
        lin_speed = 10
    elif key == "2":
        lin_speed = 20
    elif key == "3":
        lin_speed = 30
    elif key == "4":
        lin_speed = 40
    elif key == "5":
        lin_speed = 50
    
    if key == "6":
        turn_speed = 10
    elif key == "7":
        turn_speed = 20
    elif key == "8":
        turn_speed = 30
    elif key == "9":
        turn_speed = 40
    elif key == "0":
        turn_speed = 50
        
        
        
    if key is not in ["w","a","s","d","e","q","space","r"]: 
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
