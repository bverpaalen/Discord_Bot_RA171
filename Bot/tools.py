def stringInList(string,listvar):
    string = str(string)
    hit = False
    print(string)
    for item in listvar:
        print(item)
        if item == string:
            hit = True
    return hit
