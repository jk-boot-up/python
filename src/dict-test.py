my_map = {"A":1, "B":2, "C":3, 5:"hello"}
for key, value in my_map.items():
    print("{0}:{1}".format(key, value))
    print(key)
    print(value)
    print(my_map.get(key))
