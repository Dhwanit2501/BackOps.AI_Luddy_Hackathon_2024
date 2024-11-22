from typing import Annotated
from fastapi import Depends
import sqlalchemy
from database import SessionDep
from models import KeyValue, KeyValueUpdate
from exceptions import KeyAlreadyExist, KeyNotFound, ValueIsEmpty
import utils
from logger import app_logger

def createKeyValue(key: str, value: str, session: SessionDep):
    print(value)
    if not value:
        raise ValueIsEmpty(key=key)
    try:
        current_time = updated_time = utils.get_current_time_in_str()
        db_key_value = KeyValue(key=key, value=value, created_time=current_time, updated_time=updated_time)
        key_value = KeyValue.model_validate(db_key_value)
        session.add(key_value)
        session.commit()
        app_logger.info(f"Inserted key:{key} with value: {value}")
    # If key is already exist
    except sqlalchemy.exc.IntegrityError:
        raise KeyAlreadyExist(key=key)

def updateKeyValue(key: str, value: str, session: SessionDep):
    key_value_db = session.get(KeyValue, key)

    if not key_value_db:
        raise KeyNotFound(key=key, op="Update")
    
    key_value = KeyValueUpdate(key=key, value=value, updated_time=utils.get_current_time_in_str())

    key_value_db.sqlmodel_update(key_value)
    session.add(key_value_db)
    session.commit()
    app_logger.info(f"Updated existing key: {key} with new value: {value}")

def deleteKeyValue(key: str, session: SessionDep):
    key_value = session.get(KeyValue, key)

    if not key_value:
        raise KeyNotFound(key=key, op="Delete")
    
    session.delete(key_value)
    session.commit()
    app_logger.info(f"Deleted given key: {key}")