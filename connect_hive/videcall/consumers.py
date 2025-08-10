from channels.generic.websocket import AsyncWebsocketConsumer
import json

class CallConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"call_{self.room_name}"

        # Add user to the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Remove user from the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)

        # Broadcast messages to the room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "send_signaling_message",
                "message": data
            }
        )

    async def send_signaling_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event["message"]))
