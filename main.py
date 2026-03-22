from src.read_data import read_data

from src.clean_data import clean_data

from src.validate_data import validate

from src.report_generator import generate_report,data_profile

from src.logger import setup_logger

from config.config import *

import os


os.makedirs("output",exist_ok=True)

os.makedirs("logs",exist_ok=True)


logger=setup_logger(LOG_FILE)


df=read_data(INPUT_FILE)

if df is None:

    logger.error("File read failed")

    exit()


errors=validate(df)

if errors:

    logger.error(errors)


df=clean_data(df)

df.to_csv(CLEAN_FILE,index=False)


report=generate_report(df)

with open(REPORT_FILE,"w") as f:

    f.write(report)


profile=data_profile(df)

with open(PROFILE_FILE,"w") as f:

    f.write(profile)


logger.info("Pipeline completed successfully")

print("ETL Pipeline completed")
