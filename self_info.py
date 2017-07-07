import requests
from constants import APP_ACCESS_TOKEN,BASE_URL

def self_info():
    #Logic of the function
    request_url =(BASE_URL + 'users/self/?access_token=%s')%(APP_ACCESS_TOKEN)
    print 'GET request url:%s'%(request_url)
    user_info= requests.get(request_url).json()
    if user_info['meta']['code']==200:
        #if there is some information of user
        if len(user_info['data']):
            print'User name:%s'%(user_info['data']['username'])
            print 'No. of Followers: %s'%(user_info['data']['counts']['followed_by'])
            print 'No. of People you are following:%s'%(user_info['data']['counts']['follows'])
            print'No. of Posts:%s'%(user_info['data']['counts']['media'])

        else:
            print'Users does not Exist!'

    else:
        print"Status code other than 200 received!"
