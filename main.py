from flask import Flask, request, render_template
import random, sqlite3
from flask import Markup

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index5.html')

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
    # my_nam
    with open('somefile.txt', 'r') as f:
        # for line in f:
        #     count +=1
        #     my_names += line.rstrip()+", "
        my_names= [line.rstrip() for line in f]
        count = len(my_names)
    # final_text = Markup(my_names+",")
    team_name = "testing"
    # array_of_dicts_names_scores = []
    # d ={
    #     'name': team_name,
    #     'score': 35,
    # }
    # array_of_dicts_names_scores.append(d)

    #with open('teamname.txt', 'a') as the_file:
        # the_file.write(team_name +"  "+ str(count)+ "\n")
    #    the_file.write(team_name +"\n")


    conn = sqlite3.connect('data.sqlite')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Teams
    (id INTEGER PRIMARY KEY, teamname TEXT UNIQUE, score INTEGER)''')

    cur.execute('SELECT * FROM Teams ORDER BY id DESC LIMIT 1')
    try:
        row = cur.fetchone()
        player = row[1]
        score = row[2]
        score+=1
        #print(score)

        cur.execute('UPDATE Teams SET score = ? WHERE teamname = ?', (score, player))

    except:
        score=1
        cur.execute('INSERT OR IGNORE INTO Teams (teamname, score) VALUES (?, ?)', ("UNNAMED", score))


    conn.commit()
    cur.close()



    return render_template('index5.html', my_names=my_names , count=count)

# count = 0
# with open('somefile.txt', 'r') as f:
#     for line in f:
#         count +=1



#
@app.route('/clear', methods=['POST'])
def my_form_post2():
    # removing somefile
    open('somefile.txt', 'w').close()

    # create tuples
    scores=[]
    names=[]
    text = request.form['teamName']

    conn = sqlite3.connect('data.sqlite')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Teams
        (id INTEGER PRIMARY KEY, teamname TEXT UNIQUE, score INTEGER)''')

    cur.execute('SELECT * FROM Teams ORDER BY score DESC LIMIT 3')
    for row in cur:
        scores.append(row[2])
        names.append(row[1]+" "+str(row[2]))





    cur.execute('SELECT score FROM Teams WHERE teamname=? LIMIT 1', (text,))
    try:
        row = cur.fetchone()
        score = row[0]

    except:
        score = 0
        cur.execute('INSERT OR IGNORE INTO Teams (teamname, score) VALUES (?, ?)', (text, score))

    conn.commit()
    cur.close()

    # count = 0
    # with open('somefile.txt', 'r') as f:
    #     for line in f:
    #         count += 1

   # with open('teamname.txt', 'r') as f:
   #     for line in f:
   #         if (line == "testing"):
   #             t1 =+ 1
   #         if (line == "cool dudes"):
   #             t2 =+1
   #         if (line == "panthers"):
   #             t3 =+1


    # text = request.form['firstname2']
    return render_template('index5.html', name =text, scores=scores, names=names)


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

