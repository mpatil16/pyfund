def is_member(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

if __name__ == '__main__':
    print(is_member([1, 2, 4, 5], [2, 4, 6, 7]))
    print(is_member([1, 9, 5, 8], [2, 4, 6, 7]))
