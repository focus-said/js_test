"""
merge dict

"""
from copy import deepcopy


def merge_dict(source_dict, update_dict):
    if not isinstance(source_dict, dict) or not isinstance(update_dict, dict):
        raise TypeError
    return merge_func(source_dict, update_dict)


def merge_func(source_dict, update_dict):
    if not isinstance(source_dict, dict):
        return deepcopy(update_dict)
    for k in update_dict.keys():
        if k in source_dict:
            if isinstance(update_dict[k], dict):
                source_dict[k] = merge_func(source_dict[k], update_dict[k])
            else:
                source_dict[k] = deepcopy(update_dict[k])
        else:
            source_dict[k] = deepcopy(update_dict[k])
    return source_dict


if __name__ == '__main__':
    source_dict = {'key0': 'a',
                   'key1': 'b',
                   'key2': {
                       'inner_key0': 'c',
                       'inner_key1': 'd'
                   }}
    update_dict = {'key1': 'x',
                   'key2': {
                       'inner_key0': 'y'
                   }}

    # source_dict = {'a': [1, 2, 3]}
    # update_dict = {'a': {'b': source_dict}}
    # source_dict = []
    # update_dict = 2
    result = merge_dict(source_dict, update_dict)

    print(result)
