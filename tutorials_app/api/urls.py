from django.urls import path
from tutorials_app.api.views import TutorialList,TutorialDetail


urlpatterns=[
    path('',TutorialList.as_view(),name='tutorial_list'),
    path('tutorial/<int:pk>',TutorialDetail.as_view(),name='tutorial_detail'),
]