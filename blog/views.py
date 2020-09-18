from django.shortcuts import render
from .models import Post

def post_list(request):
    # 33Queries(including 31 similar and 19 duplicates) in 12.98ms
    # post_list = Post.objects.all()

    # 23Queries(including 20 similar and 9 duplicates) in 7.98ms
    # select_related -> foreignkey
    # post_list = Post.objects.select_related('author').all()

    # 14Queries(including 10 similar and 9 duplicated) in 4.00ms
    # prefetch_related -> many to many filed
    # post_list = Post.objects.prefetch_related('tag_set').select_related('author').all()

    # 4Queries(including 0 similar and 0 duplicated) in 2.99ms
    post_list = Post.objects.prefetch_related('tag_set').select_related('author__profile').all()
    
    return render(request, 'post_list.html', {'post_list' : post_list})