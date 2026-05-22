from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

        except SQLAlchemyError as error:
            print(f"Database connection failed: {error}")

        # Initialize FastAPI app
        self.app = FastAPI(
            title="Professional FastAPI App",
            version="1.0.0"
        )

        # ⭐ ADD CORS HERE (VERY IMPORTANT)
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=[
                "http://localhost:5174",
                "http://localhost:5173"
            ],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Register routes
        self.app.include_router(category_router)


# App instance
application = Application()
app = application.app