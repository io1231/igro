import hashlib

my_name = "d.galamaga"
m = hashlib.md5()
m.update(my_name.encode())

if __name__ == "__main__":
