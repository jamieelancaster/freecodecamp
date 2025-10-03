def is_spam(number):
    number = number.replace("(", "")
    number = number.replace(")", "")
    number = number.replace("-", " ")
    number = number.replace("+", "")

    x = 0
    character = ""
    for i in range(len(number)):
        if number[i] == " ":
            continue
        if number[i] == character:
            x += 1

        else:
            x = 0
        character = number[i]
        if x == 3:
            return True

    number = number.split(" ")

    if len(number[0]) > 2 or number[0][0] != "0":
        return True

    if int(number[1]) > 900 or int(number[1]) < 200:
        return True

    if str(int(number[2][0]) + int(number[2][1]) + int(number[2][2])) in number[3]:
        return True

    return False
