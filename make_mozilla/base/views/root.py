import jingo

from make_mozilla.news.models import Article
from make_mozilla.projects.models import Project
from make_mozilla.events.models import Event


def index(request):
    news = Article.objects.filter(featured=True).order_by('-updated')[0:3]
    projects = Project.objects.filter(featured=True).order_by('?')[0:5]
    events = Event.objects.filter(official=True).order_by('start')[0:3]
    return jingo.render(request, 'splash.html', {
        'news': news,
        'projects': projects,
        'events': events,
    })


def fail(request):
    return jingo.render(request, 'base/404.html', {}, status=404)


def app_fail(request):
    return jingo.render(request, 'base/500.html', {}, status=500)
