from ..attributes import *
from copy import deepcopy
import messysoup.table.table_helpers as tb

def create_table(table: list, has_headers: bool=True, has_footers:bool =True, headers:list =[], footers:list =[], return_html: bool=True):
    return tb.create_table(table, has_headers, has_footers, headers, footers, return_html)

def add_all_table_attributes(table: str, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):

    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    atts = [
        '<table',
        '<thead',
        '<th',
        '<tbody',
        '<tr',
        '<td',
        '<tfoot'
    ]

    result = deepcopy(table)

    for i in atts:
        result = result.replace(i, i + g_args)


    return result

def add_table_attributes(table: str, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):

    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    return table.replace("<table", f"<table {g_args}")

def add_trow_attrinutes(table: str, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):

    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    return table.replace("<tr", f"<tr {g_args}")


def add_tcell_attributes(table: str, colspan: str="", header: str="", rowspan: str="",
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'colspan': colspan,
        'header': header,
        'rowspan': rowspan
    }

    final_args = tag_specific_attibutes(args)

    return table.replace("<td", f"<td {final_args} {global_args}")

def add_theader_attributes(table: str, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):

    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    return table.replace("<thead", f"<thead {g_args}")

def add_th_attributes(table, abbr: str="", colspan: str="", headers: str="", rowspan: str="", scope: str="",                             ## End of tag specific arguements
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):

    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'abbr': abbr,
        'colspan': colspan,
        'headers': headers,
        'rowspan': rowspan,
        'scope': scope
    }

    final_args = tag_specific_attibutes(args)
      
    return table.replace("<th", f"<th {final_args} {tag_specific_attibutes}")

def add_tbody_attributes(table: str, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):

    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    return table.replace("<tbody", f"<tbody {g_args}")

def add_tfooter_attributes(table: str, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):

    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    return table.replace("<tfoot", f"<tfoot {g_args}")
