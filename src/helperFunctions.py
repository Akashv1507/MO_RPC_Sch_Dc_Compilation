from calendar import monthrange

def generateFileNameSuffix(startFinYr:int, endFinYr:int):

    monthList = [{'name':'Jan', 'val':1}, {'name':'Feb', 'val':2}, {'name':'Mar', 'val':3}, {'name':'Apr', 'val':4},
    {'name':'May', 'val':5}, {'name':'Jun', 'val':6}, {'name':'Jul', 'val':7}, {'name':'Aug', 'val':8}, 
    {'name':'Sep', 'val':9}, {'name':'Oct', 'val':10},{'name':'Nov', 'val':11},{'name':'Dec', 'val':12}]
    # monthList = [{'name':'Mar', 'val':3}]
    fileNameSuffixList = []

    for month in monthList:
        if month['val']<=3:
            noDays = monthrange(endFinYr, month['val'])[1]
            monthFileSuffix = month['name']+ '01' + str(endFinYr)[2:] + month['name'] + str(noDays) + str(endFinYr)[2:] + '.DBF'
            fileNameSuffixList.append(monthFileSuffix)
        else:
            noDays = monthrange(startFinYr, month['val'])[1]
            monthFileSuffix = month['name']+ '01' + str(startFinYr)[2:] + month['name'] + str(noDays) + str(startFinYr)[2:] + '.DBF'
            fileNameSuffixList.append(monthFileSuffix)

    return fileNameSuffixList