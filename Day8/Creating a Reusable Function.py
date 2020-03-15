def EmojiConverter(message):
    words = message.split(' ')  # finds the words which is separated by a space
    emojis = {
        ":)": "😀",  # For Happy
        ":(": "😕"  # For Sad
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">>")
print(EmojiConverter(message))