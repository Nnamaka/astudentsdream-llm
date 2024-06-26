import json
import time

def get_chat_history(username, r):
  messages = []
  for message_json in r.zrangebyscore(f'user:{username}', min=0, max='+inf'):
    messages.append(json.loads(message_json))
  return messages

def add_chat_history(username,user_query, response, r, role='assistant'):
  print("not caught 1 here🤖")
  user_query['timestamp'] = int(time.time())
  print("not caught 2 here🤖")
  llm_response = {'role': role, 'content': f'{response}', 'timestamp': int(time.time())}

  
  user_query_json = {json.dumps(user_query): user_query['timestamp']}
  llm_response_json = {json.dumps(llm_response): llm_response['timestamp']}

  r.zadd(f'user:{username}', llm_response_json)
  r.zadd(f'user:{username}', user_query_json)

def add_first_response(username, response, r, role='assistant'):
    llm_response = {'role': role, 'content': f'{response}', 'timestamp': int(time.time())}
    llm_response_json = {json.dumps(llm_response): llm_response['timestamp']}

    r.zadd(f'user:{username}',llm_response_json)

