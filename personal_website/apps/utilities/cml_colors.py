red='\033[31m'
green='\033[32m'
yellow='\033[93m'
reset='\033[0m'

def pwarning(text):
        print(f'{yellow}{text}{reset}')

def perror(text):
        print(f'{red}{text}{reset}')

def psuccess(text):
        print(f'{green}{text}{reset}')