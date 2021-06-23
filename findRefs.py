f = open("teksti.txt", "r", encoding="utf-8")

isStart=True
startOfRef=""

refs=[]

idx = 0
linesToGo=True
while linesToGo:
    idx += 1
    nextLine=f.readline()
    if nextLine.find("LÄHTEITÄ") != -1:
        linesToGo=False

    remainingLine = nextLine

    lineCond = True
    while lineCond:
        openClosurePos = remainingLine.find("(")
        closeClosurePos = remainingLine.find(")")

        if openClosurePos != -1 and closeClosurePos != -1:
            if startOfRef != "":
                print(str(idx) + "error1 with closures")
            refs.append(str(idx) + ": " + remainingLine[openClosurePos : closeClosurePos + 1])
            if len(remainingLine) > closeClosurePos + 2:
                remainingLine=remainingLine[closeClosurePos + 1 :]
            else:
                lineCond = False
        elif openClosurePos != -1:
            if startOfRef != "":
                print(str(idx) + "error2 with closures")
            startOfRef=remainingLine[openClosurePos :]
            lineCond = False
        elif closeClosurePos != -1:
            if startOfRef == "":
                print(str(idx) + "error3 with closures")
            refs.append(str(idx) + ": " + startOfRef + remainingLine[: closeClosurePos + 1])
            lineCond = False
        else:
            lineCond = False

f.close()

output = open("refs.txt", "w")
for ref in refs:
    output.write(ref + "\n")

output.close()