
# Here, we import the EnigmaMachine class into our file so that we can use it
# later. We're importing it from the enigma module that we installed earlier
# using 'pip install ..
from settings import ROTORS, REFLECTOR, RING_SETTINGS, PLUGBOARD
from machine import machine
from decrypt import brute_force_rotor_position

# Here we are loading the message we need to decrypt.
with open("message.txt", mode="r") as f:
    message = f.read()

result = brute_force_rotor_position(machine, message, "WETTER")

if result != 0:
    machine.set_display(result)
    message = machine.process_text(message)
else:
    message = "could not decrypt :("

with open("unencrypted_text.txt", mode="w") as f:
    f.write(message)

