
from rest_framework.routers import DefaultRouter
from products.views import ProductOperations

router = DefaultRouter()
router.register('apis',ProductOperations)
urlpatterns = router.urls
'''
    apis/  --> post ---> save
    apis/{id}  -- get--> single retrieve
    apis/  put/patch --> update
    apis/id  delete - delete
    apis/   get --> list


'''

