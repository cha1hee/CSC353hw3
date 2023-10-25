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