text = input("Greeting: ").strip().lower()

if (text.startswith("h")):
    if (text.startswith("hello")):
        print("$0")
    else:
        print("$20")

else:
    print("$100")
