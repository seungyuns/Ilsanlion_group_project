
from django.contrib import admin
from django.urls import path
import ilsanprojectapp.views 
import blog.views
import accounts.views
import noticeapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 현수꺼
    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login, name='login'),
    path('logout/', accounts.views.logout, name='logout'),
    ###################호설########
    path('',blog.views.home,name='home'),
    path('blog/show/',blog.views.show,name='show'),
    path('blog/detail/<int:blog_id>/',blog.views.detail,name='detail'),
    path('blog/new/',blog.views.new,name='new'),
    path('blog/create/',blog.views.create,name='create'),
    path('blog/destroy/<int:blog_id>/',blog.views.destroy,name='destroy'),
    #######################승윤 #######
    path('notice/',noticeapp.views.notice, name='notice'),
]
