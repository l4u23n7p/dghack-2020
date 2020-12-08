import itertools
import operator
import sys

BLOCK = 150


class mersenne_rng(object):
    def __init__(self, seed=5489):
        self.state = [0] * 624
        self.f = 1812433253
        self.m = 397
        self.u = 11
        self.s = 7
        self.b = 0x9D2C5680
        self.t = 15
        self.c = 0xEFC60000
        self.l = 18
        self.index = 624
        self.lower_mask = (1 << 31) - 1
        self.upper_mask = 1 << 31

        # update state
        self.state[0] = seed
        for i in range(1, 624):
            self.state[i] = self.int_32(
                self.f * (self.state[i - 1] ^ (self.state[i - 1] >> 30)) + i
            )

    def twist(self):
        for i in range(624):
            temp = self.int_32(
                (self.state[i] & self.upper_mask)
                + (self.state[(i + 1) % 624] & self.lower_mask)
            )
            temp_shift = temp >> 1
            if temp % 2 != 0:
                temp_shift = temp_shift ^ 0x9908B0DF
            self.state[i] = self.state[(i + self.m) % 624] ^ temp_shift
        self.index = 0

    def get_random_number(self):
        if self.index >= 624:
            self.twist()
        y = self.state[self.index]
        y = y ^ (y >> self.u)
        y = y ^ ((y << self.s) & self.b)
        y = y ^ ((y << self.t) & self.c)
        y = y ^ (y >> self.l)
        self.index += 1
        return self.int_32(y)

    def get_rand_int(self, min, max):
        return (self.get_random_number() % (max - min)) + min

    def int_32(self, number):
        return int(0xFFFFFFFF & number)

    def shuffle(self, my_list):
        for i in range(len(my_list) - 1, 0, -1):
            j = self.get_rand_int(0, i + 1)
            my_list[i], my_list[j] = my_list[j], my_list[i]


def keystream(seeds, length, base=None):
    key = base if base else []
    for seed in seeds:
        random = mersenne_rng(seed)

        for _ in range(BLOCK):
            if len(key) == length:
                break
            key.append(random.get_rand_int(0, 255))
            random.shuffle(key)
        if len(key) == length:
            break
    return key


def encrypt(string, key):
    key = keystream(map(ord, key), len(string))
    stream =  itertools.starmap(operator.xor, zip(key, map(ord, string)))

    return bytearray(stream)


if __name__ == "__main__":
    if sys.version_info >= (3, 0):
        sys.stdout.buffer.write(encrypt(sys.stdin.read(), sys.argv[1]))
    else:
        sys.stdout.write(encrypt(sys.stdin.read(), sys.argv[1]))
