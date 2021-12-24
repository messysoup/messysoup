# MessySoup

## What is it?
`MessySoup` is a python wrapper for html elements.  While still a ways away, the main goal is to be able to build a wesbite straight from python, both front and backend.  `MessySoup` is similiar to other frontend frameworks and libraries in that it allows you to build reusable blocks of code instead of having to define them in each webpage.

## What are the limitations?

### Interactivity
Currently, you still have to write all interactivity in javascript or WASM (web assembly).  However, I am keeping a sharp eye on the pyodide development.  There are a number of issues open on their github page aiming to streamline some of the import methodology which look promising.

One of the reasons pyodide hasn't been integrated with this project is that the process to get custom packages loaded in the virtual document is non-intuitive for most python devs as you first need to build a python wheel before installing it with mircopip and being able to use it.  That build could be added to this project, but we'll wait and see what direction the pyodide team goes in first.

### Events
Due to the sheer number of events available, it doesn't make sense to add each event as an arguement for every element.  For now, all events will need to be handled in JS or using the pyodide js bindings.

### File Format
Once you write your elements to disk in a file, you will notice the file is not formatted properly.  This is intentional.  To fix in VS Code, simply right click on the file and click `format document`

## How do I use it?

To get started, use `pip install messysoup`.  This library is mostly funciton based, where each html tag has it's own funciton.  In cases where an html tag or attribute name clashes with a built in function or reserved word, such as `open` and `dir`, an underscore is added to the end of the python equivalent.  Thus, `open` become `open_` and `dir` becomes `dir_`.

Each python tag has three main types of attibutes:  
1.  The content (with the exeptoin of self closing tags such as `br`).
2.  Tag specific attributes, such as `href` for `a`.
3.  Global attributes (with the exception of some tags such as `br`).

The below example uses two common tags, a paragraph and a hyperlink.  One makes use the global tags, and one makes use non-global tags.
```
from messysoup import p

content = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Aliquam sapien ligula, finibus sed ullamcorper vitae, dignissim ac turpis. " 
        "Nulla et consequat felis, vel aliquet libero. Fusce dolor nibh, sodales ut egestas eget, semper at sem. " 
        "Pellentesque sit amet massa tincidunt, consectetur purus id, molestie arcu. " 
        "Fusce in odio quis enim pulvinar condimentum. " 
        "Praesent dictum scelerisque ornare. " 
        "Morbi eget nisi ac lacus ullamcorper pharetra ut a ligula. " 
        "Aliquam porttitor commodo magna, in malesuada elit sagittis ac.")

my_paragraph = p(content=content, id='lorem-ipsum')


my_link = a("The text of the hyperlink", href="https://www.github.com")
```  

In order to create a document out of it, add it to the `MessySoup` class.

```
from messysoup import MessySoup, p


document = MessySoup("filename")

my_paragraph = p("Contents of the paragraph")

document.add(my_paragraph)

document.write_file()
```

## Creating Tables

There is also a built in way to create html tables from python datastructures.  Currently supported structures:

- list of list
- list of dictionaries
- dictionary
- pandas df.  

To do so, simply pass your structure to `create_table()`.  Currenlty all tables will be returned with headers and footers.  If a footer is not passed in separately, the last index will be used.  If headers are not passed in seperately, the following will be used:

- Pandas df: The columns headers.
- Dictionary: The keys.
- List of lists: Index 0 of the parent list.

This will create a basic html table where all tags will be lacking attributes.  To add attributes to the tags, use any combination of the below functions; they return a modified copy of the original table.  `add_all_table_attributes()` will add the specified attributes to all tags, whereas all the others will add them to the specific tag.

- `add_all_table_attributes()`
- `add_table_attributes()`
- `add_trow_attributes()`
- `add_tcell_attributes()`
- `add_theader_attributes()`
- `add_th_attributes()`
- `add_tbody_attributes()`
- `add_tfooter_attributes()`