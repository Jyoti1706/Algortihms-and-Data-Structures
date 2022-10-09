def check_password(minimum, maximum, char, password):
    ch_hash = {}
    for ch in password:
        ch_hash[ch] = ch_hash.get(ch, 1)

    count = ch_hash.get(char, 0)
    if minimum - 1 < count < maximum + 1:
        return "valid"
    return "invalid"


tc = int(input())

for i in range(tc):
    inp = input().replace(":", "")
    inp = inp.replace("-", " ")
    arr = inp.split(" ")
    print(check_password(int(arr[0]), int(arr[1]), arr[2], arr[3]))
