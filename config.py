import sys

# Path to the directory containing the data files

DATABASE_PATH = "vehiculos.csv"

if "pytest" in sys.argv[0]:
    DATABASE_PATH = "tests/vehiculos_test.csv"