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
