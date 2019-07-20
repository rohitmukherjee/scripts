import argparse

parser = argparse.ArgumentParser(description = "Backup all tables in the database")
parser.add_argument("source_host", metavar="sh", nargs=1, help="The source host of the db dump")
parser.add_argument("db_name", metavar="n", nargs=1, help="The name of the database")
parser.add_argument("db_user_name", metavar="n", nargs=1, help="The user name of the database")
parser.add_argument("db_password", metavar="p", nargs=1, help="The password of the database")
parser.add_argument("db_excluded_tables", metavar="x", nargs='+', help="The database tables to exclude while taking a dump")
parser.add_argument("destination_host", metavar="dh", nargs=1, help="The destination host of the db dump")
parser.add_argument("destination_directory", metavar="dd", nargs=1, help="The destination directory of the db dump")
parser.add_argument("destination_file_name", metavar="de", nargs=1, help="The file name of the db dump")

args = parser.parse_args()
