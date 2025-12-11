from sqlite3 import ProgrammingError
import mariadb
from db import get_connection

def call_procedure(proc_name, params=()):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(f"CALL {proc_name}({','.join(['?'] * len(params))})", params)

        while True:
            try:
                cursor.fetchall()
            except mariadb.ProgrammingError:
                pass
            if not cursor.nextset():
                break

        conn.commit()
        return True

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()
    
def add_flower(flowerid, namn, bildlank, beskrivning):
    return call_procedure("add_flower", (flowerid, namn, bildlank, beskrivning))

def remove_all():
    return call_procedure("remove_all_flowers")

def remove_one(flowerid):
    return call_procedure("remove_flower", (flowerid,))

def show_one(namn):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("CALL show_flower(?)", (namn,))

        # 1) Hämta det första resultatet (datan du vill ha)
        result = cursor.fetchall()

        # 2) Töm alla extra resultsets från stored proceduren
        while cursor.nextset():
            try:
                cursor.fetchall()
            except mariadb.ProgrammingError:
                pass

        # 3) Commit
        conn.commit()

        return result

    except Exception as e:
        # 4) Rollback måste också tömma alla sets först
        while cursor.nextset():
            try:
                cursor.fetchall()
            except:
                pass
        conn.rollback()
        raise e

    finally:
        cursor.close()
        conn.close()