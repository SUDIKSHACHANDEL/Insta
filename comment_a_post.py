import requests
from constants import BASE_URL, APP_ACCESS_TOKEN
from get_user_post import get_user_post
from get_post_id import get_post_id
insta_username = "jyotithakur15111"
def post_a_comment(insta_username):
  media_id = get_post_id(insta_username)
  message = raw_input("Enter your Message: ")
  payload = {"access_token": APP_ACCESS_TOKEN, 'text': message}
  # print media_id
  request_url = (BASE_URL +'media/%s/comments') % (media_id)

  print 'POST request url : %s' % (request_url)
  post_comment = requests.post(request_url, payload).json()

  if post_comment['meta']['code'] == 200:
    print "Post comment Successfully"
  else:
    print "Unable to comment on post"

  exit()

post_a_comment(insta_username='jyotithakur15111')
