import requests



    
    

def get_info_poke(poke_name):

    poke_name=str(poke_name).strip().lower()
    Poke_url=f'https://pokeapi.co/api/v2/pokemon/{poke_name}'

    resp_msg=requests.get(Poke_url)

    print(f"Getting information for {poke_name}...",end='')

    if resp_msg.ok:
        print('success')
        return resp_msg
    else:
        print("failure")
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        
        
    return
def main():
    get_url=get_info_poke('6')
    return

if __name__ == '_main_':
    main()