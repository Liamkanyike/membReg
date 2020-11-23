
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from users import views as user_views
from Regapp import views
from Regapp.views import ChurchListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', user_views.register, name='register'),
    path('dashboard', user_views.dashboard, name='dashboard'),
    path('', auth_views.LoginView.as_view(template_name='users/signin.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),



   
    #path('',views.login, name="login"),
    #path('logout/',views.logout, name="logout"),
    path('reg/',views.reg),
    path('view/', views.view, name="view"),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>', views.edit),
    path('details/<int:id>/', views.details, name="details"),
    path('update/<int:id>', views.update),
    path('check_email_exist', views.check_email_exist,name="check_email_exist"),
    path('check_phone_exist', views.check_phone_exist,name="check_phone_exist"),
    path('searchmain', views.searchmain, name="searchmain"),
    path('search', views.search, name="search"),
    path('church_list_view', ChurchListView.as_view(), name="church-list-view"),
    path('pdf/<pk>/', views.church_render_pdf_view, name="church-pdf-view"),
    path('pdf_view/<pk>/', views.pdf_view, name="pdf_view"),
    path('document_download/<pk>/', views.document_download, name="document_download"),


    
]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

