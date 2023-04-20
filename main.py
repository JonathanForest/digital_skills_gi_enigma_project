# Here, we import the EnigmaMachine class into our file so that we can use it
# later. We're importing it from the enigma module that we installed earlier
# using 'pip install ..
from settings import ROTORS, REFLECTOR, RING_SETTINGS, PLUGBOARD
from machine import machine
from decrypt import brute_force_rotor_position

print("""
PROJECT ENIGMA

This code attempts to brute force an attack on a message encrypted by an Enigma
machine.

""")


# TODO: I've forgotten to add something so that Python knows the words inside
# the brackets are a string, what is that?
filepath = input(Enter the name of the file that contains the encrypted message: )

cribtext = input("Enter a word that is known to be in the unencrypted message: ")

# Here we are loading the message we need to decrypt.
with open(filepath, mode="r") as f:
    # TODO: f.read is a function. I've written it here but it doesn't actually
    # run., what do I need to do for this line to call/run
    # the function?
    message = f.read

# This calls the function brute_force_rotor_position, which will try every
# combination of rotors until it either returns a three letter rotor
# combination or 0
result = brute_force_rotor_position(machine, message, cribtext)

# The brute force attack worked if result is not equal to 0
# TODO: We need to check if result equals 0, how do we do that?
# replace the underscore with the stuff you need.
if _ == 0:
    # Here we print the following words so that the user knows we couldn't
    # crack the code.
    print("The code could not be decrypted. :(")

else:

    print("We cracked the code! The rotors will be set to " + result)

    #Here we set the rotors to the result of the brute force attack.
    machine.set_display(result)

    # Here we run the decryption on the message we loaded earlier.
    message = machine.process_text(message)

    # This is the code that writes to the file.
    with open("unencrypted_text.txt", mode="w") as f:
        f.write(message)
