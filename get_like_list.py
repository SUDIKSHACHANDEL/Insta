import requests
from constants import BASE_URL, APP_ACCESS_TOKEN
from get_post_id import get_post_id
insta_username = 'shramatanu9878'
def like_list(insta_username):
  media_id = get_post_id(insta_username)

  request_url = (BASE_URL +'media/%s/likes?access_token=%s') % (media_id,APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  get_a_like = requests.get(request_url).json()
  print get_a_like
  if get_a_like['meta']['code'] == 200:
    print("hgghgh")
    print"Media with media id '{}' is liked by following users:" . format(media_id)
    for (index,user_likes) in enumerate(get_a_like['data']):
        print"{}. {} ({}) - {}".format(index+1,user_likes['full_name'],user_likes['id'],user_likes['username'])


  else:
    print("There is no Like regarding this post.")


like_list(insta_username = 'sharmatanu9878')