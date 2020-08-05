from rest_framework.routers import SimpleRouter

from testAPI_v2.viewsets import ProductSetViewSet, RecipientViewSet, OrderViewSet


class MyRouter(SimpleRouter):
    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()


router = MyRouter()
router.register(r'product_sets', ProductSetViewSet, basename='product_sets')
router.register(r'recipients', RecipientViewSet, basename='recipients')
router.register(r'orders', OrderViewSet, basename='orders')
urlpatterns = router.urls
