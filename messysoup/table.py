import pandas as pd
from .table_helpers import table, tbody, thead, tfoot, th, tr, td
from .attributes import *
from typing import Union
from copy import deepcopy

def table_from_data_frame(table: pd.DataFrame):
    data = table.iloc[:-2].values.lolist()
    headers = table.columns.values.tolist()
    footers = table.iloc[-1].values.tolist()

    return data, headers, footers


def table_from_lists(table: list, headers: list, footers: list):
    data_ = []
    headers_ = []
    footers_ = []

    ## TODO: Look into checking length of headers and footers against length of data.
    if len(headers) > 0:
        headers_ = headers

    if len(footers) > 0:
        footers_ = footers

    if len(headers) == 0 and len(footers) == 0:
        data_ = table[1:-1]
        headers_ = table[0]
        footers_ = table[-1]

    return data_, headers_, footers_,


def table_from_dict(table: list, footers: dict):
    data_dict = {}
    data_ = []
    headers_ = []
    footers_ = []

    ## This will take the dictionary and put it into a nested list
    ## Rows and columns are swapped for the moment

    if type(table) == dict:
        data_dict = deepcopy(table)

        if len(footers) > 0:
            for key, value in footers.items():
                data_dict[key].append(value)

    else:        
        for i in table:
            for key, value in i.items():
                if key in data_dict.keys():
                    data_dict[key].append(value)
                else:
                    data_dict[key] = [value]

        if len(footers) > 0:
            for key, value in footers.items():
                data_dict[key].append(value)


    for key, value in data_dict.items():
        headers_.append(key)
        temp_list = []
        for i in value:
            temp_list.append(i)
        data_.append(temp_list)



    ## Transform the 2d dataset as the rows and columns are currently swapped.
    data_ = [list(x) for x in zip(*data_)]

    footers_ = data_[-1]
    data_ = data_[:-1]

    print("Data:", data_)
    print("Headers:", headers_)
    print("Footers_:", footers_)
    return data_, headers_, footers_

## TODO: Implement this portion, the rest is functioning code.
def create_html_table(data: list, headers: list, footers: list):

    table_headers = thead(
        "".join([th(i) for i in headers])
    )

    table_data = ""

    for row in data:
        table_data += tr(
                "".join([td(i) for i in row])
            )
        

    table_data = tbody(table_data)

    table_footers = tfoot(
        tr(
            "".join([td(i) for i in footers])
        )
    )

    return table("".join([table_headers, table_data, table_footers]))

##TODO: Currently footers and headers are always generated.  Allow it so that footers aren't a required return.
def create_table(table: Union[list, dict], has_headers: bool=True, has_footers:bool =True, headers:list =[], footers: Union[list, dict] =[]):
    """
    If pandas df, must have headers and footers in the same dataframe.
    Nested lists can have seperate headers and footers.
    If passing in a list of dictionaries, the keys will become the headers. The
    last index will default to footers unless a list of footers is provided.
    `has_headers`: `True` headers are included in the table.
    `has_footers`: `True` footers are included in the table.
    """
    data_ = []
    headers_ = []
    footers_ = []
    pandas_df = False

    ## Checks to ensure that if headers are included in the dataset, additional
    ## headers are not being provided.
    if has_headers and len(headers) > 0:
        raise AttributeError
    if has_footers and len(footers) > 0:
        raise AttributeError

    ## Checks to ensure if headers and footers are provided, they are lists
    if type(headers) != list:
        raise AttributeError
    if type(footers) != list and type(footers) != dict:
        raise AttributeError

    # Check for pandas df.  If it is, create data, headers, and footers.
    try:
        import pandas as pd
        if isinstance(table, pd.DataFrame):
            pandas_df = True
            data_, headers_, footers_ = table_from_data_frame()
    except:
        pass


    ## Checks if list of lists, or list of dictionaries.
    if pandas_df == False and type(table) == dict:
        data_, headers_, footers_ = table_from_dict(table, footers)
    elif pandas_df == False and type(table[0]) == dict:
        data_, headers_, footers_ = table_from_dict(table, footers)
    elif pandas_df == False and type(table[0]) == list:
        data_, headers_, footers_ = table_from_lists(table, headers, footers)


    # result = create_html_table(data_, headers_, footers_)

    return data_, headers_, footers_
