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
player_id = set()
# map for match id's
match_id = set()
# map for tourney id's
tourney_id = set()


def insertPlayer(name, country, hand, height):
    query_string = "INSERT INTO player VALUES (%s, %s, %s, %s)"
    # check execute statement!
    cursor.execute(query_string, (name, country, hand, height))


# for all the files in the csv directory
for filename in glob.glob("tennis_atp-master/*.csv"):
    print('hi')
    file = open(filename)
    csvreader = csv.reader(file)
    for row in csvreader:
        # figure out which columns to select for which tables and what attributes for Player
        winner_name = row[WINNER_NAME]
        winner_height = row[WINNER_HT]
        playerArray = (winner_name, winner_height)
        if (playerArray not in player_id):
            insertPlayer(row[WINNER_NAME], row[WINNER_IOC],
                         row[WINNER_HAND], row[WINNER_HT])
            player_id.add(playerArray)
        loser_name = row[LOSER_NAME]
        loser_height = row[LOSER_HT]
        playerArray = [loser_name, loser_height]
        if(playerArray not in player_id):
            insertPlayer(row[LOSER_NAME], row[LOSER_IOC],
                         row[LOSER_HAND], row[LOSER_HT])

    file.close()

# # to print first line of csv
# file = open('tennis_atp-master/atp_matches_1968.csv')
# csvreader = csv.reader(file)
# row1 = next(csvreader)
# print(row1)
