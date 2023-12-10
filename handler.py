import json
import psycopg2

def articulo(event, context):
   
    db_host = "database-1.coynvh3bqnjq.us-east-1.rds.amazonaws.com"
    db_port = 5432
    db_name = "myDatabase"
    db_user = "postgres"
    db_pass = "Gordis2019"
    db_table = "articulo"
   
    conn = None
    conn = psycopg2.connect("dbname={} user={} host={} password={}".format(db_name,db_user,db_host,db_pass))

    query = "select * from articulo"
   
    cursor = conn.cursor()
    cursor.execute(query)
    raw = cursor.fetchall()
   
    result = []
    for line in raw:
        result.append(line)
       
    conn.close()
   
    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response
