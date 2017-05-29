from rest import restCall
wiki='http://divinity.wikia.com/api/v1/'



def getItemUrl(query,hits=1):
    url = getUrl(query,hits)
    dic = restCall(url)
    if dic == {}:
        return "No Result"
    else:
        return dic

    
def getUrl(query,hits):
    return wiki + "Search/List/?query="+query+"&limit="+str(hits)
    
