from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print('*****************', self.scope)
        print('Connection Accepted !!!')

    async def disconnect(self, close_code):
        await self.close()
        print('Connection Disconnected !!!')



    async def receive(self, text_data=None):
        data = text_data
        if data:
            try:
                await self.send(text_data=data)
            except Exception as e:
                print(e)
        else:
            print('Received empty text_data')
