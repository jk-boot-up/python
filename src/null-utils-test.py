value = None
if value is None:
    print("value cannot be None")
elif len(value.strip()) == 0:
    print("value cannot be empty")

value = ""
if value.strip() == "":
    print("value is empty")

value = "     "
if value.isspace():
    print("value is empty, just space")