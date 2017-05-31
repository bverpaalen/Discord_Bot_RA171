from rest import restCall
wiki='http://divinity.wikia.com/api/v1/'

def QueryUrl(query,hits=1):
    url = SearchUrl(query,hits)
    dic = restCall(url)
    if dic == {}:
        return ["No Result"]
    else:
        urls = []
        items = dic["items"]
        for item in items:
            urls.append(item["url"])
        return urls
    
def SearchUrl(query,hits):
    return wiki + "Search/List/?query="+query+"&limit="+str(hits)    
