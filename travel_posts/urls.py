from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import main_page, about_page,posts_page
urlpatterns=[
    path("",main_page,name="main_page"),
    path("about/",about_page,name="about_page"),
    path("posts/",posts_page,name="posts_page"),

]
if settings.DEBUG:  # Обслуживаем медиа файлы только в режиме DEBUG
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)