import argparse


def main():
    parser = argparse.ArgumentParser(description='OSINT Tool to search global information about a specific individual')
    parser.add_argument('-p', '--prompt',
                        help='Initial prompt to search using OSINT (e.g. First name, Last name, City)')

    args = parser.parse_args()


if __name__ == '__main__':
    main()
