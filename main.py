import os

setupPath = "doc_model_setup"
setupFile = setupPath+"/testNum.txt"
modelDocsPath = "model_documentation"
setup = True
customNotes = ""

while setup:
    if not os.path.exists(setupPath):
        os.mkdir(setupPath)
        os.mkdir(modelDocsPath)
    elif not os.path.isfile(setupFile):
        f = open(setupFile, "w")
        f.write("0")
        f.close
        setup = False
    else:
        setup = False

    
def docSetup(customName):
    if customName=="":
        with open(setupFile, 'r+') as file:
            number = file.read().rstrip()
            n = int(number)
            numberInt = n+1
            file.truncate(0)
            file.write(str(numberInt))
            print(number)
            filePathName = "Test "+str(number)
            file.close
    else:
        filePathName = customName
    
    fileHead = "# "+filePathName
    osWritePath = modelDocsPath+"/"+filePathName
    if not os.path.exists(osWritePath):
        os.mkdir(osWritePath)

    return osWritePath+"/", fileHead

def handleLogs(logList):
    logString =""
    for log in logList:
        logString = logString+"\n"+str(log)
    return logString


def docModel(fileHead, parameters, parameterValue, graphPath, text, writePath): #, textToLog,customName):
    
    resultsTable =""
    #check
    if(len(parameterValue)!=len(parameters)):
        print("The size of your hyper parameter name list and actual hyper paramenter integer values list do not match")

    for parameter in parameters:
        resultsTable = resultsTable+parameter
        if(parameter != parameters[len(parameters)-1]):
            resultsTable = resultsTable+"|"
    resultsTable=resultsTable+"\n"

    for i in range(0,len(parameters)):
        resultsTable=resultsTable+" --- "
        if(i!=len(parameters)-1):
            resultsTable = resultsTable+"|"
    
    resultsTable=resultsTable+"\n"
    
    i = 0
    for value in parameterValue:

        resultsTable = resultsTable+str(value)
        if(i != len(parameterValue)-1):
            resultsTable = resultsTable+"|"
        i=i+1
    
    resultsTable = resultsTable+"\n"
    imageMarkdown = ""

    for graph in graphPath:
        imageMarkdown = imageMarkdown+"\n![ML Graph]("+graph+")"

    markDowntext = fileHead+"\n"+resultsTable+"\n"+imageMarkdown+text

    f = open(writePath+"model_document.md", "w")

    f.write(markDowntext)

    f.close


    print(markDowntext)


    
