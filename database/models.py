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


class Any(BaseModel):
    """This class represents the 'Any' table"""


class Verb(BaseModel):
    """This class represents the 'Verb' table"""


class Noun(BaseModel):
    """This class represents the 'Noun' table"""


class Adjective(BaseModel):
    """This class represents the 'Adjective' table"""


class Adverb(BaseModel):
    """This class represents the 'Adverb' table"""
