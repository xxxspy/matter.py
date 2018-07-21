from tempfile import NamedTemporaryFile
from . import settings
from pscript import py2js
import webbrowser

def show(objs):
    if isinstance(objs, (list, tuple)):
        scripts = [py2js(o) for o in objs]
        last_call = objs[-1].__name__ + '()'
    else:
        scripts = [ py2js(objs)]
        last_call = objs.__name__ + '()'
    scripts.append(last_call)
    scripts = '\n'.join(scripts)
    template = settings.TEMPLATE.read_text(encoding='utf8')
    html = template.format(script=scripts)
    with NamedTemporaryFile(suffix='.html', 
                            prefix='matter.py.',
                            delete=False, 
                            mode='w', 
                            encoding='utf8') as f:
        f.write(html)
    webbrowser.open('file://' + f.name)
