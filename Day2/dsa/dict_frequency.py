# dict_frequency.py
arr = list(map(int, input("Enter numbers separated by space: ").split()))
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
print("Frequencies:", freq)
