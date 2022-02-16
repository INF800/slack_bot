import os
import requests
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


# how to generate URL https://www.youtube.com/watch?v=lEQ68HhpO4g 
INCOMING_WEBHOOKS_ACCESS_URL=os.getenv("INCOMING_WEBHOOKS_ACCESS_URL")


def send_message(post_data, api_url, headers={'Content-Type': 'application/json'}):
    response = requests.post(api_url, headers=headers, json=post_data) 
    return response

def generate_post_data(markdown_texts):
    # https://api.slack.com/messaging/composing/layouts#attachments
    if type(markdown_texts)!=list:
        markdown_texts = [markdown_texts]
    post_data = {'blocks': []}
    for text in markdown_texts:
        content = {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": text
            }
        }
        post_data['blocks'].append(content)
    print(post_data)
    return post_data


def send_markdown(text_or_list_of_texts, api_url=INCOMING_WEBHOOKS_ACCESS_URL):
    post_data = generate_post_data(text_or_list_of_texts)
    return send_message(post_data, api_url)
    

def main():
    post_data = generate_post_data("```hellow!!```")
    send_message(post_data, api_url=INCOMING_WEBHOOKS_ACCESS_URL)

if __name__=='__main__':
    main()