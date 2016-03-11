import re
import random
import sys
import requests
import math

tempMapping = {}
mapping = {}
sen_starters = []

def fixCaps(word):
    if word.isupper() and word != "I":
        word = word.lower()
    elif word [0].isupper():
        word = word.lower().capitalize()
    else:
        word = word.lower()
    return word

def toHashKey(lst):
    return tuple(lst)

r = requests.get('http://www.kanyerest.xyz/api/lyrics')
w_list = [fixCaps(w) for w in re.findall(r"[\w']+|[.,!?;]", r.content)]

def wordlist(n):
    if n not in range(0, 5):
        n = random.randint(0, 5)
    words = re.findall(r"[\w']+|[.,!?;]", r.content)
    i = int(math.floor((len(words)*(n/(float(6))))))
    j = int(math.floor((len(words)*(float(n+1)/(float(6))))))
    return w_list[i:j]

def addItemToTempMapping(history, word):
    global tempMapping
    while len(history) > 0:
        first = toHashKey(history)
        if first in tempMapping:
            if word in tempMapping[first]:
                tempMapping[first][word] += 1.0
            else:
                tempMapping[first][word] = 1.0
        else:
            tempMapping[first] = {}
            tempMapping[first][word] = 1.0
        history = history[1:]

def buildMapping(words):
    global tempMapping
    sen_starters.append(words[0])
    for i in range(1, len(words) - 1):
        if i <= 2:
            history = words[: i + 1]
        else:
            history = words[i - 2 + 1 : i + 1]
        follow = words[i + 1]
        if history[-1] == "." and follow not in ".,!?;":
            sen_starters.append(follow)
        addItemToTempMapping(history, follow)
    for first, followset in tempMapping.iteritems():
        total = sum(followset.values())
        mapping[first] = dict([(k, v / total) for k, v in followset.iteritems()])


def next(prevList):
    sum = 0.0
    retval = ""
    index = random.random()
    while toHashKey(prevList) not in mapping:
        prevList.pop(0)
    for k, v in mapping[toHashKey(prevList)].iteritems():
        sum += v
        if sum >= index and retval == "":
            retval = k
    return retval

def genSentence():
    buildMapping(wordlist(random.randint(0, 2)))
    curr = random.choice(sen_starters)
    sent = curr.capitalize()
    prevList = [curr]
    while (curr not in '.!?'):
        curr = next(prevList)
        prevList.append(curr)
        if len(prevList) > 2:
            prevList.pop(0)
        if (curr not in ".,!?;"):
            sent += " "
        sent+= re.sub(r'\,', '', curr)
    return sent

# i = 0
# while i < 8:
#     print genSentence()
#     i+=1

