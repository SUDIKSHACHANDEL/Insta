import urllib
import requests
# import constants file to get the access token.
from constants import APP_ACCESS_TOKEN,BASE_URL

def get_own_post():
    #Here we have the overall logic of the function.
    request_url = (BASE_URL+'users/self/media/recent/?access_token=%s') %(APP_ACCESS_TOKEN)
    print'GET request url:%s'%(request_url)
    own_media = requests.get(request_url).json()

    if own_media['meta']['code']==200:
        # It extract the post id
        if len(own_media['data']):
            image_name = own_media['data'][0]['id']+'.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            print'Your image has been downloaded!'


             # service = ['food','clothes']
             # for post in own_media['data']:
             #    for serve in service:
             #        if serve in post['caption']['text']:
             #             pass


        else:
            print'Post does not exist!'


    else:
        print'Status code other than 200 recevied!'


