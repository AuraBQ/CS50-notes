def main():
    time = input("What time is it? ").strip()
    if (7.0 <= convert(time) <= 8.0):
        print("Breakfast time")
    elif(12.0 <= convert(time) <= 13.0):
        print("Lunch time")
    elif(18.0 <= convert(time) <= 19.0):
        print("Dinner time")
    else:
        return

# Converts the time input into the ##:## format.
def convert(time):
    # adds ':' in ##:##
    x, y = time.split(":")
    # float() turns x into a value which represents hours, turns y into a value which represents minutes. Minutes is split into a value of 1/60.
    hr = float(x)
    mins = float(y) * 1 / 60
    
    return float(hr + mins)

if __name__ == "__main__":
    main()
