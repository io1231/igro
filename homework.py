import hashlib

my_name = "d.galamaga"
<<<<<<< HEAD

m = hashlib.sha256()
=======
m = hashlib.md5()
>>>>>>> parent of bf485a6... Change md5 to sha256
m.update(my_name.encode())

if __name__ == "__main__":
    print(f"Task completed by {my_name}! md5 hash is {m.hexdigest()}")
