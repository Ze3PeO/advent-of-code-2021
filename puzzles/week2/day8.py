def p1(inp):
    count = 0
    for line in inp:
        signals, digits = line.split("|")
        digits = digits.strip().split(" ")
        for digit in digits:
            if len(digit) in [2, 4, 3, 7]:
                count += 1

    return count


def p2(inp):
    result = 0

    '''
    #-------------------------------------------------------------------------------
    # Eigener Lösungsansatz:
    # (Funktioniert leider nicht wirklich)
    #-------------------------------------------------------------------------------
    solution_dict = {
        0: ['a', 'b', 'c', 'e', 'f', 'g'],
        1: ['c', 'f'],
        2: ['a', 'c', 'd', 'e', 'g'],
        3: ['a', 'c', 'd', 'f', 'g'],
        4: ['b', 'c', 'd', 'f'],
        5: ['a', 'b', 'd', 'f', 'g'],
        6: ['a', 'b', 'd', 'e', 'f', 'g'],
        7: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        8: ['a', 'b', 'c', 'd', 'f', 'g']
    }
    
    for line in inp:
        split = line.split("|")
        sig_pattern = split[0].strip().split(" ")
        digits = split[1].strip().split(" ")
        len_dict = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
        seg_x_wired_to_y = {}
        for pattern in sig_pattern:
            len_dict[len(pattern)].append(list(pattern))
        
        #segment a:     ist die differenz von den signalen für 7 und 1
        seg_x_wired_to_y['a'] = list(set(len_dict[3][0]) - set(len_dict[2][0]))[0]
        
        #segment c, f:  kandidaten für c und f sind dann auch bekannt
        #               dann jedes signal durch gehen und zählen wie oft der kandidat bei den signalen der länge 6 vorkommt
        #               der kandidat der 3 mal vorkommt ist segment f und der der 2 mal vorkommt segment c
        
        seg_c_f_candidates = len_dict[2][0]
        count_one = 0
        count_two = 0
        for pattern in len_dict[6]:
            if seg_c_f_candidates[0] in pattern:
                count_one += 1
            if seg_c_f_candidates[1] in pattern:
                count_two += 1
        if count_one > count_two:
            seg_x_wired_to_y['c'] = seg_c_f_candidates[1]
            seg_x_wired_to_y['f'] = seg_c_f_candidates[0]
        else:
            seg_x_wired_to_y['c'] = seg_c_f_candidates[0]
            seg_x_wired_to_y['f'] = seg_c_f_candidates[1]
    
        #segment b, d:  ähnliche vorgehensweise, wenn man die signale nimmt die man bekommt
        #               wenn man die bekannten segmente von 4 abzieht
        #               hat man kandidaten für b und d. d kommt 3 mal vor und b 1 mal (bei signalen mit länge 5)
        
        seg_b_d_candidates = list(set(len_dict[4][0]) - set(len_dict[2][0]))
        count_one = 0
        count_two = 0
        for pattern in len_dict[5]:
            if seg_b_d_candidates[0] in pattern:
                count_one += 1
            if seg_b_d_candidates[1] in pattern:
                count_two += 1
        if count_one > count_two:
            seg_x_wired_to_y['b'] = seg_b_d_candidates[1]
            seg_x_wired_to_y['d'] = seg_b_d_candidates[0]
        else:
            seg_x_wired_to_y['b'] = seg_b_d_candidates[0]
            seg_x_wired_to_y['d'] = seg_b_d_candidates[1]
    
        # segment e, g:  bei signalen mit länge 5 gucken. signale vpn bekannten segmenten von 8. e kommt 1 mal vor.
        #               g kommt 3 mal vor
        
        known_signals = [seg_x_wired_to_y['a'], seg_x_wired_to_y['b'], seg_x_wired_to_y['c'], seg_x_wired_to_y['d'], seg_x_wired_to_y['f']]
        seg_e_g_candidates = list(set(len_dict[7][0]) - set(known_signals))
        count_one = 0
        count_two = 0
        for pattern in len_dict[5]:
            if seg_e_g_candidates[0] in pattern:
                count_one += 1
            if seg_e_g_candidates[1] in pattern:
                count_two += 1
        if count_one > count_two:
            seg_x_wired_to_y['e'] = seg_e_g_candidates[1]
            seg_x_wired_to_y['g'] = seg_e_g_candidates[0]
        else:
            seg_x_wired_to_y['e'] = seg_e_g_candidates[0]
            seg_x_wired_to_y['g'] = seg_e_g_candidates[1]
        inv_dict = {v: k for k, v in seg_x_wired_to_y.items()}
    
        # compute result
        number = ''
        counter = 0
        for digit in digits:
            decoded = ''
            for letter in digit:
                decoded += inv_dict[letter]
            print(decoded)
            l1 = list(decoded)
            l1.sort()
            for key, value in solution_dict.items():
                print(value, l1)
                if value == l1:
                    counter += 1
                    number += str(key)
        result += int(number)
    '''

    '''
    #-------------------------------------------------------------------------------------------------
    # Mögliche Lösung aus dem Internet:
    # (Disclaimer: Der zweite Part wurde nicht abgegeben, weil das wäre nicht die feine englische Art)
    #-------------------------------------------------------------------------------------------------
    
    for line in inp:
        signals, mysteries = line.split("|")
        signals = signals.strip().split(" ")
        mysteries = mysteries.strip().split(" ")
        digits = {}
        counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
        
        # 1, 4, 7, 8 können anhand der Länge herausgefunden werden
        for signal in signals:
            for char in signal:
                counts[char] += 1
            length = len(signal)
            if length == 2:
                digits[1] = set(signal)
            if length == 3:
                digits[7] = set(signal)
            if length == 4:
                digits[4] = set(signal)
            if length == 7:
                digits[8] = set(signal)
        
        # Oberes Segment: Die Differenz von den Signalen für 7 und 1
        seg_top = (digits[7] - digits[1]).pop()

        # Rechstliche Segmente können anhand des Vorkommens von Buchstaben bestimmt werden
        for char, count in counts.items():
            if count == 4:
                seg_bl = char
            elif count == 6:
                seg_ul = char
            elif count == 7:
                if char in digits[4]:
                    seg_mid = char
                else:
                    seg_bot = char
            elif count == 8 and char != seg_top:
                seg_ur = char
            elif count == 9:
                seg_br = char
        digits[0] = {seg_top, seg_ul, seg_ur, seg_bl, seg_br, seg_bot}
        digits[2] = {seg_top, seg_ur, seg_mid, seg_bl, seg_bot}
        digits[3] = {seg_top, seg_ur, seg_mid, seg_br, seg_bot}
        digits[5] = {seg_top, seg_ul, seg_mid, seg_br, seg_bot}
        digits[6] = {seg_top, seg_ul, seg_mid, seg_bl, seg_br, seg_bot}
        digits[9] = {seg_top, seg_ul, seg_ur, seg_mid, seg_br, seg_bot}

        number = ''
        for mystery in mysteries:
            number += [str(key) for key, value in digits.items() if value == set(mystery)][0]
        result += int(number)
    '''

    return result


with open('../../input/week2/day8.txt') as file:
    inp = file.readlines()

    print('part 1: ' + str(p1(inp)))
    print('part 2: ' + str(p2(inp)))
