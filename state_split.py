# -*- coding: utf-8 -*-
"""
Created on Wed May 28 14:40:13 2014

@author: jon
"""
import psycopg2
from psycopg2.extras import RealDictCursor
import csv

credentials = {'host':'localhost',
               'database':'medicare',
               'user':'postgres',
               'password':'data'}
 
db = psycopg2.connect(**credentials)
db.cursor_factory = RealDictCursor
cursor = db.cursor()
sql = "select distinct nppes_provider_state from opendata"
cursor.execute(sql)
result = cursor.fetchall()


for state in result:
    sql = 'select * from opendata where nppes_provider_state=\''+state['nppes_provider_state']+'\';'
    cursor.execute(sql)
    result = cursor.fetchall()
    
    with open('/home/jon/DMN/Scripts/Archive/2014_05-Medicare/Medicare-metrics-data/'+state['nppes_provider_state']+'.csv', 'wb') as f:  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, result[0].keys(),delimiter=',', quotechar='"')
        w.writeheader()
        for row in result:
            w.writerow(row)
    



cursor.close()
db.close()