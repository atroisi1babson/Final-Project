from newsarticle_generation import newsarticle_creation
from summaries_generation import summaries_creation
import os


def generate_newspaper(): # this has been renamed to prevent conflicts when imported into the code scheduler that Consumer Safety Service uses
    """
    Generates recall newspaper articles based on a CSV database file
    """
    if os.path.exists("demo_summaries.csv"): # used ChatGPT to learn about os library and path.exists
        os.remove("demo_summaries.csv")
    database = "demo_recalls.csv"
    summaries_creation(database)
    database = "demo_summaries.csv"
    newsarticle_creation(database)
    print("The code has completed")


if __name__ == "__main__":
    generate_newspaper()