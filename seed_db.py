from datetime import datetime
import os
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import Session
from api.database import Post


if __name__ == '__main__':
    engine = create_engine(
        os.getenv('DB_URI'),
        echo=True
    )

    print(engine)

    with Session(engine) as session:
        for i in range(20):
            print(i)
            current_date = datetime.now()
            new_post = Post(
                title=f"{i} - A new morning", 
                description=f"A new morning details:\n{i}", 
                created_at=current_date
            )

            session.add(new_post)
            session.commit()