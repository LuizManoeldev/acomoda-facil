import logging  # Import the logging module

# Configure logging settings
logging.basicConfig(filename='app.log',  # Specify the log file name
                    filemode='a',         # Set the file mode to append ('a')
                    format='%(asctime)s - %(levelname)s - %(message)s',  # Specify the log message format
                    level=logging.INFO)   # Set the logging level to INFO

# Get the logger object for the current module
logger = logging.getLogger(__name__)
