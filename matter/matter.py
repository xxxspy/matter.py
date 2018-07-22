from tempfile import NamedTemporaryFile
from . import settings
from pscript import py2js
import webbrowser

_NAMESPACES = {}

def add_namespace(name, script):
    '''
    name: 'jquery' for example
    script: '<script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>' for example
    '''
    _NAMESPACES[name] = script

def show(objs):
    if isinstance(objs, (list, tuple)):
        scripts = [py2js(o) for o in objs]
        last_call = objs[-1].__name__ + '()'
    else:
        scripts = [ py2js(objs)]
        last_call = objs.__name__ + '()'
    scripts.append(last_call)
    scripts = '\n'.join(scripts)
    namespaces = list(_NAMESPACES.keys())
    namespaces = '\n'.join(namespaces) if namespaces else ''
    template = settings.TEMPLATE.read_text(encoding='utf8')
    html = template.format(script=scripts, namespaces=namespaces)
    with NamedTemporaryFile(suffix='.html', 
                            prefix='matter.py.',
                            delete=False, 
                            mode='w', 
                            encoding='utf8') as f:
        f.write(html)
    webbrowser.open('file://' + f.name)




def register_notebook():
    from IPython.core.magic import register_cell_magic
    from IPython.display import IFrame
    import os
    from pathlib import Path
    dir_name = 'matter-html'
    cwd = os.getcwd()
    dir_path = Path(os.path.join(cwd, dir_name))
    dir_path.mkdir(parents=True, exist_ok=True)
    template = settings.TEMPLATE.read_text(encoding='utf8')
    namespaces = list(_NAMESPACES.keys())
    namespaces = '\n'.join(namespaces) if namespaces else ''
    @register_cell_magic
    def matter_inline(line, cell):
        kws = line.split(' ')
        kwargs = {}
        for kw in kws:
            k, v = kw.split('=')
            kwargs[k] = v
        notebook = kwargs.pop('notebook', 'matter.py+notebook')
        file_id = kwargs.pop('file_id', 'file_id')
        filename = f"{dir_name}/{notebook}-{file_id}.html"
        js = py2js(cell)
        with open(filename, "w", encoding='utf8') as fp:
            fp.write(template.format(script=js, name=filename, page_link=filename, namespaces=namespaces) )
        if 'height' not in kwargs:
            kwargs['height'] = '200px'
        return IFrame(filename, width="100%", **kwargs)