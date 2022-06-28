
from .views import IndexView
from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.urls import path, include


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profissionais/', views.ProfissionalList.as_view(),  name='profissionais'),
    path('create/', views.ProfissioanlCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ProfissionalUpdate.as_view(), name ='update'),
    path('detail/<int:pk>/', views.ProfissionalDetail.as_view(), name ='detail'),
    path('delete/<int:pk>/', views.ProfissionalDelete.as_view(), name ='delete'),
    path('accounts/', include('allauth.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)