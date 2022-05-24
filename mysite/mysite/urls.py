from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), #отслеживание перехода на главную страницу
    path('news/', include('news.urls'))
]
