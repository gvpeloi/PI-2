from django.urls import path, include
from django.urls import path
from .views import IndexView
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings
from core import views



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    path('profissionais/', views.ProfissionalList.as_view(),  name='profissionais'),
    path('create/', views.ProfissioanlCreate.as_view(), name ='create'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)