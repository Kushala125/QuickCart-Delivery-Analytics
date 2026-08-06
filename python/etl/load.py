from sqlalchemy import create_engine
import pandas as pd
from logger import logger


def load_to_rds(df):

    username = "admin"
    password = "Kushala125"
    host = "65.2.117.90"
    port = 3306
    database = "quickcart"

    try:
        logger.info(f"Connecting to MySQL RDS ({host})")

        engine = create_engine(
            f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
        )

        df.to_sql(
            name="delivery_data",
            con=engine,
            if_exists="replace",
            index=False
        )

        logger.info(f"Successfully loaded {len(df)} rows into delivery_data")

        print("✅ Data loaded successfully!")

    except Exception:
        logger.exception("Failed while loading data into RDS")
        raise


if __name__ == "__main__":

    df = pd.read_csv("data/raw/delivery_data.csv")

    load_to_rds(df)