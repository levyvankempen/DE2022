import logging

from sqlalchemy.exc import SQLAlchemyError

from app import db


# for db_persist, see https://stackoverflow.com/questions/7889183/sqlalchemy-insert-or-update-example

def db_persist(func):
    def persist(*args, **kwargs):
        func(*args, **kwargs)
        try:
            db.session.commit()
            logging.info("success calling db func: " + func.__name__)
            return True
        except SQLAlchemyError as e:
            logging.error(e.args)
            db.session.rollback()
            return False
        finally:
            db.session.close()

    return persist


@db_persist
def insert_or_update(row_object):
    return db.session.merge(row_object)
