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
    # readin list of adjectives
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


    # boldtext = Markup(""+show_text+"!")

    with open('somefile.txt', 'a') as the_file:
        the_file.write(show_text+'\n')
    # final_text =
    my_names = ""
    count = 0
    with open('somefile.txt', 'r') as f:
        for line in f:
            count +=1
            my_names += line.rstrip()+", "
    # final_text = Markup(my_names+",")
    team_name = "testing"
    # array_of_dicts_names_scores = []
    # d ={
    #     'name': team_name,
    #     'score': 35,
    # }
    # array_of_dicts_names_scores.append(d)

    with open('teamname.txt', 'a') as the_file:
        the_file.write(team_name +"  "+ str(count)+ "\n")


    return render_template('index.html', boldtext=my_names , count=count)


open('somefile.txt', 'w').close()

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

