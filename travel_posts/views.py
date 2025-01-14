from django.shortcuts import render,get_object_or_404, redirect
from .models import Article,Comments
from .forms import CommentForm
def main_page(request):
        return render(request,'main_page.html')

def about_page(request):
        return render(request,'about_page.html')

def posts_page(request):
        articles= Article.objects.all().order_by('-created_at')  # Сортировка постов от новых к старым
        context = {'articles': articles}
        return render(request,'posts_page.html', context)


def selected_post(request, pk):
    article = get_object_or_404(Article, id=pk)
    context = {'article': article}
    return render(request, 'selected_post.html', context)


def comments_page(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            form = CommentForm()
            success = True
        else:
            success = False
    else:
        form = CommentForm()
        success = False

    # Отображаем только проверенные отзывы
    comments = Comments.objects.filter(is_verified=True)

    return render(request, 'comments_page.html', {
        'form': form,
        'success': success,
        'comments': comments
    })
