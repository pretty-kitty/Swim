from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

class IndexView(TemplateView):
    template_name = 'index.html'
    
    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)