from django.conf.urls import url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from testAPI_v2.viewsets import ProductSetViewSet, RecipientViewSet, OrderViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


class MyRouter(SimpleRouter):
    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = MyRouter()
router.register(r'product_sets', ProductSetViewSet, basename='product_sets')
router.register(r'recipients', RecipientViewSet, basename='recipients')
router.register(r'orders', OrderViewSet, basename='orders')
urlpatterns = router.urls

urlpatterns += [url(r'^', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), ]
