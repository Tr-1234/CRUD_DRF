from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>', views.student_detail),
    path('stuinfo/', views.student_list),
    path('stucreate/',views.student_create),
    path('stupdate/<int:pk>',views.student_put),
    path('studelete/<int:pk>',views.student_delete)
]
