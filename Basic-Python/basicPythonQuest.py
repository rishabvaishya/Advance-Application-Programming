# Basic Python Quest
# When returning lists of values, order is not important unless specified

__STUDENT_ID__ = "47505527"
__CODING_NAME__ = "Mindfreak"


def isSorted(list):
    i = 1
    while i < len(list):
        # when RHS value < LHS value
        if list[i] < list[i - 1]:
            return False
        i += 1
    return True


def isSortedAndUnique(list):
    #reusing the already defined functions
    if isSorted(list) and hasUniqueValues(list):
        return True

    return False


def hasUniqueValues(list):
    i = 1
    while i < len(list):
        for j in range(i):
            # returns false when duplicate found
            if list[j] == list[i]:
                return False
        i += 1
    return True


def genSortedArrayUniqueValues(list):
    # creating new result list, which will have sorted & unique values
    newList = []
    if not list:
        return list
    # appending 1st element from input list
    newList.append(list[0])
    i = 1
    for i in range(len(list)):
        # taking 1 element at a time from input list to compare it with each values of result list
        compareItem = list[i]
        isDuplicate = False
        for j in range(len(newList)):
            # if element is duplicate, move on to the next element from input list
            if compareItem == newList[j] :
                isDuplicate = True
                break
            # if element in new result list > comparing element from input list then swap,
            # so that at the end the largest value is appended at the end, resulting in ascending sort
            elif compareItem < newList[j] :
                temp = newList[j]
                newList[j] = compareItem
                compareItem = temp

        if not isDuplicate :
            newList.append(compareItem)
    return newList


def listToMapTwoByTwo(list):
    map = {}

    if not list:
        return map

    i = 0
    while i < (len(list)-1):
        map[list[i]] = list[i+1]
        # iterating loop by 2
        i+=2
    return map


def wordsInStringToDictWordCount(s):
    dict = {}
    words = s.split()
    for word in words :
        # if word already exists
        if word in dict :
            dict[word] = dict[word]+1
        else :
            dict[word] = 1

    return dict


def reverseWordsInString(string):
    s = ""
    words = string.split()
    for word in reversed(words):
        s+= str(word)
        s+= ' '
        # strip removes the last space from the string
    return s.strip()


def genListOfOverlaps(list1, list2,):
    finalList = []
    for myItem in list1 :
        # if element from list 1 is present in list 2
        if myItem in list2 :
            finalList.append(myItem)
    return finalList


def removeDupsNoSet(list):
    finalList = []
    for item in list :
        # if element from input list not in final resulting list
        if item not in finalList :
            finalList.append(item)
    return finalList


def removeDupsUseSet(mylist):
    # list converted to set converted to list & returned
    return list(set(mylist))


if __name__ == '__main__':
  print ('Hello Mindfreak!')


