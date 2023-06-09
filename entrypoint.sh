# # Run Alembic migrations
# alembic upgrade head

# # Start the app
# exec uvicorn main:app --host 0.0.0.0 --port 8001 --reload

#!/bin/bash

set -e

python tool_manager.py

# Install dependencies
/install_tool_dependencies.sh

# Run Alembic migrations
alembic upgrade head

# Start the app
exec uvicorn main:app --host 0.0.0.0 --port 8001 --reload