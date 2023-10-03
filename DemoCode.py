def capitalize_sentence(sentence):
    # Ensure the sentence is not empty
    if not sentence:
        return sentence

    # Capitalize the first letter of the sentence and convert the rest to lowercase
    capitalized_sentence = sentence[0].upper() + sentence[1:].lower()

    return capitalized_sentence


def solution(sentence):
    sentence = sentence.replace(".", "")
    words = sentence.split()
    dic = {}
    for word in words:
        n = len(word)
        try:
            dic[n].append(word)
        except:
            dic[n] = [word, ]
    keys = list(dic.keys())
    keys.sort()
    output = ""
    for k in keys:
        temp = " ".join(dic[k])
        output = output + temp + " "
    output = capitalize_sentence(output)
    output = output.strip() + "."
    return output


print(solution("The soldier decided to desert his dessert in the desert."))
