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

# Kate Hynes and Pauline Cha read chapters 1-3 of the textbook

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

# map for player id's
players = {}
# map for match id's
matches = {}
# map for tourney id's
tourneys = {}


def convertDate(date):
    year = date[0:4]
    month = calendar.month_name[int(date[4:6])] + ' '
    dateDay = date[6:8] + ' '
    day = month + dateDay + year
    return datetime.datetime.strptime(day, '%B %d %Y').strftime('%Y-%m-%d')


def createID(strHint, key, mapID):
    idNum = len(mapID)+1
    mapID[key] = strHint + str(idNum)
    return strHint + str(idNum)


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
    cursor.execute(query_string, (id, name, country, hand, height))


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
    cursor.execute(query_string, (id, name, level, date))


def insertMatchInfo(match_num, tourney_id, surface, score, num_sets):
    query_string = "INSERT INTO matchinfo VALUES (%s, %s, %s, %s, %s)"
    if match_num == '':
        match_num = None
    if tourney_id == '':
        tourney_id = None
    if surface == '':
        surface = None
    if score == '':
        score = None
    if num_sets == '':
        num_sets = None
    cursor.execute(query_string, (match_num, tourney_id,
                   surface, score, num_sets))


def insertPlays(match_num, player_id, win_or_lose, ace, df, fstIn):
    query_string = "INSERT INTO plays VALUES (%s, %s, %s, %s, %s, %s)"
    if match_num == '':
        match_num = None
    if player_id == '':
        player_id = None
    if win_or_lose == '':
        win_or_lose = None
    if ace == '':
        ace = None
    if df == '':
        df = None
    if fstIn == '':
        fstIn = None
    cursor.execute(query_string, (match_num, player_id,
                   win_or_lose, ace, df, fstIn))


# for all the files in the csv directory
for filename in glob.glob("tennis_atp-master/*.csv"):
    file = open(filename)
    csvreader = csv.reader(file)
    i = 0
    for row in csvreader:
        if i != 0:
            # Player
            winner_name = row[WINNER_NAME]
            winner_height = row[WINNER_HT]
            winner_key = (winner_name, winner_height)
            if (winner_key not in players):
                winner_id = createID('p', winner_key, players)
                insertPlayer(winner_id, row[WINNER_NAME], row[WINNER_IOC],
                             row[WINNER_HAND], row[WINNER_HT])
            loser_name = row[LOSER_NAME]
            loser_height = row[LOSER_HT]
            loser_key = (loser_name, loser_height)
            if(loser_key not in players):
                loser_id = createID('p', loser_key, players)
                insertPlayer(loser_id, row[LOSER_NAME], row[LOSER_IOC],
                             row[LOSER_HAND], row[LOSER_HT])
            # Tourney
            tourney_name = row[TOURNEY_NAME]
            tourney_date = row[TOURNEY_DATE]
            tourney_key = (tourney_name, tourney_date)
            if (tourney_key not in tourneys):
                tourney_id = createID('t', tourney_key, tourneys)
                insertTourney(tourney_id, row[TOURNEY_NAME],
                              row[TOURNEY_LEVEL], row[TOURNEY_DATE])
            # Matches
            match_key = (tourney_name, winner_name, loser_name)
            if (match_key not in matches):
                match_num = createID('m', match_key, matches)
                insertMatchInfo(
                    match_num, tourney_id, row[SURFACE], row[SCORE], row[BEST_OF])
            # Plays
            insertPlays(match_num, winner_id, 'W',
                        row[W_ACE], row[W_DF], row[W_1STIN])
            insertPlays(match_num, loser_id, 'L',
                        row[L_ACE], row[L_DF], row[L_1STIN])
        i += 1
    connection.commit()
    file.close()
cursor.close()


# # to print first line of csv
# file = open('tennis_atp-master/atp_matches_1968.csv')
# csvreader = csv.reader(file)
# row1 = next(csvreader)
# print(row1)
