from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from adopter import views

app_name = 'adopter'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('Report/', include('Report.urls')),
    path('Article/', include('Article.urls')),
    path('success_story/', include('success_story.urls')),

    path('stories/', views.stories, name='stories'),
    path('Report/', include('Report.urls')),
    path('Article/', include('Article.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
