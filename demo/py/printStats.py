import json

def printNumOfCams(cams):
    print(f'Number of cams: {len(cams)}')

if __name__ == '__main__':
    cams = json.load(open('../../data/data.json'))
    printNumOfCams(cams)
