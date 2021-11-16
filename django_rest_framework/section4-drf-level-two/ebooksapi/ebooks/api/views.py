from rest_framework import generics, mixins
from rest_framework.generics import get_object_or_404

from ..models import Ebook, Review
from .serializers import EbookSerializer, ReviewSerializer


# use GenericAPIView + Mixin
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


# use ListCreateAPIView
class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class ReviewCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # Review는 request.data로 전달되는 데이터 외에 ebook_pk값이 같이 저장되어야한다.
    # serialzier.save()에서 추가로 저장해야 되는 데이터(ForeignKey로 연결된 데이터)가 있을 때는 perform_create()를 override해줘야 한다.
    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        serializer.save(ebook=ebook)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer