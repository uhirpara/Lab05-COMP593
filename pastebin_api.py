import requests

API_POST_URL='https://pastebin.com/api/api_post.php'
DEVELOPER_KEY='4nxi4PWAoeAs2YkYbooPS4XncyEZ3dcO'
def main():
    paste_url=post_new_paste('whatever paste','a bunch of crap','','')
    return

def post_new_paste(title,body_text,expiration='10M',listed=True):
    """Creates a new public PasteBin paste
Args:
    title (str): Paste title body_text (str): Paste body text
    expiration (str, optional): Expiration date of paste (N = never, 10M = minutes, 1H, ID, 1W, 2W, IM, 6M, 1Y). Defaults to '10N
    listed (bool, optional): Whether paste is publicly listed (True) or not (False). Defaults to True.
Returns:
    str: URL of new paste, if successful. Otherwise None.
    
"""
    
    

    #create a dictioary of parameter values
    params={
        'api_dev_key':DEVELOPER_KEY,
        'api_option':'paste',
        'api_paste_code': body_text,
        'api_paste_name':title,
        'api_paste_expire_date':expiration,
        'api_paste_private': 0 if listed else 1 
    }
    #send the post request to the PostBin API
    print(f"Posting new paste to PasteBin...,",end='')
    resp_msg=requests.post(API_POST_URL,data=params)

    # check if Paste was crete successfully
    if resp_msg.ok:
        print(f"success")
        print(f"URL of new paste: {resp_msg.text}")
        return resp_msg.text
    else:
        print(f"failure")
        print(f"Response code {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")
        



if __name__=="_main_":
    main()