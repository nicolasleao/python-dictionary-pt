import peewee

# Create the database connection
db = peewee.SqliteDatabase('database/dictionary.db')


class BaseModel(peewee.Model):
    """Base model class, all models will inherit this class"""
    text = peewee.CharField(unique=True)
    normalized_text = peewee.CharField()
    meaning = peewee.CharField()

    class Meta:
        # Indicates where the model should be stored
        database = db


class Verbo(BaseModel):
    """This class represents the 'Verbo' table"""


class Substantivo(BaseModel):
    """This class represents the 'Substantivo' table"""


class Adjetivo(BaseModel):
    """This class represents the 'Adjetivo' table"""


class Adverbio(BaseModel):
    """This class represents the 'Adverbio' table"""
