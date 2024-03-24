from django.urls import path

from .views import RegisterView, LoginView, EventView,EventListView, LikeSaveView

urlpatterns =[
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('event/', EventView.as_view(), name='event'),
    path('getevent/', EventListView.as_view(), name='events'),
    path('savelikes/', LikeSaveView.as_view(), name='savelike')
]