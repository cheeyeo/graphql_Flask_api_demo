import os
import traceback
from datetime import datetime
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from api.database import Post, DB


def create_post_resolver(object, info, input: dict):
    engine = create_engine(
        os.getenv('DB_URI'),
        echo=True
    )

    with Session(engine) as session:
        try:
            post = Post(
                title=input['title'],
                description=input['description'],
                created_at=datetime.now(),
            )
            session.add(post)
            session.commit()
        
            return {
                "success": True,
                "post": post.to_dict()
            }
        except Exception as e:
            errors =  traceback.format_exc().splitlines()
            return {
                "success": False,
                "errors": errors
            }
    

def update_post_resolver(object, info, id, input: dict):
    engine = create_engine(
        os.getenv('DB_URI'),
        echo=True
    )

    with Session(engine) as session:
        try:
            stmt = (
                select(Post)
                .where(Post.id == id)
            )

            ret_post = session.scalars(stmt).one()

            ret_post.title = input['title']
            ret_post.description = input['description']
            session.add(ret_post)
            session.commit()

            return {
                "success": True,
                "post": ret_post.to_dict()
            }
        except Exception as e:
            errors =  traceback.format_exc().splitlines()
            return {
                "success": False,
                "errors": errors
            }


def delete_post_resolver(object, info, id):
    engine = create_engine(
        os.getenv('DB_URI'),
        echo=True
    )

    with Session(engine) as session:
        try:
            stmt = (
                select(Post)
                .where(Post.id == id)
            )

            ret_post = session.scalars(stmt).one()
            session.delete(ret_post)
            session.commit()

            return {
                "success": True,
                "post": ret_post.to_dict()
            }
        except Exception as e:
            errors =  traceback.format_exc().splitlines()
            return {
                "success": False,
                "errors": errors
            }