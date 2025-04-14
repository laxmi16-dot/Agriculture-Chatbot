from channels.generic.websocket import WebsocketConsumer
import json

import os

from groq import Groq

client = Groq(
    api_key="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"
)
class ConnectTOBot(WebsocketConsumer):
    def connect(self):
        
        print("connection done from client")
        self.accept()
        self.send(json.dumps({"message" : "Hi I am Kisan`s Friend!! Ask Me any question.."}))
    

    def receive(self, text_data=None, bytes_data=None):
        

        chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"{ text_data}",
        }
            ],
    model="llama3-8b-8192",
        )
        self.send(json.dumps({'message':f" {chat_completion.choices[0].message.content}"}))
        


        return super().receive(text_data, bytes_data)

    def disconnect(self, code):
        print("Client Disconnected")
        self.disconnect(code)

#The code defines a WebSocket-based chatbot in Django using `channels`. The `ConnectTOBot` class manages real-time communication between a client and a server. When a client connects, the `connect` method accepts the connection and sends a welcome message. The `receive` method processes incoming messages from the client, forwards them to an AI model (via the `Groq` client using the model `llama3-8b-8192`), and sends the AI's response back to the client in real time. The `disconnect` method handles and logs client disconnections. This setup enables dynamic, conversational interactions between users and the chatbot.






        
