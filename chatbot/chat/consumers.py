import json

from asgiref.sync               import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    # websocket 연결 시 실행
    async def connect(self):
        # chat/routing.py 에 있는
        # url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
        # 에서 room_name 을 가져옵니다.
        # 즉 소비자에게 WebSocket 연결을 열어줍니다.
        # 참고로 모든 소비자들은 현재 인증된 유저, URL의 인자를 포함하여 연결에 대한 정보를 갖는 scope를 갖습니다.
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # join group
        # 소비자들은 비동기 channel layer 메서드를 호출할 때 동기적으로 받아야 하기 때문에, async_to_sync(...) 같은 wrapper가 필요합니다.
        # ( 모든 channel layer 메서드는 비동기입니다. )
        # send 등과 같은 동기적인 함수를 비동기적으로 사용하기 위해서는 async_to_sync 로 감싸줘야한다.
        # async_to_sync(self.channel_layer.group_add)(
        #     self.room_group_name,
        #     self.channel_name
        # )
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # WebSocket 연결
        # self.accept()
        await self.accept()


    # websocket 연결 종료 시 실행
    async def disconnect(self, close_code):
        # leave group

        # async_to_sync(self.channel_layer.group_discard)(
        #     self.room_group_name,
        #     self.channel_name
        # )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    # receive message from WebSocket
    # 그룹에 메세지를 보냄 - 1번
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # room group에게 메세지 send
        # 그룹에게 이벤트를 보냅니다.
        # 이벤트에는 이벤트를 수신하는 소비자가 호출해야 하는 메서드 이름에 대응하는 특별한 type 키가 있습니다.
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name,
        #     {
        #         'type':'chat_message',
        #         'message':message
        #     }
        # )
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )

    # receive message from room group
    # 그룹에 메세지가 왔을 때 - 2번
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket

        # self.send(text_data = json.dumps({
        #     'message':message
        # }))
        await self.send(text_data=json.dumps({
            'message': message
        }))
