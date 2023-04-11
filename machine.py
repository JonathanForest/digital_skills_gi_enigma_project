from .settings import *
from enigma.machine import EnigmaMachine

machine = EnigmaMachine.from_key_sheet(
    rotors=ROTORS,
    reflector=REFLECTOR,
    ring_settings=RING_SETTINGS,
    plugboard_settings=PLUGBOARD
)

