from settings import *
from enigma.machine import EnigmaMachine


# The following few lines create an 'instance' of an Enigma Machine. We
# imported the blueprints earlier, now we are telling Python to use those
# blueprints to make a version of the Enigma Machine we can interact with.
# 'Enigma Machine' is the class 'template', 'from_key_sheet' is a function
# belonging to the EnigmaMachine class. What arguments are we passing to it?
machine = EnigmaMachine.from_key_sheet(
    rotors=ROTORS,
    reflector=REFLECTOR,
    ring_settings=RING_SETTINGS,
    plugboard_settings=PLUGBOARD
)

