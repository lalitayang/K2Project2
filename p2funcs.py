#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 16:19:43 2018

@author: lalitayang
"""

def nfl_week_to_date(row):
    """ To convert NFL season, week, & day to a datetime"""
    
    ## The start date of the NFL season differs year to year.
    if row['season'] == 2011:
        start_date = datetime.strptime('2011-09-08', '%Y-%m-%d')
        
    if row['season'] == 2012:
        start_date = datetime.strptime('2012-09-05', '%Y-%m-%d')
        
    if row['season'] == 2013:
        start_date = datetime.strptime('2013-09-04', '%Y-%m-%d')
        
    if row['season'] == 2014:
        start_date = datetime.strptime('2014-09-04', '%Y-%m-%d')
        
    if row['season'] == 2015:
        start_date = datetime.strptime('2015-09-10', '%Y-%m-%d')
      
    ## Data has missing week numbers    
    try: 
        return start_date + relativedelta(weeks=int(row['week_num']), days=int(row['day_of_week']))
    except:
        return start_date + relativedelta(weeks=int(row['week_num']))
 
def convert_NFL_weekday(df, col):
    """convert weekday name to number. NFL season starts on Thursdays """
    weekday_dict = {'Thursday' : 0,
                    'Sunday'   : 3,
                    'Monday'   : 4}
    
    df[col] = df[col].map(weekday_dict)
    df['date'] = df.apply(lambda x: nfl_week_to_date(x), axis=1)