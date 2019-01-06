import os
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView

class PostListView1(View):
    def get(self, request):
        name = 'K.Teari'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return'''
            <h1>AskDjango - Class Based View </h1>
            <p>{name}</p>
            <p>김태리도 예쁘다!! 나도 예쁘고 싶어.</p>
        '''

post_list1 = PostListView1.as_view()



class PostListView2(TemplateView):
    template_name = 'post_list.html' # dojo/post_list.html 은 에러
    '''django.core.exceptions.ImproperlyConfigured: 
    TemplateResponseMixin requires either a definition of 'template_name' 
    or an implementation of 'get_template_names()'''

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = 'K.Teari !!'
        #print('context type of:', type(context)) # <class 'dict'>
        return context

post_list2 = PostListView2.as_view()


class PostListView3(View):
    def get(self, request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii':False})

    def get_data(self):
        return {'message' : 'Hello, Python and Django'
        , 'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS']}

post_list3 = PostListView3.as_view()



class ExcelDownloadView(View):
    excel_path = '/Users/naami/git/hello_django/sample.xlsx'
    def get(self, request):
        filename = os.path.basename(self.excel_path)
        #print("????", filename)
        with open(self.excel_path, 'rb') as f:
            response = HttpResponse(f, content_type='application/vnd.ms-excel') # 필요한 응답헤더 세팅
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
            return response

excel_downlaod = ExcelDownloadView.as_view()