s = {"Yugesh":100, "Venki":90, "Abi":80, "Prasaanth":99}

high_mark_std = max(s, key=s.get)
highest_score = s[high_mark_std]

print(high_mark_std)