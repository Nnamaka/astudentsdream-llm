import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

system_prompt = {
    'role': 'system',
    'content': f"""You are an AI assistant who specializes in text analysis and I am Human. We will complete a text
analysis task together through a multi-turn dialogue. The task as follows: we have a text written by
an author, and at each turn I will give you a statement about the author. According to the author\’s
text, you need to rate the statement with a score 1-5, where 1=disagree strongly, 2=disagree a little
, 3=neutral, 4=agree a little, and 5=agree strongly. After rating all the statements (S0-S8), I will
ask you if the author is A: "High Agreeableness" or B: "Low Agreeableness", and then you need to give
your choice. Note that S1, S3, S4, S6, S8 are positive statements, with higher scores indicate
higher agreeableness, while S0, S2, S5, S7 are reverse-scored statements, with higher scores indicate
lower agreeableness.
AUTHOR’S TEXT:
I’m pretty happy with my first week and a half of classes. I’ve met a lot of people. It means a lot
to me. I am a very quiet, sort of shy person. I was afraid of coming to UT because I’m not the best
at making friends. So far though, it hasn’t been a problem. My big classes have been a little
intimidating because of there size. I used to have classes about 30 or less. Right now I am happy, UT
won its first football game. I’m glad I was able to go. It was lots of fun. Now I feel a little
exhausted. I haven’t really done all that much today. I actually got to sleep for 12 hours last night
. I could be exhausted because I am hungry. I think I’m pretty lucky. My parents sent me some food.
My brother brought it to Austin. He and I will share it. I’m already starting to miss home-cooked
meals. I think my 20 minutes are just about up. I probably fix a bite to eat, watch a little T. V.
and go to sleep.
""",
}