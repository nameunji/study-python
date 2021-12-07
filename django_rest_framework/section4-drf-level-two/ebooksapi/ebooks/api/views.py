from rest_framework import generics, mixins, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError

from ..models import Ebook, Review
from .pagination import SmallSetPagination
from .serializers import EbookSerializer, ReviewSerializer
from .permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly

""" use GenericAPIView + Mixin """
# class EbookListCreateAPIView(mixins.ListModelMixin,
#                              mixins.CreateModelMixin,
#                              generics.GenericAPIView):
#
#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


""" use ListCreateAPIView """
class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all().order_by("id")
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Review는 request.data로 전달되는 데이터 외에 ebook_pk값이 같이 저장되어야한다.
    # serialzier.save()에서 추가로 저장해야 되는 데이터(ForeignKey로 연결된 데이터)가 있을 때는 perform_create()를 override해줘야 한다.
    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)

        review_author = self.request.user

        # ebook 하나에 유저가 중복으로 review를 남길 수 없게끔.
        review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)
        if review_queryset.exists():
            raise ValidationError("You Have Already Reviewed this Ebook!")

        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]