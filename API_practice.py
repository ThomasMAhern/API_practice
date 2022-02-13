import requests as api

response = api.get('https://api.nationalize.io/?name=Joe')
print(response)

request = response.json()['country']
response.headers
# request



















query_params = {"gender": "female", 
                "nat": "de",
               }
requests.get("https://randomuser.me/api/", params=query_params).json()





rando_person = requests.get('https://randomuser.me/api/').json()
rando_person['results']




def rando_person():
    rando_person = requests.get('https://randomuser.me/api/').json()
    return rando_person['results']

rando_person()

























anime = 'ranking'
response = api.get(f'https://api.jikan.moe/v3/search/anime?q={anime}')
request = response.json()['results']
request
# [i['episodes'] for i in request if i['mal_id'] == 47778]








def demon_slayer():
    '''returns integer of current number of released episodes for season 2'''
    response = api.get(f'https://api.jikan.moe/v3/search/anime?q=kimetsu_no_yaiba')
    request = response.json()['results']
    return [i['episodes'] for i in request if i['mal_id'] == 47778][0] #the id can be found by looking through 'response'

demon_slayer()













[(i['API'], i['Description'], i['Link'], ' ') for i in requests.get('https://api.publicapis.org/entries').json()['entries']]