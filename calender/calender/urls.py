"""djuser URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url ,include
from django.contrib import admin


#from accounts.views import activate_user_view, home, register, login_view, logout_view
from users.views import home,login,register,show_program

# urlpatterns = [
#     url(r'^$', home),
#     url(r'^admin/', admin.site.urls),
#     url(r'^register/$', register),
#     url(r'^login/$', login_view),
#     url(r'^logout/$', logout_view),
#     url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view),
# ]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^login/$', login),
    url(r'^register/$', register),
    url(r'^(?P<slug>[\w-]+)/', include('users.urls')),
]