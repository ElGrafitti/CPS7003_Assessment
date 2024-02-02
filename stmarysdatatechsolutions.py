import os

# Get the absolute path to the project's root directory
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Set the database path using the PROJECT_ROOT variable
DATABASE_NAME = os.path.join(PROJECT_ROOT, 'database', 'stmarysdatatechsolutions.db')
