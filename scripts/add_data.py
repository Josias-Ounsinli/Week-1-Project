import os
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error

def DBConnect(dbName=None):
    """

    Parameters
    ----------
    dbName :
        Default value = None)

    Returns
    -------

    """
    conn = mysql.connect(host='localhost', user='root', password=os.getenv('Djossouns@9808'),
                         database=dbName, buffered=True)
    cur = conn.cursor()
    return conn, cur

def emojiDB(dbName: str) -> None:
    conn, cur = DBConnect(dbName)
    dbQuery = f"ALTER DATABASE {dbName} CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;"
    cur.execute(dbQuery)
    conn.commit()

def createDB(dbName: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    dbName :
        str:
    dbName:str :


    Returns
    -------

    """
    conn, cur = DBConnect()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {dbName};")
    conn.commit()
    cur.close()

def createTables(dbName: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    dbName :
        str:
    dbName:str :


    Returns
    -------

    """
    conn, cur = DBConnect(dbName)
    sqlFile = "/home/jds98/10 Academy/Week 1/Week-1-Project/scripts/final_table.sql"
    fd = open(sqlFile, 'r')
    readSqlFile = fd.read()
    fd.close()

    sqlCommands = readSqlFile.split(';')

    for command in sqlCommands:
        try:
            res = cur.execute(command)
        except Exception as ex:
            print("Command skipped: ", command)
            print(ex)
    conn.commit()
    cur.close()

    return


def insert_to_useranalytics_table(dbName: str, df: pd.DataFrame, table_name: str) -> None:
    """

    Parameters
    ----------
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName :
        str:
    df :
        pd.DataFrame:
    table_name :
        str:
    dbName:str :

    df:pd.DataFrame :

    table_name:str :


    Returns
    -------

    """
    conn, cur = DBConnect(dbName)

    for _, row in df.iterrows():
        sqlQuery = f"""INSERT INTO {table_name} (`MSISDN/Number`, `sessions frequency`,`Dur. (ms)`, `Total DL (Bytes)`,
                `Total UL (Bytes)`, `Avg RTT DL (ms)`, `Avg RTT UL (ms)`,
                `Handset Type`, `Avg Bearer TP DL (kbps)`, `Avg Bearer TP UL (kbps)`,
                `Social Media Total (Bytes)`, `Google Total (Bytes)`, `Email Total (Bytes)`, `Youtube Total (Bytes)`,
                `Netflix Total (Bytes)`, `Gaming Total (Bytes)`, `Other Total (Bytes)`,
                `Engagement scores`, `Experience scores`, `Satisfaction scores`)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19])

        try:
            # Execute the SQL command
            cur.execute(sqlQuery, data)
            # Commit your changes in the database
            conn.commit()
            print("Data Inserted Successfully")
        except Exception as e:
            conn.rollback()
            print("Error: ", e)
    return

def db_execute_fetch(*args, many=False, tablename='', rdf=True, **kwargs) -> pd.DataFrame:
    """

    Parameters
    ----------
    *args :

    many :
         (Default value = False)
    tablename :
         (Default value = '')
    rdf :
         (Default value = True)
    **kwargs :


    Returns
    -------

    """
    connection, cursor1 = DBConnect(**kwargs)
    if many:
        cursor1.executemany(*args)
    else:
        cursor1.execute(*args)

    # get column names
    field_names = [i[0] for i in cursor1.description]

    # get column values
    res = cursor1.fetchall()

    # get row count and show info
    nrow = cursor1.rowcount
    if tablename:
        print(f"{nrow} recrods fetched from {tablename} table")

    cursor1.close()
    connection.close()

    # return result
    if rdf:
        return pd.DataFrame(res, columns=field_names)
    else:
        return res


if __name__ == "__main__":
    createDB(dbName='useranalytics')
    emojiDB(dbName='useranalytics')
    createTables(dbName='useranalytics')

    df = pd.read_csv('/home/jds98/10 Academy/Week 1/Week-1-Project/data/Final table.csv')

    insert_to_useranalytics_table(dbName='useranalytics', df=df, table_name='Userinformation')