# -------------------------------
# NUMERIC TYPES
# -------------------------------
integer_val = 10
float_val = 3.14
complex_val = 2 + 3j

print("Numeric Types:")
print("int:", integer_val)
print("float:", float_val)
print("complex:", complex_val)


# -------------------------------
# SEQUENCE TYPES
# -------------------------------
string_val = "Hello Python"
list_val = [1, 2, 3, 4]
tuple_val = (10, 20, 30)
range_val = range(5)

print("\nSequence Types:")
print("str:", string_val)
print("list:", list_val)
print("tuple:", tuple_val)
print("range:", list(range_val))  # convert to list for display


# -------------------------------
# MAPPING TYPE
# -------------------------------
dict_val = {"name": "Ayushman", "age": 23}

print("\nMapping Type:")
print("dict:", dict_val)


# -------------------------------
# SET TYPES
# -------------------------------
set_val = {1, 2, 3, 3}  # duplicate removed automatically
frozenset_val = frozenset([4, 5, 6])

print("\nSet Types:")
print("set:", set_val)
print("frozenset:", frozenset_val)


# -------------------------------
# BOOLEAN TYPE
# -------------------------------
bool_val = True

print("\nBoolean Type:")
print("bool:", bool_val)


# -------------------------------
# BINARY TYPES
# -------------------------------
bytes_val = bytes([65, 66, 67])        # ASCII for A, B, C
bytearray_val = bytearray([68, 69, 70])
memoryview_val = memoryview(bytes_val)

print("\nBinary Types:")
print("bytes:", bytes_val)
print("bytearray:", bytearray_val)
print("memoryview:", memoryview_val)


# -------------------------------
# NONE TYPE
# -------------------------------
none_val = None

print("\nNone Type:")
print("NoneType:", none_val)


# -------------------------------
# TYPE CHECKING (IMPORTANT)
# -------------------------------
print("\nType Checking:")
print(type(integer_val))
print(type(string_val))
print(type(dict_val))
print(type(set_val))