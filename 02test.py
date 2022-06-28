"""
电话排列组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
"""

num_map = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'v', 'z']
}


def func(num):
    result = []
    head_count = 0
    while True:
        result = pstr(result, num_map[num[head_count]])
        head_count += 1
        if head_count == len(num):
            break
    return result


def pstr(list_strs, strs):
    """
    :param list_strs: list is not null
    :param strs: str is not null
    :return:
    """
    tmp_res = []
    for end in strs:
        for head in list_strs:
            tmp_res.append(str(head) + str(end))
        if not list_strs:
            return list(strs)
    return tmp_res


if __name__ == '__main__':
    import random
    while True:
        rnum = random.randint(20000, 100000)
        if '0' in str(rnum) or '1' in str(rnum):
            continue
        break
    print(rnum)
    rnum = 23
    a = func(str(rnum))
    print(len(a))
    print(a)


