# see. https://docs.djangoproject.com/en/4.0/topics/db/multi-db/
# router for DB

from django.conf import settings


class AppRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    write_db = settings.WRITER_DATABASE
    read_db = settings.READER_DATABASE
    db_list = {write_db, read_db}

    def db_for_read(self, model, **hints):
        return self.read_db

    def db_for_write(self, model, **hints):
        return self.write_db

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._state.db in self.db_list and obj2._state.db in self.db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
