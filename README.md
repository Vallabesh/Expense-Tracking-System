The Expense Tracking System is a full-stack application that enables users to record, update, and analyze their daily expenses through an interactive interface. The backend is built using FastAPI, exposing RESTful APIs for data operations and analytics, while MySQL serves as the database for structured storage. The frontend is developed with Streamlit, providing a simple yet powerful UI for data entry and visualization.

The application supports:

Adding and updating expenses by date
Category-wise expense analysis with percentage breakdown
Monthly expense trend visualization
Real-time synchronization between frontend and backend

The project follows a modular architecture:

Database Layer: Handles SQL queries and connection management
API Layer: Implements business logic and endpoints using FastAPI
Frontend Layer: Provides interactive UI and visualizations using Streamlit

This project highlights key concepts such as REST API design, data validation with Pydantic, stateful UI handling in Streamlit, and end-to-end data flow from user input to database and back.
