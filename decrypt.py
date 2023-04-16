def brute_force_rotor_position(machine, ciphertext, cribtext ):
    """Brute Force Attack on the Enigma Machine"""
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # This is the brute force part, where we cycle through all possible
    # three letter combinations of the alphabet and attempt decrypting the
    # text.
    for i in alphabet:  # This is the first rotor
        for j in alphabet:  # This is the second rotor
            for k in alphabet:  # This is the third rotor
                # Concatenate (join) all the rotor letters above to create the
                # rotor string
                rotor = i + j + k

                # Let's set the machine rotor positions to our current guess
                # and process/decrypt the text, storing the result in the
                # variable plaintext
                machine.set_display(rotor)

                # TODO: What's wrong with this line?
                plaintext == machine.process_text(ciphertext)

                # Let's see if we can see our cribtext in the plain/decrypted
                # text. If it is, we will 'return' the current rotor position
                # as we think that works!

                # TODO: Something is missing here...
                if cribtext in plaintext:
                    return rotor

    # TODO: We need this line to return a 0, how to we do that?
    # Look at the return above for a hint...
    return

