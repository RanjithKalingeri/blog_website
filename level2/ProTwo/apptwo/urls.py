from django.conf.urls import url
from apptwo import views
from django.contrib import admin
from django.urls import path


app_name = 'apptwo'


urlpatterns = [
   url(r'^test/$', views.test, name = 'test' ),
   url(r'^$', views.base, name = 'base' ),
   url(r'^test2/$', views.test2, name = 'test2' ),
   url(r'^test3/$', views.test3, name = 'test3' ),
   url(r'^register/$', views.register, name = 'register' ),
   url(r'^index2/$', views.index2, name = 'index2' ),
   # url(r'^admin/$', admin.site.urls),
   path('admin/', admin.site.urls),

   url(r'special/', views.special, name = 'special'),
   url(r'^login/$', views.user_login, name = 'login'),

]
