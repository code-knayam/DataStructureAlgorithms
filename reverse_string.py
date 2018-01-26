def reverse_string(sentence):
    # sentence = sentence.split(" ")
    # for index in range(len(sentence)):
    #     if len(sentence[index])>4:            
    #         sentence[index] = sentence[index][::-1]
    # return " ".join(sentence)

    return " ".join( [word[::-1] if len(word)>4 else word for word in sentence.split(" ") ])

print(reverse_string("Hey Welcome"))