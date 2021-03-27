import psycopg2


class DB_Manager:
    def __init__(self):
        self.conn = psycopg2.connect(database='scappdb',
                    user='postgres',
                    password='jvjye4b66k9ermx7',
                    host='localhost',
                    port='5432')

        self.cursor = self.conn.cursor()

    def init_tables(self):
        query = '''CREATE TABLE IF NOT EXISTS Registration(
            id (int) PRIMARY KEY,
            first-name (TEXT),
            last-name (TEXT),
            birth-date (DATE),
            age (int),
            school-name (TEXT),
            standard (decimal),
            village (TEXT),
            sub-county (TEXT),
            church (TEXT),
            childrens-Home (TEXT),
            care-taker (TEXT),
            father (TEXT),
            mother (TEXT),
            care-taker-phone VARCHAR(14),
            alternate-phone VARCHAR(14))'''
        self.cursor.execute(query)
        self.conn.commit()

        query = '''CREATE TABLE IF NOT EXISTS Screening(
            id (int) PRIMARY KEY FOREIGN KEY REFERENCES Registration(id),
            date (DATETIME),
            location (TEXT),
            anterior-mitral-valve-leaflet-thickness SET(Normal, Abnormal),
            posterior-mitral-valve-leaflet-thickness SET(Normal, Thickened),
            posterior-mitral-valve-mobility SET(Normal, Reduced),
            aortic-valve-thickness SET(Normal, Thickened),
            mitral-valve-function SET(Normal, Abnormal),
            aortic-valve-function SET(Normal, Abnormal),
            anterior-mitral-valve-leaflet-mobility SET(Normal, Abnormal),
            mitral-regurgitation SET(">1.5cm", ">1cm"),
            aortic-regurgitation BOOL,
            comments (TEXT))'''
        self.cursor.execute(query)
        self.conn.commit()

        query = '''CREATE TABLE IF NOT EXISTS PCN(
            id (int) PRIMARY KEY (matches ID from registration table),
            date (DATETIME),
            location (TEXT),
            worsening-exercise-intolerance (BOOL),
            poor-pcn-reaction (BOOL),
            injection-given (BOOL),
            comments (TEXT))'''
        
        self.cursor.execute(query)
        self.conn.commit()

    def submit_registration(self, reg_info):
        query = '''INSERT INTO Registration
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        self.cursor.execute(query, (reg_info["id"],
                                reg_info["first-name"],
                                reg_info["last-name"],
                                reg_info["birth-date"],
                                reg_info["age"],
                                reg_info["school-name"],
                                reg_info["standard"],
                                reg_info["village"],
                                reg_info["sub-county"],
                                reg_info["church"],
                                reg_info["childrens-Home"],
                                reg_info["care-taker"],
                                reg_info["father"],
                                reg_info["mother"],
                                reg_info["care-taker-phone"],
                                reg_info["alternate-phone"]))
        self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    db = DB_Manager()
    db.init_tables()
    
    