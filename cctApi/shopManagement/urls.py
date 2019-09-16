from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from . import views

router = routers.DefaultRouter()
router.register('customer', views.CustomerView)
router.register('product', views.ProductView)
router.register('order', views.OrderView)
router.register('orderline', views.OrderLineView)

urlpatterns = [
        path('', include(router.urls)),
        path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    ]


