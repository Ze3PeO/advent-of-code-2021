def p1(inp):
    count = 0
    for line in inp:
        split = line.split("|")
        sig_pattern = split[0].strip().split(" ")
        digits = split[1].strip().split(" ")
        print(sig_pattern, digits)
        for digit in digits:
            # anzahl der segmente die die zahlen 1, 4, 7, 8 brauchen
            if len(digit) in [2, 4, 3, 7]:
                count += 1

    return count


def p2(inp):
    # aaaa
    #b    c
    #b    c
    # dddd
    #e    f
    #e    f
    # gggg
    #1, 4, 7, 8 nutzen

    #segment a:     ist die differenz von den signalen für 7 und 1
    #segment c, f:  kandidaten für c und f sind dann auch bekannt
    #               dann jedes signal durch gehen und zählen wie oft der kandidat bei den signalen der länge 6 vorkommt
    #               der kandidat der 3 mal vorkommt ist segment f und der der 2 mal vorkommt segment c
    #segment b, d:  ähnliche vorgehensweise, wenn man die signale nimmt die man bekommt
    #               wenn man die bekannten segmente von 4 abzieht
    #               hat man kandidaten für b und d. d kommt 3 mal vor und b 1 mal (bei signalen mit länge 5)
    #segment e, g:  bei signalen mit länge 5 gucken. signale vpn bekannten segmenten von 8. e kommt 1 mal vor.
    #               g kommt 3 mal vor

    #Voila

    return -1


with open('../../input/week2/day8.txt') as file:
    inp = file.readlines()

    print('part 1: ' + str(p1(inp)))
    print('part 2: ' + str(p2(inp)))
