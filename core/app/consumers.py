from channels.generic.websocket import WebsocketConsumer
from channels.consumer import SyncConsumer,AsyncConsumer
from asgiref.sync import async_to_sync
import json


class MySyncConsumer(SyncConsumer):
    
    def websocket_coonect(self,event):
        """
            This handler is called when client initially opens a
            connection add is about to finish the websocket handler.
        """
        print('websocket connected',event)
    
    def websocket_receive(self,event):
        
        
        """
        This handler is called when data received from Client.
        """
        print('websocket Message Received',event)    
        
    def websocket_disconnect(self,event):
        """
            This handler is called when either connection to the client is
            lost, either from the client closing the connection, the server
            closing the connection, or loss the socket. 
        """
        print('websocket disconnnect',event)



class MyAsyncConsumer(AsyncConsumer):
    
    async def websocket_coonect(self,event):
        """
            This handler is called when client initially opens a
            connection add is about to finish the websocket handler.
        """
        print('websocket connected',event)
    
    async def websocket_receive(self,event):
        
        
        """
        This handler is called when data received from Client.
        """
        print('websocket Message Received',event)    
        
    async def websocket_disconnect(self,event):
        """
            This handler is called when either connection to the client is
            lost, either from the client closing the connection, the server
            closing the connection, or loss the socket. 
        """
        print('websocket disconnnect',event)




# class TextConsumer(WebsocketConsumer): 
#     def connect(self):
#         self.room_name ="test_cunsumer"
#         self.room_group_name ="text_consumer_group"
#         async_to_sync(self.channel_layer.group_add)(
#                 self.room_name,self.room_group_name            
#             )
#         self.accept()
#         self.send(text_data=json.dumps({'status':"connected"}))
        
        
#     def receive(self,text_data):
#         "send data from frontend to backend"
#         print(text_data)
#         self.send(text_data = json.dumps({'status':"we got you"}))
        
        
#     def disconnect(self,*args,**kwargs):
#         print('disconnected')