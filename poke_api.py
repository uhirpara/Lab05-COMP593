import requests

def get_info_poke(pokemon):

    pokemon=str(pokemon)
    url=f'https://pokeapi.co/api/v2/pokemon/{pokemon}'

    resp_msg=requests.get(url)

    print(f"Getting information for {pokemon}...")

    if resp_msg.ok:
        print('success')
        return resp_msg
    else:
        print("failure")
        print(f"Response code : 404)")
        
        
    return
def main():
    url=get_info_poke('6')
    return

if __name__ == '_main_':
    main()