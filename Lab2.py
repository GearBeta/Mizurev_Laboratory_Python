def find_common_participants(stroke1, stroke2, splitter=','):
    list1 = stroke1.split(splitter)
    list2 = stroke2.split(splitter)
    return sorted(list(set(list1).intersection(list2)))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


participants = find_common_participants(participants_first_group, participants_second_group, '|')
print('Общие участники = ', participants)