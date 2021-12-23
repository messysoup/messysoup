def global_args(accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    
    global_args = ""
    
    args = {
        'accesskey': accesskey,
        'class': class_,
        'contenteditable': contenteditable,
        f'data-{data_key}': data_value,
        'dir': dir_,
        'draggable': draggable,
        'hidden': hidden,
        'id': id_,
        'lang': lang,
        'spellcheck': spellcheck,
        'style': style,
        'tabindex': tabindex,
        'title': title,
        'translate': translate
    }

    for key, value in args.items():
        if value.strip() != "":
            global_args += f"{key}={str(value)} "

    return global_args


def tag_specific_attibutes(args: dict):

    specific_args = ""

    for key, value in args.items():
        if value != "":
            specific_args += f"{key}={str(value)} "

    return specific_args