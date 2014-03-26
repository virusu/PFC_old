from django.http import HttpResponse
from grimoire-api/scm.py import SCM

def home(request):

	html = "<html><body>home</body></html>"
	return HttpResponse(html)

def users(request):
	html = ""
	return HttpResponse(html)

def projects(request, project):
	html = "<html><body>projects view goes here</body></html>"
	return HttpResponse(html + " and project name is " + project)

def ncommits(request):
    data = SCM (database = 'mysql://jgb:XXX@localhost/vizgrimoire_cvsanaly',
            var = "ncommits", dates = (None, None))
    return HttpResponse(data.total())
