def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    # name pulls every individual name in the list, then prints each name in a separate letter in the {receiver} section.
    for name in names:
        print(write_letter(name, "Princess Peach"))

# Uses receiver and sender to insert the corresponding names into the letter with an f string.
def write_letter(receiver, sender):
    return f"""
        +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
            Dear {receiver},
            
            You are cordially invited to a ball at 
            Peach's Castle this evening, 7:00 PM:
            
            Sincerely,
            {sender}
        +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        """

main()
