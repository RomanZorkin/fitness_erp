from django.urls import path

from bboard import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:rubric_id>/', views.by_rubric, name='by_rubric'),
    path('add/', views.BbCreateView.as_view(), name='add'),
    path('servadd/', views.add_service, name='servadd'),
    path('deviceadd/', views.AddDeviceView.as_view(), name='deviceadd'),    
    path('expenses_sample/', views.expenses_sample, name='expenses_sample'),
]
