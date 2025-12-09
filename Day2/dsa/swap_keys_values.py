# swap_keys_values.py
d = {}
n = int(input("How many key:value pairs? "))
for _ in range(n):
    k = input("key: ")
    v = input("value: ")
    d[k] = v
swapped = {v: k for k, v in d.items()}
print("Swapped dict:", swapped)
