import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--text", help="Interact with Lisa by typing", action='store_true')
    parser.add_argument("-s", "--silent", help="Lisa doesn't speak; she writes instead.", action='store_true')
    return parser.parse_args()