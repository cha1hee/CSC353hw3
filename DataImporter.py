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
import lxml
import lxml.etree
import datetime

# Connect to MySQL
connection = mysql.connector.connect(
    user='root', password='123456', host='localhost')
cursor = connection.cursor()

# initialize senator_ids as set for O(1) time to check if senator is seen before
senator_ids = set()


# Convert the vote option into a single-character representation
def convertVoteCast(vote_cast):
    if vote_cast == 'Yea':
        return 'Y'

    if vote_cast == 'Nay':
        return 'N'

    return 'A'


# This converts the date obtained from the XML files into a SQL date string
def convertDate(date):
    date_split = date.split(',')
    day = date_split[0] + date_split[1]

    return datetime.datetime.strptime(day, '%B %d %Y').strftime('%Y-%m-%d')


# Insert values into VOTE_CAST table
def insertVoteCast(cursor, senator_id, congress_number, congress_session, vote_number, vote_option):
    query_string = "INSERT INTO vote_cast VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query_string, (senator_id, congress_number,
                   congress_session, vote_number, vote_option))


# Insert values into VOTES table
def insertVote(cursor, congress_number, congress_session, vote_year, vote_date, vote_number):
    query_string = "INSERT INTO votes VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query_string, (congress_number,
                   congress_session, vote_year, vote_date, vote_number))  # check execute statement!


# Insert values into SENATOR table
def insertSenator(cursor, first_name, last_name, party, state, senator_id):
    query_string = "INSERT INTO senator VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query_string, (first_name,
                   last_name,  party, state, senator_id))


# Data Definition
# Read the 'Schema.sql' file into the 'schema_string' variable
f = open("Schema.sql", "r")
schema_string = f.read()

# Run the contents of 'Schema.sql', creating a schema (deleting previous incarnations),
# and creating the three relations mentioned in the handout.
try:
    for result in cursor.execute(schema_string, multi=True):
        pass
except mysql.connector.Error as error_descriptor:
    if error_descriptor.errno == mysql.connector.errorcode.ER_TABLE_EXISTS_ERROR:
        print("Table already exists: {}".format(error_descriptor))
    else:
        print("Failed creating schema: {}".format(error_descriptor))
    exit(1)

# After running the contents of 'Schema.sql', you have to do again
# a USE SenatorVotes in your connection before adding the tuples.
try:
    cursor.execute("USE {}".format("SenatorVotes"))
except mysql.connector.Error as error_descriptor:
    print("Failed using database: {}".format(error_descriptor))
    exit(1)

cursor.close()

# Data Manipulation
cursor = connection.cursor()
for filename in glob.glob("XML/*.xml"):
    tree = lxml.etree.parse(filename)
    # Extract the attributes of Vote
    congress_number = tree.xpath("//congress")[0].text
    congress_session = tree.xpath("//session")[0].text
    year = tree.xpath("//congress_year")[0].text
    date = convertDate(tree.xpath("//vote_date")[0].text)
    vote_number = tree.xpath("//vote_number")[0].text
    insertVote(cursor, congress_number,
               congress_session, year, date, vote_number)
    # Find all members
    members = tree.xpath("//member")
    for member in members:
        senator_id = member.xpath("lis_member_id")[0].text
        vote_option = convertVoteCast(member.xpath("vote_cast")[0].text)
        # Parse other attributes of senator if not seen before
        if (senator_id not in senator_ids):
            senator_ids.add(senator_id)
            last_name = member.xpath("last_name")[0].text
            first_name = member.xpath("first_name")[0].text
            party = member.xpath("party")[0].text
            state = member.xpath("state")[0].text
            insertSenator(cursor, first_name, last_name,
                          party, state, senator_id)
        insertVoteCast(cursor, senator_id, congress_number,
                       congress_session, vote_number, vote_option)
    connection.commit()
cursor.close()

connection.close()
