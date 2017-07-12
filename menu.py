import requests
from constants import APP_ACCESS_TOKEN, BASE_URL
from get_own_post import get_own_post
from self_info import self_info
from get_user_post import get_users_post
spy_name = "Sudiksha"
spy_salutation= "Ms."
spy_name =  spy_salutation + " "+ spy_name
def start_insta():






        print " Welcome!........ " + spy_name + " You are connected with instabot......!"

        show_menu = True

        while show_menu:
            print('Below mentioned your options.Please choose any one of the option:->\n\t\t\t ')
            menu_choices = "\n What do you want to do? \n \t 1. You Want Self Information \n \t 2. Want to get Own Post \n \t 3. Get user post \n \t 4. Get user Information\n \t 5. Like a post\n \t 6. Comment a post\n \t 7.  Close Application \n \t\t\t\t\t >>>Please enter one of the option from the above.......:->>>"
            menu_choice = raw_input( menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    #self_info()
                elif menu_choice == 2:
                    #get_own_post()
                elif menu_choice == 3:
                    #get_user_post()
                elif menu_choice == 4:
                    #get_user_info()
                elif menu_choice == 5:
                    #Like_a_post()
                else:
                    show_menu = False
            else:
                print 'Please enter  one of the option from above........? '

start_insta()