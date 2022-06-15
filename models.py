from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    DateTimeField,
)
from datetime import datetime as dt

db = SqliteDatabase("sano.db")
import shortuuid


class BaseModel(Model):
    id = CharField(primary_key=True, default=lambda: shortuuid.uuid())
    created_at = DateTimeField(default=lambda: dt.now())
    updated_at = DateTimeField(default=lambda: dt.now())

    def save(self, *args, **kwargs):
        self.updated_at = dt.now()
        return super(BaseModel, self).save(*args, **kwargs)

    def save_no_update(self, *args, **kwargs):
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        database = db


class User(BaseModel):
    email = CharField()
    name = CharField(null=True)
    password_hash = CharField(255, null=True)


class Order(BaseModel):
    name = CharField()
    description = CharField()
    quantity = CharField()
    total = CharField()


def create_tables():
    with db:
        db.create_tables([User, Order], safe=True)
