import os
import traceback
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from api.database import Post, DB


def list_posts_resolver(obj, info):
    # print(f'LIST POSTS RESOLVER: {obj}')
    # print(f'INFO: {info}')

    engine = create_engine(
        os.getenv('DB_URI'),
        echo=True
    )

    with Session(engine) as session:
        try:
            posts = session.query(Post).order_by(Post.created_at.desc())
            posts_dict = [post.to_dict() for post in posts]
            
            return {
                "success": True,
                "posts": posts_dict
            }
        except Exception as e:
            errors =  traceback.format_exc().splitlines()
            return {
                "success": False,
                "errors": errors
            }


def get_post_resolver(obj, info, id):
    # print(f'INSIDE GET POST: {id}')
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