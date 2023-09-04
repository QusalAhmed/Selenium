import requests

message_text = "From Server"
bot_token = '5618872665:AAED7ikwYNQxFfZzWwR6B8-NVB3LKb5P-SA'
chat_id = '1783177827'
telegram_api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

try:
    response = requests.post(telegram_api_url, json={'chat_id': chat_id, 'text': message_text})
    print(response.text)
except Exception as send_message_error:
    print(send_message_error)
