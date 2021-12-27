from .attributes import *
from copy import deepcopy

class MessyStyles():
    """
    Generates a CSS file.
    """
    def __init__(self, file_name) -> None:
        self.css_file = ""
        self.file_name = file_name
        
    def add_styles(self, style):
        """
        Enter your CSS style in the `style` argument.
        recommend blockquotes for anything larger than one liner.
        """

        self.css_file += style
    
    def write_file(self):
        f = open(f"{self.file_name}.css", "w")
        n = f.write(self.css_file)
        f.close()

class MessySoup():
    """
    An HTML generator.
    Below are a list of global attributes many tags share:
        - `accesskey`
        - `class`
        - `contenteditable`
        - `data-*`
        - `dir`
        - `draggable`
        - `hidden`
        - `id`
        - `lang`
        - `spellcheck`
        - `style`
        - `tabindex`
        - `title`
        - `translate`
    """

    def __init__(self, file_name) -> None:
        self.html_file = ""
        self.file_name = file_name

    def add(self, element):
        self.html_file += element

    def write_file(self, dir_: str=""):
        """
        Provide a directory to write the file to. An empty directory will
        deftault to the working directory
        """
        f = open(f"{dir_}{self.file_name}.html", "w")
        n = f.write(self.html_file)
        f.close()


#########################################################################################
#########################################################################################
#--------------------------------Start of HTML Tags-------------------------------------#
#########################################################################################
#########################################################################################




def a(text, href: str="", download: str="", hreflang: str="", media: str="", ping: str="",
                referrerpolicy: str="", ref: str="", target: str="", type_: str="",             ## End of tag specific arguments
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a hyperlink.\n
    `href`: Enter the link as a string\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                        dir_, draggable, hidden, id_, lang, spellcheck, style, 
                        tabindex, title, translate)

    args = {
        'href': href,
        'download': download,
        'hreflang': hreflang,
        'media': media,
        'ping': ping,
        'referrerpolicy': referrerpolicy,
        'ref': ref,
        'target': target,
        'type': type_
    }

    final_args = tag_specific_attibutes(args)

    return f"<a {final_args} {g_args}>{text}</a>\n"

def abbreviation(text, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns an abbreviation.
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                        dir_, draggable, hidden, id_, lang, spellcheck, style, 
                        tabindex, title, translate)

    return f"<abbr {g_args}>{text}</abbr>\n"

def address(text, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns an address.
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                        dir_, draggable, hidden, id_, lang, spellcheck, style, 
                        tabindex, title, translate)

    return f"<address {g_args}>\n{text}</address>\n"

def area(alt: str="", coords: str="", download: str="", href: str="",
            hreflang: str="", media: str="", referrerpolicy: str="", rel: str="",
            shape: str="", target: str="", type_: str="",                                           ## End of tag specific arguments
            accesskey:str ="", class_: str ="", contenteditable: str ="", 
            data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
            hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
            style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns an area.  Must be used inside a map.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                        dir_, draggable, hidden, id_, lang, spellcheck, style, 
                        tabindex, title, translate)

    args = {
        'alt': alt,
        'coords': coords,
        'download': download,
        'href': href,
        'hreflang': hreflang,
        'media': media,
        'referrerpolicy': referrerpolicy,
        'rel': rel,
        'shape': shape,
        'target': target,
        'type': type_
    }

    final_args = tag_specific_attibutes(args)


    return f"<area {final_args} {g_args}>\n"

def article(text, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns an article.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                        dir_, draggable, hidden, id_, lang, spellcheck, style, 
                        tabindex, title, translate)

    return f"<article {g_args}>{text}</article>\n"

def aside(text, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns an `aside`.\n
    `text`: the contents of the aside.\n
"""
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                        dir_, draggable, hidden, id_, lang, spellcheck, style, 
                        tabindex, title, translate)

    return f"<aside {g_args}>{text}</aside>\n"

def audio(contents, autoplay: str="", controls: str="", loop: str="", muted: str="",
                preload: str="", src: str="",                                                       ## End of tag specific attributes
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns an audio elemnt.\n
    `contents`: The contents of the `audio` tag.
    """

    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                        dir_, draggable, hidden, id_, lang, spellcheck, style, 
                        tabindex, title, translate)

    args = {
        'autoplay': autoplay,
        'controls': controls,
        'loop': loop,
        'muted': muted,
        'preload': preload,
        'src': src
    }

    final_args = tag_specific_attibutes(args)


    return f"<audio {final_args} {g_args}>{contents}</audio>\n"

def b(text, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a bold tag.\n
    `text`: Required.  Text in the tag.
    `contents`: The contents to be enboldened.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                        dir_, draggable, hidden, id_, lang, spellcheck, style, 
                        tabindex, title, translate)

    return f"<b {g_args}>{text}</b>\n"

def base(href, target="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Needs to be in the head arguement.\n
    `href`: Required. The default URL\n
    `target`: The default target
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                        dir_, draggable, hidden, id_, lang, spellcheck, style, 
                        tabindex, title, translate)

    return f"<base href={href} {target} {g_args} >\n"

def bdi(text, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a `bdi`\n
    `text`: Required. Text to isolate.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                        dir_, draggable, hidden, id_, lang, spellcheck, style, 
                        tabindex, title, translate)

    return f"<bdi {g_args}>{text}</bdi>\n"

def bdo(text, dir_: str="",accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a `dir` element.\n
    `text`: Required.  Text to alter.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                        dir_, draggable, hidden, id_, lang, spellcheck, style, 
                        tabindex, title, translate)

    args = {
        'dir': dir_
    }

    final_args = tag_specific_attibutes(args)

    return f"<bdo {final_args} {g_args}>{text}</bdo>\n"

def blockquote(text, cite="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a `blockquote`.\n
    `text`: Required. Text to quote.\n
    `cite`: Location cited.\n
"""
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                        dir_, draggable, hidden, id_, lang, spellcheck, style, 
                        tabindex, title, translate)

    return f"<blockquote {cite} {g_args}>{text}</blockquote>\n"

def body(text, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns the body element.\n
    `text`: Required.  Contents of the tag.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
                        
    return f"<body {g_args}>{text}</body>\n"

def br():
    return f"<br>\n"

def button(text, autofocus: str="", disabled: str="", form: str="", formation: str="",
                formenctype: str="", formmethod: str="", formvalidate: str="", formtarget="",
                name: str="", type_: str="", value: str="",                                         ## End of tag specific args
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a button.\n
    `text`: Required.  Contents of the tag.\n
    """    
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    args ={
        'autofocus': autofocus,
        'disabled': disabled,
        'form': form,
        'formation': formation,
        'formenctype': formenctype,
        'formmethod': formmethod,
        'formvalidate': formvalidate,
        'formtarget': formtarget,
        'name': name,
        'type': type_,
        'value': value
    }

    final_args = tag_specific_attibutes(args)
    
    return f"<button {final_args} {g_args}>{text}</button>\n"

def canvas(text, width: str="", height: str="",                                                     ## End of tag specific args
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a `canvas`.
    `text`: Required.  Contents of the tag.\n

    `args`: Specific args for `canvas`, limited to:\n
        - `height`
        - `width`
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'heigh': height,
        'width': width
    }

    final_args = tag_specific_attibutes(args)

    return f"<canvas {final_args} {g_args}>{text}</canvas>\n"

def caption(text, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a `caption`.\n
    `text`: Required.  Contents of the tag.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    return f"<caption {g_args}>{text}</caption>\n"

def cite(text, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a citation.\n
    `text`: Required.  Contents of the tag.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    return f"<cite {g_args}>{text}</cite>\n"

def code(text, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a code fragment.\n
    `text`: Required.  Contents of the tag.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<code {g_args}>{text}</code>\n"

def col(span: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Specifies column properties.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'span': span
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<col {final_args} {g_args} >\n"

def colgroup(contents, span: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Groups columns for formatting.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'span': span
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<colgroup {final_args} {g_args}>{contents}</colgroup>\n"

def data(text, value: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Used to add machine readable translation of the content.\n
    `text`: Required.  The content to be translated.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'value': value
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<data {final_args} {g_args}>{text}</data>\n"

def datalist(contents, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a `datalist` element.\n
    `contents`: Required.  The content of the tag.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<datalist {g_args}>{contents}</datalist>\n"

def dd(text, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Used to describe an item in a desciption list.\n
    `text`: Required.  The content of the tag.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<dd {g_args}>{text}</dd>\n"

def de(text, cite: str="", datetime: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Used in combination with an `ins` tag.  Will cause text to have a strikethrough.\n
    `text`: Required.  The content of the tag.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    args = {
        'cite': cite,
        'datetime': datetime
    }

    final_args = tag_specific_attibutes(args)
    
    return f"<del {final_args} {g_args}>{text}</del>\n"

def details(content, open_: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Used to show or hide additional details.\n
    `contents`: Required.  The content to be translated.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    args = {
        'open': open_
    }

    final_args = tag_specific_attibutes(args)

    return f"<details {final_args} {g_args}>{content}</details>\n"

def dfn(text, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a definition element.\n
    `text`: The text to be defined.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<dfn {g_args}>{text}</dfn>\n"

def dialog(text, open_: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a dialog box.\n
    `text`: The content of the dialog box.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    args = {
        'open': open_
    } 

    final_args = tag_specific_attibutes(args)

    return f"<dialog {final_args} {g_args}>{text}</dialog>\n"

def div(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a `div`.\n
    `content`: The contents of the `div`,\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<div {g_args}>{content}</div>\n"

def dl(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines a description list.\n
    `content`: the content to be defined.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<dl {g_args}>{content}</dl>\n"

def dt(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines an item in a description list.\n
    `content`: Content being defined.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<dt {g_args}>{content}</dt>\n"

def em(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns emphasized text.\n
    `content`: The content to be emphasized.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<em {g_args}>{content}</em>\n"

def fieldset(content, disabled: str="", form: str="", name: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a fieldset.  Used to group like items in a form.\n
    `content`: The items to be grouped together.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'disabled': disabled,
        'form': form,
        'name': name,
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<fieldset {final_args} {g_args}>{content}</fieldset>\n"

def figcaption(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines a caption for a `figure` element.\n
    `content`: The caption.
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<figcaption {g_args}>{content}</figcaption>\n"

def figure(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a self contained conent.\n
    `content`: The content.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<figure {g_args}>{content}</figure>\n"

def footer(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a footer.\n
    `content`: The contents of the footer.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<footer {g_args}>{content}</footer>\n"

def form(content, accept_charset: str="", action: str="", autocomplete: str="",
                enctype: str="", method: str="", name: str="", novalidate: str="",
                rel: str="", target: str="",                                                            ## End of tag specific attributes
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines a form.\n
    `content`: The content of the form.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'accept-charset': accept_charset,
        'action': action,
        'autocomplete': autocomplete,
        'enctpye': enctype,
        'method': method,
        'name': name,
        'novalidate': novalidate,
        'rel': rel,
        'target': target
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<form {final_args} {g_args}>{content}</form>\n"

def h1(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a heading.\n
    `content`: The text of the heading.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<h1 {g_args}>{content}</h1>\n"


def h2(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a heading.\n
    `content`: The text of the heading.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<h2 {g_args}>{content}</h2>\n"
    
def h3(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a heading.\n
    `content`: The text of the heading.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<h3 {g_args}>{content}</h3>\n"
    
def h4(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a heading.\n
    `content`: The text of the heading.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<h4 {g_args}>{content}</h4>\n"
    
def h5(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a heading.\n
    `content`: The text of the heading.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<h5 {g_args}>{content}</h5>\n"
    
def h6(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a heading.\n
    `content`: The text of the heading.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<h6 {g_args}>{content}</h6>\n"

def head(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a head.\n
    `content`: The contents of the `head`.
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<head {g_args}>{content}</head>\n"

def header(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a header.\n
    `content`: The contents of the header.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<header {g_args}>{content}</header>\n"

def hr(accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Used to break up content, returns a horizontal line.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<hr {g_args}>\n"

def html(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines the root of the page, is a container for everything except `doctype`.\n
    `content`: Content of the page.
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<html {g_args}>{content}</html>\n"

def i(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Marks text as italic.\n
    `content`: Content to be italicized.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<i {g_args}>{content}</i>\n"

def ifrmae(content, allow: str="", allowfullscreen: str="", allowpaymentrequest: str="",
                height: str="", loading: str="", name: str="", referrerpolicy: str="",
                sandbox: str="", src: str="", srcdoc: str="", width: str="",                            ## End of tag specific arguements.
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Embeds another document in the main document.\n
    `content`: The other document.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'allow': allow,
        'allowfullscreen': allowfullscreen,
        'allowpaymentrequests': allowpaymentrequest,
        'height': height,
        'loading': loading,
        'name': name,
        'reffererpolicy': referrerpolicy,
        'src': src,
        'srcdoc': srcdoc
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<iframe {final_args} {g_args}>{content}</iframe>\n"

def img(alt: str="", crossorigin: str="", height: str="", ismap: str="", loading: str="",
                longdesc: str="", referrerpolicy: str="", sizes: str="", src: str="",
                srcset: str="", usemap: str="", width: str="",                                              ## End of tag specific arguements.
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Displays an image.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'alt': alt,
        'crossorigin': crossorigin,
        'height': height,
        'ismap': ismap,
        'loading': loading,
        'longdesc': longdesc,
        'referrerpolicy': referrerpolicy,
        'sizes': sizes,
        'src': src,
        'srcset': srcset,
        'usemap': usemap,
        'width': width
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<img {final_args} {g_args}>\n"

def input_(accept: str="", alt: str="", autocomplete: str="", autofocus: str="", checked: str="",
                dirname: str="", disabled: str="", form: str="", formaction: str="", formenctype: str="", 
                formmethod: str="", formnovalidate: str="", formtarget: str="", height: str="", 
                list_: str="", max_: str="", maxlength: str="", min_: str="", minlength: str="", 
                multiple: str="", name: str="", pattern: str="", placeholder: str="", readonly: str="", 
                required: str="", size: str="", src: str="", step: str="", type_: str="", 
                value: str="", width: str="",                                                                           ## End of tag specific arguments 
    
     accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Allows the user to enter input.\n
    """

    args = {
        'accept': accept,
        'alt': alt,
        'autocomplete': autocomplete,
        'autofocus': autofocus,
        'checked': checked,
        'dirname': dirname,
        'disabled': disabled,
        'form': form,
        'formaction': formaction,
        'formenctype': formenctype,
        'formmethod': formmethod,
        'formnovalidate': formnovalidate,
        'formtarget': formtarget,
        'height': height,
        'list': list_,
        'max': max_,
        'maxlength': maxlength,
        'min_': min_,
        'minlength': minlength,
        'multiple': multiple,
        'name': name,
        'pattern': pattern,
        'placeholder': placeholder,
        'readonly': readonly,
        'required': required,
        'size': size,
        'src': src,
        'step': step,
        'type': type_,
        'value': value,
        'width': width
    }
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    final_args = tag_specific_attibutes(args)
      
    return f"<input {final_args} {g_args}>\n"

def ins(content, cite: str="", datetime: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Paired with `del`, returns inserted text.\n
    `content` - Content to be inserted.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'cite': cite,
        'datetime': datetime
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<ins {final_args} {g_args}>{content}</ins>\n"

def kdb(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a visual for keyboard input.\n
    `content`: Returns the keys in question.
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<kdb {g_args}>{content}</kdb>\n"

def label(content, for_: str="", form: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines a label.\n
    `content`: Contents of the label.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'for': for_,
        'form': form
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<label {final_args} {g_args}>{content}</label>\n"

def legend(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines a legend.\n
    `content`: Contents of the legend.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<legend {g_args}>{content}</legend>\n"

def li(content, value: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines a list value.\n
    `content`: Contents of the list value.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'value': value
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<li {final_args} {g_args}>{content}</li>\n"

def link(crossorigin: str="", href: str="", hreflang: str="", media: str="", 
                referrerpolicy: str="", rel: str="", sizes: str="", title_link: str="", 
                type_: str="",                                                                                  ## End of tag specific arguements
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines a link between the current document and an external resource.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'crossorigin': crossorigin,
        'href': href,
        'hreflang': hreflang,
        'media': media,
        'referrerpolicy': referrerpolicy,
        'rel': rel,
        'sizes': sizes,
        'title': title_link,
        'type': type_
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<link {final_args} {g_args}>\n"

def main(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines the main part of the document.\n
    `content`: Contents of the documents.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<main {g_args}>{content}</main>\n"

def map_(content, name: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines an image map.\n
    `content`: Contents of the map.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
    
    args = {
        'name': name
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<map {final_args} {g_args}>{content}</map>\n"

def mark(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines text that should be marked/highlighted.\n
    `content`: Content to be highlighted.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<mark {g_args}>{content}</mark>\n"

def meta(charset: str="", content: str="", http_equiv: str="", name: str="",                                    ##End of tag specific args
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines metadata about the document.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'charset': charset,
        'content': content,
        'http-equiv': http_equiv,
        'name': name
    }
      
    final_args = tag_specific_attibutes(args)

    return f"<meta {final_args} {g_args}>\n"

def meter(content, form: str="", high: str="", low: str="", max_: str="", min_: str="", 
                optimum: str="", value: str="",                                                                             ## End of tag specific arguement

accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines a guage.\n
    `content`: Contents of the meter.
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'form': form,
        'high': high,
        'low': low,
        'max': max_,
        'min': min_,
        'optimum': optimum,
        'value': value
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<meter {final_args} {g_args}>{content}</meter>\n"

def nav(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines a navigation section.\n
    `content`: Content of the navigation.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<nav {g_args}>{content}</nav>\n"

def noscript(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines alternative content to be displayed when scripts
    aren't supported or disabled.\n
    `content`: Content to be displayed.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<noscript {g_args}>{content}</noscript>\n"

def ol(content, reversed_: str="", start: str="", type_: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns an ordered list item.\n
    `content`: Contents of the list item.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'reversed': reversed_,
        'start': start,
        'type': type_,
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<ol {final_args} {g_args}>{content}</ol>\n"

def optgroup(content, disabled: str="", label: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns an option group in a `select` tag.\n
    `content`: The group of optoins.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'disabled': disabled,
        'label': label
    }
       
    final_args = tag_specific_attibutes(args)

    return f"<optgroup {final_args} {g_args}>{content}</optgroup>\n"

def option(content, disabled: str="", label: str="", selected: str="", value: str="",                               ## End of tag specific arguements
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns an option in a `select` tag.\n
    `content`: The option in question.\n
    """ 
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'disabled': disabled,
        'label': label,
        'selected': selected,
        'value': value
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<option {final_args} {g_args}>{content}</option>\n"

def output(content, for_: str="", form: str="", name: str="", accesskey:str ="", 
                class_: str ="", contenteditable: str ="", data_key: str="", 
                data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns the output of a calculation.\n
    `content`: The output.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'for': for_,
        'form': form,
        'name': name
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<output {final_args} {g_args}>{content}</output>\n"

def p(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a paragraph.\n
    `content`: Contents of the paragraph.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<p {g_args}>{content}</p>\n"

def param(name: str="", value: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines the parameters of an object.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'name': name,
        'value': value,
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<param {final_args} {g_args}>\n"

def picture(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a `picture`.  Used as an alternate to `img` when
    multiple picture sizes are available.  Will use the first
    one that matches the viewport.\n
    `content`: The various pictures.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<picture {g_args}>{content}</picture>\n"

def pre(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines preformatted text.\n
    `content`: The preformatted text.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<pre {g_args}>{content}</pre>\n"

def progress(content, max_: str="", value: str="",  accesskey:str ="", class_: str ="", 
                contenteditable: str ="", data_key: str="", data_value: str="", dir_: str="", 
                draggable: str="", hidden: str="", id_: str="", lang: str="",
                spellcheck: str="", style: str="", tabindex: str="", title: str="",
                translate: str=""):
    """
    Defines a progress bar.\n
    `content`: Contents of the progressbar.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'max': max_,
        'value': value
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<progress {final_args} {g_args}>{content}</progress>\n"

def q(content, cite: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines a short quote.\n
    `content`: Quote.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'cite': cite
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<q {final_args} {g_args}>{content}</q>\n"

def rp(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Provides parenthesis around ruby text.\n
    `contents`: The parenthesis.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<rp {g_args}>{content}</rp>\n"

def rt(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Provides an explanation or pronounciation around ruby text.\n
    `contents`: The explanation or pronounciation.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<rt {g_args}>{content}</rt>\n"

def ruby(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Specifies a ruby annotation.\n
    `content`: The annotation.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<ruby {g_args}>{content}</ruby>\n"

def s(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Specifies text that is no longer correct, accurate, or relevant.\n
    `content`: New content.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<s {g_args}>{content}</s>\n"

def samp(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines output from a computer program.\n
    `content`: Content to be displayed.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<samp {g_args}>{content}</samp>\n"

def script(content, async_: str="", crossorigin: str="", defer: str="", integrity: str="", 
                nomodule: str="", referrerpolicy: str="", src: str="", type_: str="",                               ## End of tag specific arguements
                accesskey:str ="", class_: str ="", contenteditable: str ="",  
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines a script to be called.\n
    `content`: The script.\n
    """    
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'async': async_,
        'crossorigin': crossorigin,
        'defer': defer,
        'integrity': integrity,
        'nomodule': nomodule,
        'referrerpolicy': referrerpolicy,
        'src': src,
        'type': type_
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<script {final_args} {g_args}>{content}</script>\n"

def section(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines a section in a document.\n
    `content`: Contents of the sections.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<section {g_args}>{content}</section>\n"

def select(content, autofocus: str="", disabled: str="", form: str="", multiple: str="", 
                name: str="", required: str="", size: str="",                                                       ## End of tag specific arguements

accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Used to create a drop-down list.\n
    `content`: The contents of the list.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'autofocus': autofocus,
        'disabled': disabled,
        'form': form,
        'multiple': multiple,
        'name': name,
        'required': required,
        'size': size
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<select {final_args} {g_args}>{content}</select>\n"

def small(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Used to make small text.\n
    `content`: Content to make small.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<small {g_args}>{content}</small>\n"

def source(media: str="", sizes: str="", src: str="", srcset: str="", type_: str="",                                ## End of tag specific arguements
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Specifies multiple media elements.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'media': media,
        'sizes': sizes,
        'src': src,
        'srcset': srcset,
        'type': type_
    }
      
    final_args = tag_specific_attibutes(args)

    return f"<source {final_args} {g_args}>\n"

def span(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns and inline container.\n
    `content`: The content of the container.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<span {g_args}>{content}</span>\n"

def strong(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Makes text bold.\n
    `content`: Content to make bold.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<strong {g_args}>{content}</strong>\n"

def style(content, media: str="", type_: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Define CSS style for a document.\n
    `content`: CSS styles.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'media': media,
        'type': type_
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<style {final_args} {g_args}>{content}</style>\n"

def sub(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines subscript text.\n
    `content`: Content to be subscripted.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<sub {g_args}>{content}</sub>\n"

def summary(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a summary.\n
    `contents`: Contents of a summary.\n
"""
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<summary {g_args}>{content}</summary>\n"

def sup(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns superscript.\n
    `content`: Contents of the superscript.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<sup {g_args}>{content}</sup>\n"

def svg(content, args=""):
    """
    Returns an `svg` object.\n
    `content`: Contents of the `svg`.\n
    `args`: Args specific to `svg`.
    """

    return f"<svg {args}>{content}</svg>\n"

def table(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a table.\n
    `content`: Contents of the table.\n
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

def template(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Used to hide a container from the user later made visible from a script.\n
    `content`: Content of the template.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<template {g_args}>{content}</template>\n"

def textarea(content, autofocus: str="", cols: str="", disabled: str="", form: str="", 
                maxlength: str="", name: str="", placeholder: str="", readonly: str="", 
                required: str="", rows: str="", wrap: str="",                                                           ## End of tag specific arguements
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a textarea, a multiline input textbox.\n
    `content`: Contents of the `textarea`.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'autofocus': autofocus,
        'cols': cols,
        'disabled': disabled,
        'form': form,
        'maxlength': maxlength,
        'name': name,
        'placeholder': placeholder,
        'readonly': readonly,
        'required': required,
        'rows': rows,
        'wrap': wrap
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<textarea {final_args} {g_args}>{content}</textarea>\n"

def tfoot(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a table footer.\n
    `content`: Contents of the table footer.\n
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
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<thead {g_args}>{content}</thead>\n"

def time(content, datetime: str="", accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines a specific time or datetime.\n
    `content`: The time or datetime.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'datetime': datetime
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<time {final_args} {g_args}>{content}</time>\n"

def title(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines the title of the html document.\n
    `content`: Contents of the title.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<title {g_args}>{content}</title>\n"

def tr(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a table row.\n
    `content`: Contents of the table row.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<tr {g_args}>{content}</tr>\n"

def track(default: str="", kind: str="", label: str="", src: str="", srclang: str="", 
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Specify the track for the audio or video element.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'default': default,
        'kind': kind,
        'label': label,
        'src': src,
        'srclang': srclang
    }

    final_args = tag_specific_attibutes(args)
      
    return f"<track {final_args} {g_args}>\n"

def u(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Underlines text.\n
    `content`: Content to be underlined.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<u {g_args}>{content}</u>\n"

def ul(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Defines an unordered list.\n
    `content`: Contents of the unordered list.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<ul {g_args}>{content}</ul>\n"

def var(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a variable.\n
    `content`: The variable in question.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<var {g_args}>{content}</var>\n"

def video(content, autoplay: str="", controls: str="", height: str="", loop: str="", 
                muted: str="", poster: str="", preload: str="", src: str="", width: str="",                             ## End of tag specific arguements
                accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Returns a video.\n
    `content`: Sources and error text.\n
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)

    args = {
        'autoplay': autoplay,
        'controls': controls,
        'height': height,
        'loop': loop,
        'muted': muted,
        'poster': poster,
        'preload': preload,
        'src': src,
        'width': width
    }
      
    final_args = tag_specific_attibutes(args)
    
    return f"<video {final_args} {g_args}>{content}</video>\n"

def wbr(content, accesskey:str ="", class_: str ="", contenteditable: str ="", 
                data_key: str="", data_value: str="", dir_: str="", draggable: str="", 
                hidden: str="", id_: str="", lang: str="", spellcheck: str="", 
                style: str="", tabindex: str="", title: str="", translate: str=""):
    """
    Specifices a word break opportunity.
    `content`: Contents of the word break`.
    """
    g_args = global_args(accesskey, class_, contenteditable, data_key, data_value, 
                    dir_, draggable, hidden, id_, lang, spellcheck, style, 
                    tabindex, title, translate)
      
    return f"<wbr {g_args}>{content}</wbr>\n"
