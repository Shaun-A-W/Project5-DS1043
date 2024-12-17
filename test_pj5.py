"""

This file acts as a testing ground for the personal library
completed as a part of Project 5 for DS-1043. It is highly likely
that the test functions for count and searching in files
will not work on unique machines. Consider running manually on own files.
These two tests omitted by default.

Completed alongside the personal module by Shaun W.

"""

import SWpj5 as ds
import tempfile
import os
_TEST = True

def test_prime():
    assert ds.p_factor(5) == [1,5]
    assert ds.p_factor(16) == [2,2,2,2]
    assert ds.p_factor(15) == [3,5]
    assert ds.p_factor(102) == [2, 3, 17]
    try: ds.p_factor(-11)
    except ValueError: assert True



def test_nest():
    assert ds.no_nest([1,'far',[6,8,23,'close'],'one']) == [1,'far',6,8,23,'close','one']
    assert ds.no_nest([]) == []
    assert ds.no_nest([1,[]]) == [1]
    try: ds.no_nest([1,{2:3}])
    except TypeError: assert True



def test_table():
    # table testing start
    data_l = [['abcd', 1234567, 100, True], [33, False, 'alphabeta', 231311223.333334]]
    data_d = [{'a': 233, 'two': 'c', 'd': False, 'four': 12222222222222},
              {'one': 12.399, 'two': '3', 'three': True, 'four': False}]
    header = ['a', 'two', 'three', 'four', ]

    data_wide = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13]]
    header_wide = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
                   'thirteen']

    ds.view_table(header, data_l, file=None)
    print("\n")
    ds.view_table(header, data_d, file=None)
    print("\n")
    ds.view_table(header_wide, data_wide, file=None)
    assert ds.max_widths(['alpha', 'beta', 'charlie', 'delta'],
                         [[False, 'one', 'chocolate', 123456789], [1, 2, 3, 4]]) == [5, 4, 9, 8]
    # table testing end



def test_count():

    with tempfile.NamedTemporaryFile(mode='w+t', suffix='txt', dir=os.getcwd()) as temp_file:
        # Write to the temporary file
        temp_file.write("This is some temporary text.\n")
        try:
            assert ds.file_wordcount('temp_file.txt') == 5
        except PermissionError:
            raise PermissionError('Temp file not reachable. Manual test of wordcount required.')
        except FileNotFoundError:
            raise FileNotFoundError('Temp file not found. Manual test of wordcount required.')


def test_search():
    with tempfile.NamedTemporaryFile(mode='w+t', suffix='txt', dir=os.getcwd()) as temp_file:
        # Write to the temporary file
        temp_file.write("This is some temporary text.\n")
        try:
            assert ds.file_search('temp_file.txt', [], False) == {}
        except PermissionError:
            raise PermissionError('Temp file not reachable. Manual test of search required.')
        except FileNotFoundError:
            raise FileNotFoundError('Temp file not found. Manual test of search required.')




if _TEST:
    test_prime()
    test_nest()
    test_table()
    # test_count() # Omitted. Refer to docstring
    # test_search() # Omitted. Refer to docstring
    print('')
    print('**********************')
    print('\n', '| Tests completed. | ', '\n')
    print('**********************')