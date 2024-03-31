import json
import time

def get_chat_history(username, r):
  messages = []
  for message_json, _ in r.zrangebyscore(f'user:{username}', min=0, max='+inf'):
    messages.append(json.loads(message_json))
  return messages

def add_chat_history(username,user_query, response, r, role='assistant'):
  user_query['timestamp'] = int(time.time())
  llm_response = {'role': role, 'content': f'{response}', 'timestamp': int(time.time())}

  r.zadd(f'user:{username}', {{json.dumps(llm_response): llm_response['timestamp']}})
  r.zadd(f'user:{username}', {json.dumps(user_query): user_query['timestamp']})

def add_first_response(username, response, r, role='assistant'):
    llm_response = {'role': role, 'content': f'{response}', 'timestamp': int(time.time())}
    r.zadd(f'user:{username}', {{json.dumps(llm_response): llm_response['timestamp']}})

