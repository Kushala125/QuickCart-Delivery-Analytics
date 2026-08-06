from extract import extract_data
from transform import transform_data
from load import load_to_rds
from logger import logger
import time


def run_pipeline():

    start = time.time()

    logger.info("========== ETL Pipeline Started ==========")

    try:

        df = extract_data()

        df = transform_data(df)

        load_to_rds(df)

        logger.info("ETL Pipeline completed successfully")

    except Exception:
        logger.exception("ETL Pipeline failed")
        raise

    finally:

        end = time.time()

        logger.info(f"Pipeline execution time: {round(end-start,2)} seconds")

        logger.info("========== ETL Pipeline Finished ==========")


if __name__ == "__main__":
    run_pipeline()