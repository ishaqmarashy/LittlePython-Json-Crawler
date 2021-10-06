from typing import Sized
import requests

def api(arg):
    #   My Own API Key you may use yours if you'd like
    apikey='215E7ED2-8B7D-2842-A5B0-B6F438ECB5998AB6FBC2-59BA-41CC-B54C-B96011624A9B'
    url=f'https://api.guildwars2.com/v2/{arg}'
    response=requests.get(url,data={'access_token':apikey})
    # response=request.post(url, data=())
    return response.json()
    
def getItem(arg):
    if(arg):
        return api(f'items/{arg}')

def listCharacters(arg):
    if(arg):
        return api(f'characters/{arg}')
    else:
        return api('characters/')

def listEquipment(arg):
    return listCharacters(f'{arg}')
    
print('Select a character:')
charList=listCharacters('')


while True:
    count=1
    for i in charList:
        print (f'{count} : {i}')
        count=count+1
    Input = int(input())
    if(Input<1 or Input>count-1):
        print('invalid')
    else:
        listEquip=listEquipment(charList[Input-1])
        activeEquip=listEquip['equipment']
        activeID=listEquip['name']
        print(f'{charList[Input-1]}\'s active {activeID} template\'s equipment: ')
        for item in activeEquip:
            itemDetail=getItem(item['id'])
            print(f'{item["slot"]}: {itemDetail["name"]}')
            if 'stats' in item:
                for stat in item['stats']['attributes']:
                    print(f"    {stat}: {  item['stats']['attributes'][stat]}")
            if 'upgrades' in item:
                for upgrades in item['upgrades']:
                    upgrade=getItem(upgrades)
                    print(f'          {upgrade["name"]}')
                    if 'bonuses' in upgrade['details']:
                        for bonus in upgrade['details']['bonuses']:
                            print(f'               {bonus}')
                    else:
                        print(f'             {upgrade["details"]["infix_upgrade"]["buff"]["description"]}')



    print('Select a character:')
