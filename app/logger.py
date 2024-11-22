import logging


app_logger = logging.getLogger('app_logger')
app_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('myapp.log')
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

app_logger.addHandler(file_handler)