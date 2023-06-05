import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    
    #DELIVERABLE 1
    def __init__(self, name, breed, id = None):
        self.id = id
        self.name = name
        self.breed = breed

    #DELIVERABLE 2
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS dogs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                breed TEXT
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    
    #DELIVERABLE 3
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS dogs
        """

        CURSOR.execute(sql)
        CONN.commit()

    
    #DELIVERABLE 4
    def save(self):
        sql = """
            INSERT INTO dogs (name, breed)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.breed))
        CONN.commit()

    #DELIVERABLE 5
    # @classmethod
    # def create(cls, name, breed):
    #     dog = cls(name, breed)
    #     dog.save()
    #     return dog
    @classmethod        
    def create(cls, name, breed):
        dog = cls(name, breed)
        dog.save()
        return dog
        
    @classmethod
    def new_from_db(cls, row):
        dog = cls(
            name=row[1],
            breed=row[2],
            id=row[0]
        )

        return dog
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM dogs
        """

        return [cls.new_from_db(row) for row in CURSOR.execute(sql).fetchall()]

