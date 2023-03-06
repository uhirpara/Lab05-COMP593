import requests
DAD_JOKE_API_URL='https://icanhazdadjoke.com/'

DAD_JOKE_SEARCH_URL=f'{DAD_JOKE_API_URL}/search'

def main():
    jokes=search_dad_jokes('dog')

    return


def search_dad_jokes(search_term,page=1,limit=20):
   #setup the query string parameters
   query_param={
        'page': page,
        'limit': limit,
        'term': search_term
   }

   # setup the header parameters
   header_params={
        'Accept':'application/json',

    }

    #send a GET request for a dad jokes taht conatain search term
   print(f'searching for dad jokes containing "{search_term}"...',end='')
   resp_msg=requests.get(DAD_JOKE_SEARCH_URL,params=query_param,headers=header_params)
   #check whether the request was successful
   if resp_msg.ok:
        print(f"success")
        body_dict=resp_msg.json()
        jokes_portion=body_dict['results']
        jokes_list=[j['joke'] for j in jokes_portion]

        return jokes_list
   else:
        print(f"failure")
        print(f"Response code {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")


def get_random_dad_joke():


    

    # setup the header parameters
    header_params={
        'Accept':'application/json',

    }
    #send a GET request for a random dad joke
    print('Gatting a random dad joke...',end='')
    resp_msg=requests.get(DAD_JOKE_API_URL,headers=header_params)

    #check whether the request was successful

    if resp_msg.ok:
        print(f"success")
        body_dict=resp_msg.json()
        return body_dict("joke")
        print(f"URL of new paste: {resp_msg.text}")
        return resp_msg.text
    else:
        print(f"failure")
        print(f"Response code {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")
    return



if __name__=="_main_":
 main()