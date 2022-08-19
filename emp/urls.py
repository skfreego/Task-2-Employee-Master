from django.urls import path
from .views import HomeView, LoginView,HomeView, EmpAdd, EmpList, ContactView, EmpUpdateView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('logout/', views.logout_view,name='logout'),
    path('addemp/', EmpAdd.as_view(),name='addemp'),
    path('emplist/', EmpList.as_view(),name='emplist'),
    path('contact/', ContactView.as_view(),name='ContactView'),
    path('empupdate/update/<int:pk>/', EmpUpdateView.as_view(),name='empupdate'),
]

urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
