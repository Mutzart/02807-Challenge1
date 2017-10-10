import xml.etree.cElementTree as ET
import time

############### Methods used in challenge ###############

# Method to remove any non-ASCII chars from the string, and convert it to lower case
def removeFormatting(s):
    return ("".join(i for i in s if ord(i)<126 and ord(i)>31)).lower()

# method to sort input into appropriate parts
def query(text , input , init_idx=0):
    inputs = input.split('"')  # separates intervals from string bits
    inputs = filter(None, inputs)  # Removes the empty string lists at start and end
    n = len(inputs)
    matches = 0
    start = text.find(inputs[0], init_idx)
    while start > 0:
        case = 1  # variable to keep track of interval comparison
        for i in range(0, n-2, 2):
            # find the two occurances
            current = text.find(inputs[i], start)
            next = text.find(inputs[i+2], start)

            # Interval
            [first, second] = inputs[i+1][1:-1].split(',')

            # Check if interval is valid
            dist = (next - current)
            case = case*int( dist > int(first) and dist < int(second))

        if case:
            matches += 1

        start = text.find(inputs[0], (start + 1))
    return matches



    #print inputs
    #return inputs

############### Search through database ###############
wikiFile = 'Data\\enwiki-20170820-pages-articles.xml'
#wikiFile = 'Data\\HenryDuncan.xml'

print 'Beginning'
time_start = time.time()

# get an iterable
wiki = ET.iterparse(wikiFile, events=("start", "end"))

# turn it into an iterator
wiki = iter(wiki)

# get the root element
event, root = wiki.next()
num_articles = 0
time_mid = time.time()
print 'initialization complete'
count = 0
for event, article in wiki:

    if event == 'end' and article.tag == 'text':
        textstring = removeFormatting(article.text)
        print textstring


time_end = time.time()

print 'Time used: ' +str(time_end - time_start) + ' with loading done after ' + str(time_mid - time_start)
