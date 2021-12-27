from messysoup.table.table import create_table
import pytest

def test_create_table_list_of_dicts():
    mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]

    data, headers, footers = create_table(mydict, has_footers = False, footers={'a': 10000, 'b': 20000, 'c': 30000, 'd': 40000}, return_html=False)

    assert data == [[1, 2, 3, 4], [100, 200, 300, 400], [1000, 2000, 3000, 4000]]
    assert headers == ['a', 'b', 'c', 'd']
    assert footers == [10000, 20000, 30000, 40000]

def test_create_table_single_dict():
    mydict = {'a': [1, 10, 100, 1000], 
            'b': [2, 20, 200, 2000], 
            'c': [3, 30, 300, 3000], 
            'd': [4, 40, 400, 4000]}
    
    data, headers, footers = create_table(mydict, has_footers=False, footers={'a': 10000, 'b': 20000, 'c': 30000, 'd': 40000}, return_html=False)

    assert data == [[1, 2, 3, 4], [10, 20, 30, 40], [100, 200, 300, 400], [1000, 2000, 3000, 4000]]
    assert headers == ['a', 'b', 'c', 'd']
    assert footers == [10000, 20000, 30000, 40000]
