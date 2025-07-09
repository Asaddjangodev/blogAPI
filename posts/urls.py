from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewSet


router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")

urlpatterns = router.urls
#urlpatterns = [
#    path("users/", UserList.as_view()), # new
#    path("users/<int:pk>/", UserDetail.as_view()), # new
#    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
#    path("", PostList.as_view(), name="post_list"),
#]

