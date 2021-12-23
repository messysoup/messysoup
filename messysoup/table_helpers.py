
from .attributes import *

'''
Table tags from messysoup in another file to avoid circular imports
when creating tables.
'''

def table(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a table.\n
    `content`: Contents of the table.\n
    `global_args`: Global attributes shared between HTML elements.
    see class docstring for complete list.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<table {g_args}>{content}</table>\n"

def tbody(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a table body.\n
    `content`: Contents of the table body.\n
    `global_args`: Global attributes shared between HTML elements.
    see class docstring for complete list.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<tbody {g_args}>{content}</tbody>\n"

def td(content, colspan: str="", header: str="", rowspan: str="",
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a data cell in a table.\n
    `content`: Content of the cell.\n
    `global_args`: Global attributes shared between HTML elements.
    see class docstring for complete list.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'colspan': colspan,
        'header': header,
        'rowspan': rowspan
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<td {final_args} {g_args}>{content}</td>\n"



def tfoot(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a table footer.\n
    `content`: Contents of the table footer.\n
    `global_args`: Global attributes shared between HTML elements.
    see class docstring for complete list.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<tfoot {g_args}>{content}</tfoot>\n"

def th(content, abbr: str="", colspan: str="", headers: str="", rowspan: str="", scope: str="",                             ## End of tag specific arguements
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a table header cell.\n
    `content`: Contents of the table header cell.\n
    `global_args`: Global attributes shared between HTML elements.
    see class docstring for complete list.\n
    """
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
      
    return f"<th {final_args} {g_args}>{content}</th>\n"

def thead(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a table header.\n
    `content`: Contents of the table head.\n
    `global_args`: Global attributes shared between HTML elements.
    see class docstring for complete list.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<thead {g_args}>{content}</thead>\n"

def tr(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a table row.\n
    `content`: Contents of the table row.\n
    `global_args`: Global attributes shared between HTML elements.
    see class docstring for complete list.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<tr {g_args}>{content}</tr>\n"
