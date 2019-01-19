from flask import Flask, request, render_template
import random
from flask import Markup

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['firstname']
    # processed_text = text.lower()
    first_letter = text[0].lower()
    text=text.capitalize()
    print(first_letter)
    my_list_of_same_letter_adjectives = []

    with open('adjectives.txt', 'r') as f:
        for line in f:
            for word in line.split():
                if (first_letter == word[0]):  # if first letter is same as first letter from adjective list
                    # print(word)
                    # add the adjective to separate list
                    my_list_of_same_letter_adjectives.append(word.capitalize())

    # the random adjective pass to frontend
    random_adjective = random.choice(my_list_of_same_letter_adjectives)
    print(random_adjective)
    show_text= (random_adjective+ " " +text)
    boldtext = Markup("<b>"+show_text+"!<b>")

    return render_template( 'index.html', boldtext=boldtext  )



# first_letter = "w"
# # temporary first letter
# # this will become the first letter of the user
# # first_letter= 'w'
# #
# my_list_of_same_letter_adjectives = []
#
# with open('adjectives.txt','r') as f:
#     for line in f:
#         for word in line.split():
#            if(first_letter == word[0]):# if first letter is same as first letter from adjective list
#                # print(word)
#                # add the adjective to seperate list
#                my_list_of_same_letter_adjectives.append(word)
#
# # the random adjective pass to frontend
# random_adjective = random.choice(my_list_of_same_letter_adjectives)
# print(random_adjective)

