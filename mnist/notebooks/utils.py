import pandas as pd
from plumbum import local

DATA_DIR = local.path(__file__).dirname.up() / 'data'
