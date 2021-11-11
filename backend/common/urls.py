from django.conf.urls import url

from common import views

urlpatterns = {
    url(r'', views.connection)
    # url(r'', views.users)

}