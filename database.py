# -*- coding: utf-8 -*-
"""Database module, including the SQLAlchemy databasegfd object and DB-related utilities."""
import datetime
from sqlalchemy.orm import relationship

from sqlalchemy import event

from extensions import db

# Alias common SQLAlchemy names
Column = db.Column
relationship = relationship


class CRUDMixin(object):
    """Mixin that adds convenience methods for CRUD (create, read, update, delete) operations."""

    @classmethod
    def create(cls, **kwargs):
        """Create a new record and save it the databasegfd."""
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        """Update specific fields of a record."""
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        """Save the record."""
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        """Remove the record from the databasegfd."""
        db.session.delete(self)
        return commit and db.session.commit()


class TimeMixin(object):
    """
    Mixin that adds convenient methods to automatically handle when an object was created and last updated.
    """

    __table_args__ = {"extend_existing": True}

    # created_at = db.Column("created_at", db.DateTime, nullable=False)
    # updated_at = db.Column('updated_at', db.DateTime, nullable=False)

    @staticmethod
    def create_time(mapper, connection, instance):
        now = datetime.datetime.utcnow()
        instance.created_at = now
        instance.updated_at = now

    @staticmethod
    def update_time(mapper, connection, instance):
        now = datetime.datetime.utcnow()
        instance.updated_at = now

    @classmethod
    def register(cls):
        pass
        # event.listen(cls, 'before_insert', cls.create_time)
        # event.listen(cls, 'before_update', cls.update_time)


class SqlModel(CRUDMixin, TimeMixin, db.Model):
    """Base model class that includes CRUD convenience methods."""

    __abstract__ = True

    def __init__(self, **kwargs):
        db.Model.__init__(
            self,
            **kwargs
        )

        self.register()

    @classmethod
    def get_or_create(cls, **kwargs):
        instance = cls.query.filter_by(**kwargs).first()
        if instance:
            return instance
        else:
            instance = cls(**kwargs)
            db.session.add(instance)
            db.session.commit()
            return instance


# From Mike Bayer's "Building the app" talk
# https://speakerdeck.com/zzzeek/building-the-app
class SurrogatePK(object):
    """A mixin that adds a surrogate integer 'primary key' column named ``id`` to any declarative-mapped class."""

    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls, record_id):
        """Get record by ID."""
        if any(
                (isinstance(record_id, (str, bytes)) and record_id.isdigit(),
                 isinstance(record_id, (int, float))),
        ):
            return cls.query.filter_by(id=int(record_id)).first()
        return None


def reference_col(tablename: str, nullable: bool = False, pk_name: str = 'id', **kwargs):
    """Column that adds primary key foreign key reference.

    Usage: ::
        category_id = reference_col('category')
        category = relationship('Category', backref='categories')
    """
    return db.Column(
        db.ForeignKey('{0}.{1}'.format(tablename, pk_name)),
        nullable=nullable, **kwargs)


def get_or_create(model, **kwargs):
    instance = db.session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        db.session.add(instance)
        db.session.commit()
        return instance
