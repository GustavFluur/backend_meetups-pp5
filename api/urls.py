from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('task-list', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),

	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]


#  What is connected to what:
# #### 
#  views.py <=> api-overview = use the same
#  views.py <=> 'task-list' = meetup-list
#  views.py <=> 'task-detail/<str:pk>/ = meetup-detail/<str:pk>/ 
#  views.py <=> 'task-create/' = meetup-create
#  views.py <=> 'task-update/<str:pk>/  = meetup-update/<str:pk>/
#  views.py <=> 'task-delete/<str:pk>/' = meetup-delete/<str:pk>/ 