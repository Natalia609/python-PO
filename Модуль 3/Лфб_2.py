# TODO Напишите функцию find_common_participants

def splitting(s_1, s_2, a=","):
    s_1_rem = s_1.split(a)
    s_2_rem = s_2.split(a)
    surr = []
    for i in range(0,len(s_1_rem)):
        for j  in range(0,len(s_2_rem)):
            if s_1_rem[i] == s_2_rem[j]:
                surr.append(s_1_rem[i])
    surr.sort()
    return surr

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(splitting(participants_first_group, participants_second_group, "|"))
# TODO Провеьте работу функции с разделителем отличным от запятой
