from solution_utils import HashedLinkedList


def check_hashed_linked_list_init(lst, expect_success, circular):
    message = None
    try:
        hashed_list = HashedLinkedList(lst, circular)
        message = 'SUCCESS'
        node = hashed_list.start
        index = 0
        while(node != None and not (node == hashed_list.start and index != 0)):
            if (lst[index] != node.value and expect_success):
                message = f'FAIL: Expected {node.value} to be {lst[index]}'
                break
            node = node.next
            index += 1
        if not expect_success and message == 'SUCCESS':
            message = 'FAIL: Construction was successful.'
    except ValueError as err:
        if (expect_success):
            message = f'FAIL: ValueError: {err}'
        else:
            message = f'SUCCESS: ValueError: {err}'
    return message


def check_hashed_linked_list_to_list(lst, expect_success, circular):
    message = None
    try:
        hashed_list = HashedLinkedList(lst, circular)
        to_list = hashed_list.to_list()
        if (to_list != lst and expect_success):
            message = f'FAIL: Expected: {lst}. Actual: {to_list}'
        elif (expect_success):
            message = 'SUCCESS'
        else:
            message = 'FAIL: to_list was successful.'
    except Exception as err:
        message = f'FAIL: Exception: {err}'
    return message


def check_hashed_linked_list_extract_correct(lst, circular, expected_extract, expected_left_behind, from_value, count):
    message = None
    try:
        hashed_list = HashedLinkedList(lst, circular)
        extract = hashed_list.extract(from_value, count)
        if (expected_extract == extract):
            to_list = hashed_list.to_list()
            if (expected_left_behind == to_list):
                message = 'SUCCESS'
            else:
                message = f'FAIL: Expected left over: {expected_left_behind}, Actual: {to_list}'
        else:
            message = f'FAIL: Expected extract: {expected_extract}, Actual: {extract}'
    except Exception as err:
        message = f'FAIL: Exception: {err.with_traceback()}'
    return message

def check_hashed_linked_list_insert_correct(lst, circular, expected_list, after_value, additional):
    message = None
    try:
        hashed_list = HashedLinkedList(lst, circular)
        hashed_list.insert(after_value, additional)
        to_list = hashed_list.to_list()
        if (expected_list == to_list):
            message = 'SUCCESS'
        else:
            message = f'FAIL: Expected {expected_list}, Actual: {to_list}'
    except Exception as err:
        message = f'FAIL: Exception: {err.with_traceback()}'
    return message

print(f'HashedLinkedList')
print(f'  __init__ by list')
test_cases = [
    ([1], True, False), ([1, 2, 3, 4, 5], True,
                         False), ([1, 2, 3, 3, 4, 5], False, False),
    ([1], True, True), ([1, 2, 3, 4, 5], True,
                        True), ([1, 2, 3, 3, 4, 5], False, True),
]
for test in test_cases:
    print(f"    {test[0]} ({'Circular' if test[2] else 'List'}): {check_hashed_linked_list_init(test[0], test[1], test[2])}")

print(f' to_list')
test_cases = [([1], True, False), ([1, 2, 3, 4, 5], True, False),
              ([1], True, True), ([1, 2, 3, 4, 5], True, True)]
for test in test_cases:
    print(f"    {test[0]} ({'Circular' if test[2] else 'List'}): {check_hashed_linked_list_to_list(test[0], test[1], test[2])}")

print(f' extract')
test_cases = [([1, 2], False, [1], [2], 1, 1), ([1, 2], False, [2], [1], 2, 1), ([1, 2, 3, 4, 5], False, [2, 3, 4], [1, 5], 2, 3),
              ([1, 2], True, [1], [2], 1, 1), ([1, 2], True, [2], [1], 2, 1), ([1, 2, 3, 4, 5], True, [2, 3, 4], [1, 5], 2, 3),
              ([1, 2, 3, 4, 5], True, [4, 5, 1, 2], [3], 4, 4), ([9,3,2,7,8,4,6,1,5], True, [1,5,9], [3,2,7,8,4,6], 1, 3)]
for test in test_cases:
    print(f"    {test[0]} from {test[4]} ({'Circular' if test[1] else 'List'}): {check_hashed_linked_list_extract_correct(test[0], test[1], test[2], test[3], test[4], test[5])}")

print(f' insert')
test_cases = [([1, 2], False, [1,2,3,4,5], 2, [3,4,5]), ([1,5], False, [1,2,3,4,5], 1, [2,3,4]), ([1, 2], True, [1,2,3,4,5], 2, [3,4,5]), ([1,5], True, [1,2,3,4,5], 1, [2,3,4])]
for test in test_cases:
    print(f"    {test[0]} insert {test[4]} at {test[3]} ({'Circular' if test[1] else 'List'}): {check_hashed_linked_list_insert_correct(test[0], test[1], test[2], test[3], test[4])}")