from django.urls import path, include
from django.urls import path
from .views import IndexView, CadastroForm, LoginForm, BaseView, Lista
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    path('cadastro/', CadastroForm,  name='cadastro'),
    path('login/', LoginForm, name='login'),
    path('base/', BaseView.as_view(), name='base'),
    path('profissionais/', Lista, name='profissionais'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)