from django.conf.urls import url
from .                import consumers

# consumer 라우팅을 처리하기 위해 생성(장고의 url과 유사)
websocket_urlpatterns = [
    # url(r'^ws/order/$', consumers.OrderConsumer),
    url('ws/order/', consumers.OrderConsumer),
]
# ↑ 위 url을 장고가 인식할 수 있도록 장고(chatbot)의 routing.py에 추가해줘야함