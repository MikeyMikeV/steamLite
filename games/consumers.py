import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import GameMainInfo, Review
from profiles.models import Profile

class GameConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.game_id = None
        self.game_group_name = None
        self.game_main_info = None
        self.user_profile = None

    def connect(self):
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        self.game_group_name = f'game_{self.game_id}'
        self.game_main_info = GameMainInfo.objects.get(game_id=self.game_id)
        self.user_profile = Profile.objects.get(user_id = self.scope['user'].pk)
        # connection has to be accepted
        self.accept()

        # join the room group
        async_to_sync(self.channel_layer.group_add)(
            self.game_group_name,
            self.channel_name,
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.game_group_name,
            self.channel_name,
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(message)
        if not self.user_profile.user.is_authenticated:  # new
            return
        
        # send chat message event to the room

        match message:
            case 'add_to_wishlist':  
                if not self.user_profile.wishlist.contains(self.game_main_info):
                    self.user_profile.wishlist.add(self.game_main_info)
                    async_to_sync(self.channel_layer.group_send)(
                        self.game_group_name,
                        {
                            'type': 'add_to_wishlist',
                        }
                    )
                else:
                    self.user_profile.wishlist.remove(self.game_main_info)
                    async_to_sync(self.channel_layer.group_send)(
                        self.game_group_name,
                        {
                            'type': 'remove_from_wishlist',
                        }
                    )
            case 'add_to_ignorelist':
                if not self.user_profile.ignore.contains(self.game_main_info):
                    self.user_profile.ignore.add(self.game_main_info)
                    async_to_sync(self.channel_layer.group_send)(
                        self.game_group_name,
                        {
                            'type': 'add_to_ignorelist',
                        }
                    )
                else:
                    self.user_profile.ignore.remove(self.game_main_info)
                    async_to_sync(self.channel_layer.group_send)(
                        self.game_group_name,
                        {
                            'type': 'remove_from_ignorelist',
                        }
                    )
            case 'add_review':
                review_value = int(text_data_json['value'])
                review_text = text_data_json['text']
                print(self.user_profile, review_text, review_value)
                review = Review.objects.create(
                    author = self.user_profile,
                    text = review_text,
                    value = review_value
                )
                self.game_main_info.reviews.add(review)
            case _:
                print('no')
        

    def add_to_wishlist(self, event):
        self.send(text_data=json.dumps(event))

    def remove_from_wishlist(self, event):
        self.send(text_data=json.dumps(event))

    def add_to_ignorelist(self, event):
        self.send(text_data=json.dumps(event))

    def remove_from_ignorelist(self, event):
        self.send(text_data=json.dumps(event))