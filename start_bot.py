import requests,urllib
from constants import APP_ACCESS_TOKEN,BASE_URL
from self_info import self_info
from get_user_info import get_user_info
from get_own_post import get_own_post
from get_user_post import get_user_post
from get_like_list import get_like_list
from like_a_post import like_a_post
from get_comment_list import get_comment_list
from comment_a_post import post_a_comment
from negative_comment import delete_negative_comment
def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot.........!'
        print 'Your menu options are as follow. Please choose any one of the option.........:\n\t\t\t\t\t'
        print "1.Get your own details\n"
        print "2.Get details of a user by username\n"
        print "3.Get your own recent post\n"
        print "4.Get the recent post of a user by username\n"
        print "5.Get a list of people who have liked the recent post of a user\n"
        print "6.Like the recent post of a user\n"
        print "7.Get a list of comments on the recent post of a user\n"
        print "8.Make a comment on the recent post of a user\n"
        print "9.Delete negative comments from the recent post of a user\n"
        print "10.Exit\n\t\t\t\t"

        choice = raw_input("Enter you choice: ")
        if choice == "1":
            self_info()
        elif choice == "2":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "3":
            get_own_post()
        elif choice == "4":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice=="5":
           insta_username = raw_input("Enter the username of the user: ")
           get_like_list(insta_username)
        elif choice=="6":
           insta_username = raw_input("Enter the username of the user: ")
           like_a_post(insta_username)
        elif choice=="7":
           insta_username = raw_input("Enter the username of the user: ")
           get_comment_list(insta_username)
        elif choice=="8":
           insta_username = raw_input("Enter the username of the user: ")
           post_a_comment(insta_username)
        elif choice=="9":
           insta_username = raw_input("Enter the username of the user: ")
           delete_negative_comment(insta_username)
        elif choice == "10":
            exit()
        else:
            print "wrong choice"

start_bot()