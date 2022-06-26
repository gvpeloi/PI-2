from django.urls import path, include
from django.urls import path
from .views import IndexView
from django.conf import settings
from django.conf.urls.static import static
from core import views



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profissionais/', views.ProfissionalList.as_view(),  name='profissionais'),
    path('create/', views.ProfissioanlCreate.as_view(), name ='create'),
    path('create/<int:pk>/', views.ProfissionalUpdate.as_view(), name ='update'),
    path('detail/<int:pk>/', views.ProfissionalDetail.as_view(), name ='detail'),
    path('delete/<int:pk>/', views.ProfissionalDelete.as_view(), name ='delete'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)