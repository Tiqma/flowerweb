from sqlite3 import ProgrammingError
import mariadb
from db import get_connection

def add_flower(flowerid, namn, bildlank, beskrivning):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("CALL add_flower(%s, %s, %s, %s)", (flowerid, namn, bildlank, beskrivning))

        # Läs och ignorera alla resultset
        while True:
            try:
                cursor.fetchall()
            except mariadb.ProgrammingError:
                pass
            if not cursor.nextset():
                break

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def remove_all():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("CALL remove_all_flowers()")

        while True:
            try:
                cursor.fetchall()
            except mariadb.ProgrammingError:
                pass
            if not cursor.nextset():
                break

        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()

def remove_one(flowerid):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("Call remove_flower(?)", (flowerid,))

        while True:
            try:
                cursor.fetchall()
                
            except mariadb.ProgrammingError:
                pass
            
            if not cursor.nextset():
                break
        
        conn.commit()
        return True
    
    except Exception as e:
        conn.rollback()
        raise e
    
    finally: 
        cursor.close()
        conn.close()

