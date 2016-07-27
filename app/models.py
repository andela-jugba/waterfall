from app import db


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    books = db.relationship('Book',
                            secondary=classifications,
                            backref=db.backref('categories', lazy='dynamic'),
                            lazy='dynamic')

    def __repr__(self):
        return '<Category %r>' % self.name


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return '<Book %r>' % self.name

classifications = db.table('classifications',
                           db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
                           db.Column('category_id', db.Integer, db.ForeignKey('categories.id'))

)