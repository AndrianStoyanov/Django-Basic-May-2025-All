from datetime import datetime

from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView

import posts
from formsbasice import settings
from posts import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('post/', include([
        path('add/', views.CreatePost.as_view(), name='add-post'),
        path('edit/<int:pk>/', views.EditPost.as_view(), name='edit-post'),
        path('delete/<int:pk>/', views.DeletePost.as_view(), name='delete-post'),
        path('details/<int:pk>/', views.DetailsPost.as_view(), name='post-details'),
    ])),
    path('redirect/', views.MyRedirectView.as_view()),

]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)