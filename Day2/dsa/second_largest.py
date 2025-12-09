# second_largest.py
nums = list(map(int, input("Enter numbers separated by space: ").split()))
unique = sorted(set(nums), reverse=True)
if len(unique) >= 2:
    print("2nd largest =", unique[1])
else:
    print("No second largest (all elements same or single element).")
