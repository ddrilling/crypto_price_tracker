import argparse
from price_tracker import getPrice as gp

def main():
    parser = argparse.ArgumentParser(prog = 'Crypto Price Tracker',description = 'Find price of crypto currency', 
                                     epilog = 'If problem occurs, ensure you have entered the correct ids')
    parser.add_argument('ids', metavar = 'I', type = str, nargs = 1, help = 'The ids of the currency you are looking for')
    args = parser.parse_args()
    print(gp(args))