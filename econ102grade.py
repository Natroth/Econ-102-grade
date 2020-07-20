def econGrade(ps2, final):
    ps1 = 48.5
    mid = 80

    psAver = max([ps1, ps2])

    option1 = (.35 * psAver) + (.65 * final)  #New Grading Scheme
    option2 = (.25 * psAver) + (.35 * mid) + (.4 * final)  #Old Grading Sheme

    array = [option1, option2]

    letter = max(array)
    print(letter)

    if option1 > option2:
        print("Used new grading scheme")
    else:
        print("Used old grading scheme")

    print(f'option 1: {option1}')
    print(f'option 2: {option2}')

    if letter >= 90:
        return "A"
    elif letter >= 85:
        return "A-"
    elif letter >= 80:
        return "B+"
    elif letter >= 75:
        return "B"
    elif letter >= 70:
        return "B-"


print(econGrade(90, 85))
