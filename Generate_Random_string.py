import random
import string

letters_and_digits = string.ascii_letters+string.digits
res = (random.choice(letters_and_digits) for i in range(10))
print("".join(res))