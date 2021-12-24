
l = [1, 2, 1, 100, 3, 5, 0]

def get_max_item(list_int):
    max_item = []
    max = 0
    for item in list_int:
        # print(max)
        if item > max:
            max = item
            max_item.append(max)
    return max_item

print(get_max_item(l))