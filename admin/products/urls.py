from django.urls import path

from .views import ProductViewSet, UserAPIView

# 配置URL，与views中对应
# 需要在admin.urls中创建
# restful风格
urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', UserAPIView.as_view())
]
