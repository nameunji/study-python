import json
import websocket

from django.shortcuts             import render
from django.views                 import View
from websocket                    import create_connection
from django.http                  import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from boto3.dynamodb.conditions    import Key, Attr


def index(request):
    return render(request, 'order/index.html', {})

# def orderStatus(request):
#     dynamodb = boto3.resource('dynamodb')
#     table = dynamodb.Table('lastordr_order')

#     order_count = table.scan(
#         FilterExpression=Key('status').eq(201)
#     )["Count"]

#     receive_count = table.scan(
#         FilterExpression=Key('status').eq(210)
#     )["Count"]

#     return JsonResponse({"order_count": order_count, "receive_count": receive_count}, status=200)


@csrf_exempt
def check(request):
    request_data = json.loads(request.body)
    if len(request_data) > 0:
        json_data = json.dumps(request_data)
        ws = create_connection("ws://13.125.211.215:8000/ws/order/")
        ws.send(json_data)
        ws.close()
    return HttpResponse(status = 404)

