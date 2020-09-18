from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from blog.views import post_list

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('__debug__', include(debug_toolbar.urls)),
        path('', include('blog.urls'))

    ] 
