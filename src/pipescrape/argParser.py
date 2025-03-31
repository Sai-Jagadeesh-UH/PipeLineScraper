from argparse import ArgumentParser


parser = ArgumentParser(prog="=ScrapeBot",
                        description='downloads file on scecific date',
                        epilog='Only for ethical purposes'
                        )

parser.add_argument("-f", "--fro", type=str,
                    help="files from date mmddyyyy")

parser.add_argument("-t", "--till", type=str,
                    help="files till date mmddyyyy")

parser.add_argument("-o", "--on", type=str,
                    help="on a specific date mmddyyyy")
