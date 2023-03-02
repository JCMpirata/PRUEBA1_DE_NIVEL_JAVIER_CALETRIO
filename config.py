import sys


DATABASE_PATH = "vehiculo.csv"


if "pytest" in sys.argv[0]:
    DATABASE_PATH = "test/vehiculo_test.csv"