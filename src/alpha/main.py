from ..beta.my_module import suml, prodl

def magic_tricks():
    print("magic tricks!")

zeroes = [0 for _ in range(5)]
ones = [1 for _ in range(5)]
print(suml(zeroes))
print(prodl(ones))

