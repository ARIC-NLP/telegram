from telethon import TelegramClient, sync
from telethon.tl.functions.messages import GetHistoryRequest
import pandas as pd

# ---------------------------------------------------------------------------------------------

api_id = XXXXXX
api_hash = '7djdadf992302f0kf003'
phone_number = '+01167512XXX73'
channel_username = 'nameid'  
channel_clear_name = "Clear Name"

# ---------------------------------------------------------------------------------------------

client = TelegramClient(None, api_id, api_hash).start()


my_private_channel_id = None
my_private_channel = None

for dialog in client.iter_dialogs():
    if dialog.name == channel_clear_name:
        my_private_channel = dialog
        my_private_channel_id = dialog.id
        break

if my_private_channel is None:
    print("chat not found")
else:
    print("chat id is", my_private_channel_id)


if not client.is_user_authorized():
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('Enter code: '))


channel_entity = client.get_entity(my_private_channel_id)

# Get recent posts
posts = client(GetHistoryRequest(
    peer=channel_entity,
    limit=100,
    offset_date=None,
    offset_id=0,
    max_id=0,
    min_id=0,
    add_offset=0,
    hash=0))
# messages stored in `posts.messages`

for message in posts.messages:
	print(message)
	if message.media is not None:
		client.download_media(message.media, './image'+str(message.id))
       

client.disconnect()
