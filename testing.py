movies_dict = {"This is my goal":3.09, "More than this":2.5, "My stalled engine":2.2,"You and him":1.8}

for m in movies_dict.items():
    if 4 > m[1] > 3:

        print(f"{m[0]} is Great")