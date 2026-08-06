import boto3
import pandas as pd
from logger import logger


def extract_data():
    bucket = "quickcart-food-delivery-kush1250"
    key = "del.csv"

    try:
        logger.info("Starting data extraction from S3")

        s3 = boto3.client("s3")

        response = s3.get_object(
            Bucket=bucket,
            Key=key
        )

        df = pd.read_csv(response["Body"])

        logger.info(f"Successfully extracted {len(df)} rows from S3")

        return df

    except Exception:
        logger.exception("Failed during data extraction")
        raise


if __name__ == "__main__":
    extract_data()