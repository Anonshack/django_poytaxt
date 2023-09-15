from django.urls import path
from .views import (HomePageView,
                    TumanListView,
                    setLanguage,
                    )

urlpatterns = [
    path('setLang/<str:lang>', setLanguage),
    path('tumanlar/<int:pk>/', TumanListView.as_view(), name='tuman_list'),
    path('', HomePageView.as_view(), name='home'),
]
