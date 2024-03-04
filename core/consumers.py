# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'kitchen_group'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        order_data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "kitchen.message",
                "message": order_data['message'],
            }
        )
        await self.send(text_data=json.dumps({'message': 'Pedido recebido com sucesso!'}))

    async def kitchen_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

class KitchenConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'kitchen_group'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def kitchen_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': f"Received message in kitchen: {message}"
        }))
