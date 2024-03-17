from django.urls import path

from .views import JobView

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('jobs/', JobView.as_view()),
]
