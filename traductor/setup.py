import sys
from distutils.core import setup

kwargs = {}
if 'py2exe' in sys.argv:
    import py2exe
    kwargs = {
        'console' : [{
            'script'         : 'trasl.py',
            'description'    : 'Programa traductor de subtitulos.',
            'icon_resources' : [(0, 'icon.ico')]
            }],
        'zipfile' : None,
        'options' : { 'py2exe' : {
            'dll_excludes'   : ['w9xpopen.exe'],
            'bundle_files'   : 1,
            'compressed'     : True,
            'optimize'       : 2
            }},
         }

setup(
    name='traductor',
    author='josue acevedo maldonado (Neomatrix)',
    author_email='josuecevedo@gmail.com',
    **kwargs)
