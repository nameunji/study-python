import order.routing

from channels.auth    import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# 클라이언트와 Channels 개발 서버가 연결될 때, ProtocolTypeRouter을 먼저 조사하여 어떤 타입의 연결(protocol)인지 확인
application = ProtocolTypeRouter({
    # (http->django views is added by default)

    # 만약 websocket protocol이라면, AuthMiddlewareStack으로 이어짐
    # AuthMiddlewareStack은 현재 인증된 사용자에 대한 참조로 scope를 결정
    # 이는 Django에서 현재 인증된 사용자의 view 함수에서 request 요청을 결정하는
    # AuthenticationMiddleware와 유사한 방식이며, 그 결과 URLRouter로 연결
    'websocket' : AuthMiddlewareStack(URLRouter(order.routing.websocket_urlpatterns))
})