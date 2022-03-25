from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from profiles.models import Profile
from profiles.api.serializers import ProfileSerializer


# class ProfileList(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]


# use ViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet

class ProfileViewSet(ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


# use ViewSet (+update)
from rest_framework import viewsets
from rest_framework import mixins
from profiles.api.permissions import IsOwnProfileOrReadOnly

class ProfileViewSet(mixins.UpdateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]


# use ViewSet (+update, delete) (profileStatus)
from rest_framework.viewsets import ModelViewSet
from profiles.models import ProfileStatus
from profiles.api.serializers import ProfileStatusSerializer
from profiles.api.permissions import IsOwnerOrReadOnly

class ProfileStatusViewSet(ModelViewSet):
    queryset = ProfileStatus.objects.all()
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)


from profiles.api.serializers import ProfileAvatarSerializer

class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object