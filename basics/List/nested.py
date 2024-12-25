# Nested list
print("Nested list")
randomList = [1, 2, 3, [["one", "two"], "three"]]
print(randomList[3])         # [["one","two"],"three"]
print(randomList[3][1])      # "three"
print(randomList[3][0][1])   # "two"
