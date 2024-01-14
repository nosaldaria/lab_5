from sqlalchemy import create_engine, Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    status = Column(String(50))
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', nullable=False)
    updated_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', server_onupdate='CURRENT_TIMESTAMP', nullable=False)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    article_id = Column(Integer, ForeignKey('articles.id'))
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', nullable=False)

    user = relationship('User', back_populates='comments')
    article = relationship('Article', back_populates='comments')

engine = create_engine('mysql://root:dnsn240409d@localhost:3306/new_project')

Base.metadata.create_all(engine)
