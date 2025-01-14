from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text


class Post(Base) :
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key = True, nullable = False,)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    published = Column(Boolean, server_default = "TRUE", nullable = False)
    time_created = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text("now()"))
    
    user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)
    
    owner = relationship("Users")
    
    
    
class Users(Base) :
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True, nullable = False,)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    time_created = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text("now()"))
    
    
    
class Coins(Base) :
    __tablename__ = "coins"
    
    id = Column(Integer,primary_key = True, nullable = False)
    coin_amount = Column(Integer, nullable = False)
    time_created = Column(TIMESTAMP(timezone = True), nullable = False, server_default = text("now()"))
    
    
class Votes(Base) :
    __tablename__ = "votes"
    
    user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), primary_key = True)
    post_id = Column(Integer, ForeignKey("posts.id", ondelete = "CASCADE"), primary_key = True)
    
    
    