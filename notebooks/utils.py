import pandas as pd
from plumbum import local

DATA_DIR = local.path(__file__).dirname.up() / 'data'
TRAIN_PATH =  DATA_DIR / 'train.csv'
TEST_PATH = DATA_DIR / 'test.csv'


def load_data():
    df = pd.read_csv(TRAIN_PATH)