# READ DATA FROM A FILE NAMED "poem.txt" AND FIND OUT WHETHER IT CONTAINS THE WORD "twinkle"

with open("poem.txt") as f:
    content=f.read()
    if "twinkle" in content:
        print("TWINKLE WORD IS PRESENT")
    else:
        print("TWINKLE WORD NOT FOUND!")
        