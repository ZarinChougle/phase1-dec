# remove_duplicates.py
arr = list(map(int, input("Enter numbers separated by space: ").split()))
seen = set()
out = []
for x in arr:
    if x not in seen:
        out.append(x)
        seen.add(x)
print("Without duplicates:", out)
