from django.shortcuts import render,get_object_or_404, redirect

def main_page(request):
        return render(request,'main_page.html')

def about_page(request):
        return render(request,'about_page.html')

def posts_page(request):
        return render(request,'posts_page.html')