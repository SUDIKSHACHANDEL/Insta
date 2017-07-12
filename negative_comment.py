import requests,urllib
from constants import BASE_URL,APP_ACCESS_TOKEN
from textblob import TextBlob
#Here NaiveBayes.... import to analyse what type of comments it is:
from textblob.sentiments import NaiveBayesAnalyzer
from get_user_id import get_user_id

#Here we import post_id to get the media_id... for request url.
from get_post_id import get_post_id

insta_username='jyotithakur15111'

# A function to define the sentiment analyse and delete the negative comments. It also shows the list of positive and negative comments.

def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        # if there is some data or info in the comment box.
        if len(comment_info['data']):
            #This shows that  how to delete the negative comments from any post :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)

                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print 'Yee... ! Negative comment is successfully deleted!\n'
                    else:
                        print 'Sorry....! Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'


