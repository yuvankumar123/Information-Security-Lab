import hashlib
a = input("Enter a string:\n")
result = hashlib.md5(a.encode())
print("The byte equivalent of hash is:", end=" ")
print(result.digest())

print("The available algorithms are:", end=" ")
print(hashlib.algorithms_guaranteed)
