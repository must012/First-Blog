from django.views import generic
from django.shortcuts import render, reverse

from .models import Board

# Create your views here.

# object_list = Board.objects.order_by('-published_date')[:10]

"""
def index(request):
    # object_list = Board.objects.order_by('-published_date')[:5]
    # template = loader.get_template('homepage/index.html')
    #
    # return HttpResponse(template.render({'board_title': object_list}, request))

    object_list = Board.objects.order_by('-published_date')[:10]

    context = {
        'object_list': object_list,
        'object_len': int(Board.objects.count() / 10 + 1)
    }
    
    return render(request, 'homepage/index.html', context)
"""


# ListView 의 Default value 1) context_object_name = object_list
# 2) template_name = 모델명 소문자_detail.html
class IndexView(generic.ListView):
    model = Board
    template_name = 'homepage/index.html'
    paginate_by = 5  # 한 페이지에 보여줄 오브젝트 갯수
    # pagination 을 할 땐, template에서 page_obj 인스턴스의 메소드가 사용가능
    # is_paginated 페이징 됐다면
    # has_previous = 이전 페이지가 있다면
    # paginator.page_range = 페이지 갯수




# DetailView 의 Default value 1) context_object_name = object
# 2) template_name = 모델명 소문자_detail.html
class DetailView(generic.DetailView):
    model = Board
    template_name = 'homepage/detail.html'


# def detail(request, board_id):
#     post = go4(Board, pk=board_id)
#     return render(request, 'homepage/detail.html', {'post': post})

def check_boardnum(request):
    num = request.POST.get('pk',None)

    return reverse('homepage:detail', kwargs={'pk': 1})
