
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Enformer Admin"
admin.site.site_title = "Enformer Admin Portal"
admin.site.index_title = "Welcome to Admin Practice Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('enformerapp1.urls')),
    # path('/dashboard', include('enformerapp1.urls')),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

