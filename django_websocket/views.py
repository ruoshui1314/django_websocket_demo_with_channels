from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@csrf_exempt
def get_users(request):
    if request.method != 'GET':
        return HttpResponse('method should be GET')
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'chat_ttt',
        {'type': 'chat_message', 'message': 'welcome'},
    )
    return HttpResponse('ok')
