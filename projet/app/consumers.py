from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print('Connection Accepted !!!')

    async def disconnect(self, close_code):
        await self.close()
        print('Connection Disconnected !!!')


    async def receive(self, text_data=None):
        if text_data:
            try:
                text_data_json = json.loads(text_data)
                message = text_data_json["message"]
                await self.send(text_data=json.dumps({"message": message}))
            except json.JSONDecodeError as e:
                print('Received invalid JSON data:', text_data)
        else:
            print('Received empty text_data')
