from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SubscriptionView, SubscriptionViewSet


router = DefaultRouter()
router.register('admin', SubscriptionViewSet)

urlpatterns = [
    # path('admin/', SubscriptionViewSet.as_view()),
    path('reg/create/', SubscriptionView.as_view(), name="subscription")
]

urlpatterns += router.urls
