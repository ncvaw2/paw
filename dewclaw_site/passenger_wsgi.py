import os, sys

log = file('/home/karlov3/paw/dewclaw/log', 'a')


INTERP = "/home/karlov3/paw/env/bin/python"
if sys.executable != INTERP:
    print >>log, "Detected wrong interpreter location, swapping to %s" % (INTERP)
    #swapping interpreters will not flush any files
    log.flush()
    log.close()
    os.execl(INTERP, INTERP, *sys.argv)
    #Should resume execution from the top of the file




cwd = os.getcwd()
myapp_directory = cwd + '/dewclaw'


print >>log, "myapp_directory %s" % (myapp_directory)


sys.path.insert(0,myapp_directory)
sys.path.append(os.getcwd())
os.environ['DJANGO_SETTINGS_MODULE'] = "main.settings"

print >>log, sys.path
log.flush()



#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.get_wsgi_application()

from paste.exceptions.errormiddleware import ErrorMiddleware
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
# To cut django out of the loop, comment the above application = ... line ,
# and remove "test" from the below function definition.
def testapplication(environ, start_response):
    status = '200 OK'
    output = 'Hello World! Running Python version ' + sys.version + '\n\n'
    response_headers = [('Content-type', 'text/plain'),
                       ('Content-Length', str(len(output)))]
    # to test paste's error catching prowess, uncomment the following line
    # while this function is the "application"
    #raise("error")
    start_response(status, response_headers)
    return [output]

application = ErrorMiddleware(application, debug=True)
