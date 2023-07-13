sample_text="Hello World"

print("UTF-8 Encoding :")
utf_8=sample_text.encode("utf-8")
print(f"Encoded UTF-8 : {utf_8}")
utf_8=utf_8.decode("utf-8")
print(f"Decoded UTF-8 : {utf_8}")

print("UTF-16 Encoding :")
utf_8=sample_text.encode("utf-16")
print(f"Encoded UTF-16 : {utf_8}")
utf_8=utf_8.decode("utf-16")
print(f"Decoded UTF-16 : {utf_8}")

print("UTF-32 Encoding :")
utf_8=sample_text.encode("utf-32")
print(f"Encoded UTF-32 : {utf_8}")
utf_8=utf_8.decode("utf-32")
print(f"Decoded UTF-32 : {utf_8}")

print("ASCII Encoding :")
utf_8=sample_text.encode("ascii")
print(f"Encoded ASCII : {utf_8}")
utf_8=utf_8.decode("utf-8")
print(f"Decoded ASCII : {utf_8}")

