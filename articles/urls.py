import debug_toolbar
from django.urls import path, include
from django.contrib import admin
from articles.views import articles_list



urlpatterns = [
    path('', articles_list, name='articles'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
]
