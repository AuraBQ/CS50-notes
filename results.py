#results = ["Mario", "Luigi"]

#results.append("Princess")
#results.append("Yoshi")
#results.append("Koopa Troopa")
#results.append("Toad")


#results.append(["Bowser", "Donkey Kong Jr."])
#results.remove(["Bowser", "Donkey Kong Jr."])
#results.extend(["Bowser", "Donkey Kong Jr."])

#print(results)

#Makes a list of the following characters
results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr."]

#Removes Bowser
results.remove("Bowser")
#Inserts Bowser as the first in the list.
results.insert(0, "Bowser")
#Reverses the list
results.reverse()

print(results)
