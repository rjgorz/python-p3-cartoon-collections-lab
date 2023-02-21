def roll_call_dwarves(dwarves):
    for i in range(len(dwarves)):
        print(f"{i+1}. {dwarves[i]}")

def summon_captain_planet(list):
    return [item.title() + "!" for item in list]

def long_planeteer_calls(list):
    long = False
    for item in list:
        if len(item) > 4:
            long = True
            break
    return long

def find_the_cheese(list):
    found = False
    for item in list:
        if item == "cheddar" or item == "gouda" or item == "camembert":
            cheese = item
            found = True
            break
    if found:
        return cheese
    else:
        return None
