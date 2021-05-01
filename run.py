# Run a test server.
from DashApp import app
import os
import importlib
DEBUG = 1
if DEBUG:
    print(app.url_map)

def Modules_getter():
    module_subdirs = [d for d in os.listdir('Modules/') if (os.path.isdir("Modules/"+d) and "__" not in d)]
    if DEBUG:
        print(module_subdirs)
    for s in module_subdirs:
        try:
            c360_module = importlib.import_module(f'Modules.{s}')
            if c360_module.conf()["enabled"] == True:
                importlib.import_module(f'Modules.{s}.views')
        except Exception as e:
            if DEBUG:
                print(e)

Modules_getter()
if DEBUG:
    print("=========== After =============")
    print(app.url_map)
app.run(host='0.0.0.0', port=8080, debug=True)