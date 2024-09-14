#!/bin/bash

# Run the first command (your initialization script)
echo "Running /app/index_data.py... Indexing knowledge base into elasticsearch"
python ./app/index_data.py

# Check if the script ran successfully
if [ $? -ne 0 ]; then
    echo "index_data.py failed."
    exit 1
fi

# Run the second command (start the Streamlit app)
echo "Starting Streamlit app AZ900 Study Buddy"
streamlit run ./app/app.py --server.port=8501 --server.address=0.0.0.0
