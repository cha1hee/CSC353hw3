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

# Connect to MySQL
connection = mysql.connector.connect(
    user='root', password='123456', host='localhost')
cursor = connection.cursor()

# map for player id's
player_id = map(name, )
# map for match id's

# map for tourney id's

# sample query_string from hw1:
# Insert values into VOTES table


def insertVote(id, name, country, hand, height):
    query_string = "INSERT INTO player VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query_string, (congress_number,
                   congress_session, vote_year, vote_date, vote_number))  # check execute statement!


# for all the files in the csv directory
directory = 'tennis_atp-master'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # if the file exists then proceed with reading in the csv
    if os.path.isfile(f):
        file = open(f)
        csvreader = csv.reader(file)

        for row in csvreader:
            # figure out which columns to select for which tables and what attributes
            row
