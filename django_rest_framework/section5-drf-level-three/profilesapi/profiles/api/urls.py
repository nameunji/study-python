# from django.urls import path
# from profiles.api.views import ProfileList
#
# urlpatterns = [
#     path("profiles/", ProfileList.as_view(), name="profile-list")
# ]


# use ViewSet
from django.urls import path
from profiles.api.views import ProfileViewSet

profile_list = ProfileViewSet.as_view({"get": "list"})
profile_detail = ProfileViewSet.as_view({"get": "retrieve"})

urlpatterns = [
    path("profiles/", profile_list, name="profile-list"),
    path("profiles/<int:pk>/", profile_detail, name="profile-detail")
]

# use ViewSet + Router
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from profiles.api.views import ProfileViewSet, ProfileStatusViewSet, AvatarUpdateView

# router는 자동으로 links를 생성해낸다.
router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"status", ProfileStatusViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update")
]