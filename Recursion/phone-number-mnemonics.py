def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    phone_dictionary = {"1": ["1", ], "2": ['a', 'b', 'c'], "3": ['d', 'e', 'f'], "4": ['g', 'h', 'i'],
                        "5": ['j', 'k', 'l'],
                        "6": ['m', 'n', 'o'], "7": ['p', 'q', 'r', 's'], "8": ['t', 'v', 'u'],
                        "9": ['w', 'x', 'y', 'z'], "0": ["0", ]}
    outputs = [[], ]
    for phn in phoneNumber:
        n = len(outputs)
        temp = []
        for i in range(n):
            arr = outputs[i]
            dic = phone_dictionary[phn]
            for char in dic:
                ele = arr + [char]
                temp.append(ele)
        outputs = temp[:]
    print(outputs)
    results = []
    for i in range(len(outputs)):
        results.append("".join(outputs[i]))
    return results


phone = "002"
print(phoneNumberMnemonics(phone))
