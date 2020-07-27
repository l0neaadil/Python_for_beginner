def emo_cvt(message):
    words = message.split(' ')
    emojis = {
        ":(": '😃',
        ":)": '😁',
        ":()": "😅"
    }
    output = ''
    for word in words:
        output = output + ' ' + emojis.get(word, word)
    return output


message = input('--->')
# print(emo_cvt(message))
result = emo_cvt(message)
print(result)



