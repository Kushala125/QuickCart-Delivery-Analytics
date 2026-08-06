import pandas as pd
from logger import logger


def transform_data(df):

    try:
        logger.info("Starting data transformation")

        original_rows = len(df)

        df = df.drop_duplicates()

        df = df.dropna(subset=["Order_ID"])

        df.columns = df.columns.str.strip()

        logger.info(
            f"Transformation completed. Rows before: {original_rows}, Rows after: {len(df)}"
        )

        return df

    except Exception:
        logger.exception("Transformation failed")
        raise