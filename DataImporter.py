# every time you see a line, if you see a new attribute, put it in
# check if it's already been inserted (if already in dictionary)
# need to make our own match_id b/c it's unreliable
# some people make a tourney id and the OG match id & make a product of this
# in the match table, use the "unreliable ID" and the tournament ID TOGETHER as your csv file
# change it to "cascade" when you delete tournament so you can do this

# integrity constraints:
# cascade & set null stuff
# triggers
# everything is done in the sql
# we can connect directly to dbeaver
# python only imports the data!!

# Kate Hynes and Pauline Cha

# Install with pip install mysql-connector-python (on some systems 'pip' might be called 'pip3')
import mysql.connector
import os
import glob
import csv
import datetime
import calendar

TOURNEY_ID = 0
TOURNEY_NAME = 1
SURFACE = 2
DRAW_SIZE = 3
TOURNEY_LEVEL = 4
TOURNEY_DATE = 5
MATCH_NUM = 6
WINNER_ID = 7
WINNER_SEED = 8
WINNER_ENTRY = 9
WINNER_NAME = 10
WINNER_HAND = 11
WINNER_HT = 12
WINNER_IOC = 13
WINNER_AGE = 14
LOSER_ID = 15
LOSER_SEED = 16
LOSER_ENTRY = 17
LOSER_NAME = 18
LOSER_HAND = 19
LOSER_HT = 20
LOSER_IOC = 21
LOSER_AGE = 22
SCORE = 23
BEST_OF = 24
ROUND = 25
MINUTES = 26
W_ACE = 27
W_DF = 28
W_SVPT = 29
W_1STIN = 30
W_1STWON = 31
W_2NDWON = 32
W_SVGMS = 33
W_BPSAVED = 34
W_BPFACED = 35
L_ACE = 36
L_DF = 37
L_SVPT = 38
L_1STIN = 39
L_1STWON = 40
L_2NDWON = 41
L_SVGMS = 42
L_BPSAVED = 43
L_BPFACED = 44
WINNER_RANK = 45
WINNER_RANK_POINTS = 46
LOSER_RANK = 47
LOSER_RANK_POINTS = 48

# Connect to MySQL
connection = mysql.connector.connect(
    user='root', password='123456', host='localhost', database='tennishw3')
cursor = connection.cursor()

# sets to store new IDs for each entity
# we might not even need these tbh... ?? not sure
players = set()
matches = set()
tourneys = set()
plays = set()

# player & tourn ids are reliable
# whenever you see a match you never see it again
# use auto increment
# can also concat tourn id and match id from csv

# don't put derived data in the db
# don't create


def convertDate(date):
    year = date[0:4]
    month = calendar.month_name[int(date[4:6])] + ' '
    day = date[6:8] + ' '
    formatted_date = month + day + year
    return datetime.datetime.strptime(formatted_date, '%B %d %Y').strftime('%Y-%m-%d')


def insertPlayer(id, name, country, hand, height):
    query_string = "INSERT INTO player VALUES (%s, %s, %s, %s, %s)"
    if name == '':
        name = None
    if country == '':
        country = None
    if hand == '':
        hand = None
    if height == '':
        height = None
    try:
        cursor.execute(query_string, (id, name, country, hand, height))
    except mysql.connector.Error as error_descriptor:
        print("Failed inserting tuple: {}".format(error_descriptor))


def insertTourney(id, name, level, date):
    query_string = "INSERT INTO tournament VALUES (%s, %s, %s, %s)"
    if name == '':
        name = None
    if level == '':
        level = None
    if date == '':
        date = None
    else:
        date = convertDate(date)
    try:
        cursor.execute(query_string, (id, name, level, date))
    except mysql.connector.Error as error_descriptor:
        print("Failed inserting tuple: {}".format(error_descriptor))


def insertMatchInfo(match_id, tourney_id, surface, score, num_sets):
    query_string = "INSERT INTO matchinfo VALUES (%s, %s, %s, %s, %s)"
    if tourney_id == '':
        tourney_id = None
    if surface == '':
        surface = None
    if score == '':
        score = None
    if num_sets == '':
        num_sets = None
    try:
        cursor.execute(query_string, (match_id, tourney_id,
                   surface, score, num_sets))
    except mysql.connector.Error as error_descriptor:
        print("Failed inserting tuple: {}".format(error_descriptor))


def insertPlays(match_id, player_id, win_or_lose, ace, df, fstIn, first_won, second_won):
    query_string = "INSERT INTO plays VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    if win_or_lose == '':
        win_or_lose = None
    if ace == '':
        ace = None
    if df == '':
        df = None
    if fstIn == '':
        fstIn = None
    if first_won == '':
        first_won = None
    if second_won == '':
        second_won = None
    try:
        cursor.execute(query_string, (match_id, player_id,
                   win_or_lose, ace, df, fstIn, first_won, second_won))
    except mysql.connector.Error as error_descriptor:
        print("Failed inserting tuple: {}".format(error_descriptor))

# for all the files in the csv directory
# filenum = 0
# winner = 0
# loser = 0
# match_id_len = 0
# longest_match_id = ''
# tourney_id_len = 0
# longest_tourney_id = ''
# score_len = 0
# longest_score = ''
for filename in glob.glob("tennis_atp-master/*.csv"):
    file = open(filename)
    csvreader = csv.reader(file)
    i = 0
    for row in csvreader:
        if i != 0:
            # Player
            winner_id = row[WINNER_ID]
            if (winner_id not in players):
                insertPlayer(winner_id, row[WINNER_NAME], row[WINNER_IOC],
                             row[WINNER_HAND], row[WINNER_HT])
                players.add(winner_id)
            loser_id = row[LOSER_ID]
            if(loser_id not in players):
                insertPlayer(loser_id, row[LOSER_NAME], row[LOSER_IOC],
                             row[LOSER_HAND], row[LOSER_HT])
                players.add(loser_id)
            # Tourney
            tourney_id = row[TOURNEY_ID]
            # if (len(tourney_id) > tourney_id_len):
            #     tourney_id_len = len(tourney_id)
            #     longest_tourney_id = tourney_id
            if (tourney_id not in tourneys):
                insertTourney(tourney_id, row[TOURNEY_NAME],
                              row[TOURNEY_LEVEL], row[TOURNEY_DATE])
                tourneys.add(tourney_id)
            # Matches
            match_id = tourney_id + row[MATCH_NUM]
            # if (len(match_id) > match_id_len):
            #     match_id_len = len(match_id)
            #     longest_match_id = match_id
            # if (len(row[SCORE]) > score_len):
            #     score_len = len(row[SCORE])
            #     longest_score = row[SCORE]
            if (match_id not in matches):
                insertMatchInfo(
                    match_id, tourney_id, row[SURFACE], row[SCORE], row[BEST_OF])
                matches.add(match_id)
            # Plays
            w_plays_key = (match_id, winner_id)
            if (w_plays_key not in plays):
                insertPlays(match_id, winner_id, 'W',
                            row[W_ACE], row[W_DF], row[W_1STIN], row[W_1STWON], row[W_2NDWON])
                plays.add(w_plays_key)
            l_plays_key = (match_id, loser_id)
            if (l_plays_key not in plays):
                insertPlays(match_id, loser_id, 'L',
                            row[L_ACE], row[L_DF], row[L_1STIN], row[L_1STWON], row[L_2NDWON])
                plays.add(l_plays_key)
        i += 1
    connection.commit()
    file.close()
    # print(filenum)
    # filenum += 1
cursor.close()
# print("match id longest ", match_id_len, "tourney id longest ", tourney_id_len, "score longest ", score_len)
# print("match id longest ", longest_match_id, "tourney id longest ", longest_tourney_id, "score longest ", longest_score)


# # # to print first line of csv
# # file = open('tennis_atp-master/atp_matches_1968.csv')
# csvreader = csv.reader(file)
# row1 = next(csvreader)
# print(row1)
