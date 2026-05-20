from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError
from routes.routes import router as category_router
from core.db import engine
from models import model




class Application:

    def __init__(self):

        # Create database tables
        try:
            model.Base.metadata.create_all(bind=engine)
            print("Database connected successfully.")

            origins = [
                "http://localhost:5173",
                "http://127.0.0.1:5173",
            ]



        except SQLAlchemyError as error:
            print(f"Database connection failed: {error}")

        # Initialize FastAPI app
        self.app = FastAPI(
            title="Professional FastAPI App",
            version="1.0.0"
        )

        # Register routes
        self.app.include_router(category_router)


# App instance
application = Application()
app = application.app