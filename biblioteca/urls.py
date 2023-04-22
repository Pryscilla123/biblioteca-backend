from rest_framework import routers

from biblioteca.views import BookViewsSets, AuthorViewsSets

router = routers.SimpleRouter()
router.register(r'book', BookViewsSets)
router.register(r'author', AuthorViewsSets)

urlpatterns = router.urls
