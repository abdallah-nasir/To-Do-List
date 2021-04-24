from django.urls import path
from . import views
from .views import *

app_name="api"
urlpatterns = [
	# path('', views.apiOverview, name="api-overview"),
	path('task-list/',taskList.as_view(), name="task-list"),
	path('task-detail/<str:id>/',taskDetail.as_view(), name="task-detail"),
	path('task-create/', views.taskCreate.as_view(), name="task-create"),

	path('task-update/<str:id>/',taskUpdate, name="task-update"),
	path('task-delete/<str:id>/',taskDelete.as_view(), name="task-delete"),
]
