import sys

#This little snippet here grabs the text file argument from the command line.
with open(sys.argv[1]) as f:
    lines = f.readlines()
f.close()
i = 0
#These next 6 for loops isolate the lines from the text file.
for line in lines:
    if i == 0:
        aLine = line
    if i == 1:
        bLine = line
    if i == 2:
        cLine = line   
    if i == 3:
        dLine = line
    if i == 4:
        eLine = line
    i += 1
i = 0
#Then they isolate the numbers into individual placeholders.
for num in aLine.split():
    if i == 0:
        a1 = int(num)
    if i == 1:
        a2 = int(num)
    if i == 2:
        a3 = int(num)
    if i == 3:
        a4 = int(num)
    if i == 4:
        a5 = int(num)
    i += 1
i = 0
for num in bLine.split():
    if i == 0:
        b1 = int(num)
    if i == 1:
        b2 = int(num)
    if i == 2:
        b3 = int(num) 
    if i == 3:
        b4 = int(num)
    if i == 4:
        b5 = int(num)
    i += 1
i = 0
for num in cLine.split():
    if i == 0:
        c1 = int(num)
    if i == 1:
        c2 = int(num)
    if i == 2:
        c3 = int(num) 
    if i == 3:
        c4 = int(num)
    if i == 4:
        c5 = int(num)
    i += 1
i = 0
for num in dLine.split():
    if i == 0:
        d1 = int(num)
    if i == 1:
        d2 = int(num)
    if i == 2:
        d3 = int(num) 
    if i == 3:
        d4 = int(num)
    if i == 4:
        d5 = int(num)
    i += 1
i = 0
for num in eLine.split():
    if i == 0:
        e1 = int(num)
    if i == 1:
        e2 = int(num)
    if i == 2:
        e3 = int(num) 
    if i == 3:
        e4 = int(num)
    if i == 4:
        e5 = int(num)
    i += 1
#Many, many things needed to be initialized.
stop = 0
currLine = 0
position = 0
#These are used to check for changes.
changeOccurA = 0
changeOccurB = 0
changeOccurC = 0
changeOccurD = 0
changeOccurE = 0
#These are used to show the previous matrix.
oldA1 = a1
oldA2 = a2
oldA3 = a3
oldA4 = a4
oldA5 = a5
oldB1 = b1
oldB2 = b2
oldB3 = b3
oldB4 = b4
oldB5 = b5
oldC1 = c1
oldC2 = c2
oldC3 = c3
oldC4 = c4
oldC5 = c5
oldD1 = d1
oldD2 = d2
oldD3 = d3
oldD4 = d4
oldD5 = d5
oldE1 = e1
oldE2 = e2
oldE3 = e3
oldE4 = e4
oldE5 = e5
roundNum = 1
updated = 1
#Then I opened a file and began my huge loop. It's mostly identical for the separate stages. So I'll comment round A only.
f = open("OUTPUT.txt", "a")
f.write("-------\n")
while stop < 5:
    if currLine == 0:
        #When I begin any round I set the change checks back to zero.
        changeOccurA = 0
        changeOccurB = 0
        changeOccurC = 0
        changeOccurD = 0
        changeOccurE = 0
        #Then I print the round number, and the current and previous matrices.
        f.write("Round %d: A\n" % (roundNum))
        f.write("Current DV matrix = \n")
        f.write("%d %d %d %d %d\n" % (a1, a2, a3, a4, a5))
        f.write("%d %d %d %d %d\n" % (b1, b2, b3, b4, b5))
        f.write("%d %d %d %d %d\n" % (c1, c2, c3, c4, c5))
        f.write("%d %d %d %d %d\n" % (d1, d2, d3, d4, d5))
        f.write("%d %d %d %d %d\n" % (e1, e2, e3, e4, e5))
        f.write("Last DV matrix = \n")
        f.write("%d %d %d %d %d\n" % (oldA1, oldA2, oldA3, oldA4, oldA5))
        f.write("%d %d %d %d %d\n" % (oldB1, oldB2, oldB3, oldB4, oldB5))
        f.write("%d %d %d %d %d\n" % (oldC1, oldC2, oldC3, oldC4, oldC5))
        f.write("%d %d %d %d %d\n" % (oldD1, oldD2, oldD3, oldD4, oldD5))
        f.write("%d %d %d %d %d\n" % (oldE1, oldE2, oldE3, oldE4, oldE5))
        oldA1 = a1
        oldA2 = a2
        oldA3 = a3
        oldA4 = a4
        oldA5 = a5
        oldB1 = b1
        oldB2 = b2
        oldB3 = b3
        oldB4 = b4
        oldB5 = b5
        oldC1 = c1
        oldC2 = c2
        oldC3 = c3
        oldC4 = c4
        oldC5 = c5
        oldD1 = d1
        oldD2 = d2
        oldD3 = d3
        oldD4 = d4
        oldD5 = d5
        oldE1 = e1
        oldE2 = e2
        oldE3 = e3
        oldE4 = e4
        oldE4 = e5
        #I also check if the matrix was updated using a flag I set up later.
        if(updated == 0):
            f.write("Updated from last DV matrix or the same? Updated\n")
        else:
            f.write("Updated from last DV matrix or the same? Not updated\n")
        f.write("\n")
        while position < 4:
            #Here is where I begin checking each other row with node A.
            if position == 0:
                #Essentially each row checks if there's a shorter path (or any path at all) to the current node.
                #And if so they update their number for that node.
                f.write("Sending DV to node B\nNode B received DV from A\n")
                if((b1 > b3) or b1 == 0) and (b3 != 0):
                    if(c1 != 0) and (((c1 + b3) < b1) or b1 == 0):
                        b1 = c1 + b3
                        changeOccurB += 1
                if((b1 > b4) or b1 == 0) and (b4 != 0):
                    if(d1 != 0) and (((d1 + b4) < b1) or b1 == 0):
                        b1 = d1 + b4
                        changeOccurB += 1
                if((b1 > b5) or b1 == 0) and (b5 != 0):
                    if(e1 != 0) and (((e1 + b5) < b1) or b1 == 0):
                        b1 = e1 + b5
                        changeOccurB += 1
            #When a change in numbers occurs I make sure it writes the correct statement using the change checks.
            if changeOccurB > 0:
                f.write("Updating DV matrix at node B\nNew DV matrix at node B = %d %d %d %d %d\n\n" % (b1, b2, b3, b4, b5))
            else:
                f.write("No change in DV at node B\n\n")
            position += 1
            if position == 1:
                #What happens to each of the rows is practically identical in process. So I believe it's okay to skip ahead.
                f.write("Sending DV to node C\nNode C received DV from A\n")
                if((c1 > c2) or c1 == 0) and (c2 != 0):
                    if(b1 != 0) and (((b1 + c2) < c1) or c1 == 0):
                        c1 = b1 + c2
                        changeOccurC += 1
                if((c1 > c4) or c1 == 0) and (c4 != 0):
                    if(d1 != 0) and (((d1 + c4) < c1) or c1 == 0):
                        c1 = d1 + c4
                        changeOccurC += 1
                if((c1 > c5) or c1 == 0) and (c5 != 0):
                    if(e1 != 0) and (((e1 + c5) < c1) or c1 == 0):
                        c1 = e1 + c5
                        changeOccurC += 1
            if changeOccurC > 0:
                f.write("Updating DV matrix at node C\nNew DV matrix at node C = %d %d %d %d %d\n\n" % (c1, c2, c3, c4, c5))
            else:
                f.write("No change in DV at node C\n\n")
            position += 1
            if position == 2:
                f.write("Sending DV to node D\nNode D received DV from A\n")
                if((d1 > d2) or d1 == 0) and (d2 != 0):
                    if(b1 != 0) and (((b1 + d2) < d1) or d1 == 0):
                        d1 = b1 + d2
                        changeOccurD += 1
                if((d1 > d3) or d1 == 0) and (d3 != 0):
                    if(c1 != 0) and (((c1 + d3) < d1) or d1 == 0):
                        d1 = c1 + d3
                        changeOccurD += 1
                if((d1 > d5) or d1 == 0) and (d5 != 0):
                    if(e1 != 0) and (((e1 + d5) < d1) or d1 == 0):
                        d1 = e1 + d5
                        changeOccurD += 1
            if changeOccurD > 0:
                f.write("Updating DV matrix at node D\nNew DV matrix at node D = %d %d %d %d %d\n\n" % (d1, d2, d3, d4, d5))
            else:
                f.write("No change in DV at node D\n\n")
            position += 1
            if position == 3:
                f.write("Sending DV to node E\nNode E received DV from A\n")
                if((e1 > e2) or e1 == 0) and (e2 != 0):
                    if(b1 != 0) and (((b1 + e2) < e1) or e1 == 0):
                        e1 = b1 + e2
                        changeOccurE += 1
                if((e1 > e3) or e1 == 0) and (e3 != 0):
                    if(c1 != 0) and (((c1 + e3) < e1) or e1 == 0):
                        e1 = c1 + e3
                        changeOccurE += 1
                if((e1 > e4) or e1 == 0) and (e4 != 0):
                    if(d1 != 0) and (((d1 + e4) < e1) or e1 == 0):
                        e1 = d1 + e4
                        changeOccurE += 1
            if changeOccurE > 0:
                f.write("Updating DV matrix at node E\nNew DV matrix at node E = %d %d %d %d %d\n" % (e1, e2, e3, e4, e5))
            else:
                f.write("No change in DV at node E\n")
            position += 1
            f.write("-------\n")
        #Here a check for the whole node occurs wherein if no changes happened at all I increase the stop counter.
        if(changeOccurA == 0) and (changeOccurB == 0) and (changeOccurC == 0) and (changeOccurD == 0) and (changeOccurE == 0):
            #I also change it so that it flags it for not having updated.
            stop += 1
            updated = 1
        else:
            #If there was a change the stop counter resets.
            stop = 0
            updated = 0
        #Once 5 stop increments have happened the loop is broken.
        if(stop == 5):
            break
        position = 0    
        currLine += 1
        roundNum += 1
        #I also segmented Node sections for a little more clarity.
#---------------------------------------A Round Finishes----------------------------------------------------------------------------------#       
    if currLine == 1:
        changeOccurA = 0
        changeOccurB = 0
        changeOccurC = 0
        changeOccurD = 0
        changeOccurE = 0
        f.write("Round %d: B\n" % (roundNum))
        f.write("Current DV matrix = \n")
        f.write("%d %d %d %d %d\n" % (a1, a2, a3, a4, a5))
        f.write("%d %d %d %d %d\n" % (b1, b2, b3, b4, b5))
        f.write("%d %d %d %d %d\n" % (c1, c2, c3, c4, c5))
        f.write("%d %d %d %d %d\n" % (d1, d2, d3, d4, d5))
        f.write("%d %d %d %d %d\n" % (e1, e2, e3, e4, e5))
        f.write("Last DV matrix = \n")
        f.write("%d %d %d %d %d\n" % (oldA1, oldA2, oldA3, oldA4, oldA5))
        f.write("%d %d %d %d %d\n" % (oldB1, oldB2, oldB3, oldB4, oldB5))
        f.write("%d %d %d %d %d\n" % (oldC1, oldC2, oldC3, oldC4, oldC5))
        f.write("%d %d %d %d %d\n" % (oldD1, oldD2, oldD3, oldD4, oldD5))
        f.write("%d %d %d %d %d\n" % (oldE1, oldE2, oldE3, oldE4, oldE5))
        oldA1 = a1
        oldA2 = a2
        oldA3 = a3
        oldA4 = a4
        oldA5 = a5
        oldB1 = b1
        oldB2 = b2
        oldB3 = b3
        oldB4 = b4
        oldB5 = b5
        oldC1 = c1
        oldC2 = c2
        oldC3 = c3
        oldC4 = c4
        oldC5 = c5
        oldD1 = d1
        oldD2 = d2
        oldD3 = d3
        oldD4 = d4
        oldD5 = d5
        oldE1 = e1
        oldE2 = e2
        oldE3 = e3
        oldE4 = e4
        oldE4 = e5
        if(updated == 0):
            f.write("Updated from last DV matrix or the same? Updated\n")
        else:
            f.write("Updated from last DV matrix or the same? Not updated\n")
        f.write("\n")
        while position < 4:
            if position == 0:
                f.write("Sending DV to node A\nNode A received DV from B\n")
                if((a2 > a3) or a2 == 0) and (a3 != 0):
                    if(c2 != 0) and (((c2 + a3) < a2) or a2 == 0):
                        a2 = c2 + a3
                        changeOccurA += 1
                if((a2 > a4) or a2 == 0) and (a4 != 0):
                    if(d2 != 0) and (((d2 + a4) < a2) or a2 == 0):
                        a2 = d2 + a4
                        changeOccurA += 1 
                if((a2 > a5) or a2 == 0) and (a5 != 0):
                    if(e2 != 0) and (((e2 + a5) < a2) or a2 == 0):
                        a2 = e2 + a5
                        changeOccurA += 1 
            if changeOccurA > 0:
                f.write("Updating DV matrix at node A\nNew DV matrix at node A = %d %d %d %d %d\n\n" % (a1, a2, a3, a4, a5))
            else:
                f.write("No change in DV at node A\n\n")
            position += 1
            if position == 1:
                f.write("Sending DV to node C\nNode C received DV from B\n")
                if((c2 > c1) or c2 == 0) and (c1 != 0):
                    if(a2 != 0) and (((a2 + c1) < c2) or c2 == 0):
                        c2 = a2 + c1
                        changeOccurC += 1    
                if((c2 > c4) or c2 == 0) and (c4 != 0):
                    if(d2 != 0) and (((d2 + c4) < c2) or c2 == 0):
                        c2 = d2 + c4
                        changeOccurC += 1
                if((c2 > c5) or c2 == 0) and (c1 != 0):
                    if(e2 != 0) and (((e2 + c5) < c2) or c2 == 0):
                        c2 = e2 + c5
                        changeOccurC += 1 
            if changeOccurC > 0:
                f.write("Updating DV matrix at node C\nNew DV matrix at node C = %d %d %d %d %d\n\n" % (c1, c2, c3, c4, c5))
            else:
                f.write("No change in DV at node C\n\n")
            position += 1
            if position == 2:
                f.write("Sending DV to node D\nNode D received DV from B\n")
                if((d2 > d1) or d2 == 0) and (d1 != 0):
                    if(a2 != 0) and (((a2 + d1) < d2) or d2 == 0):
                        d2 = a2 + d1
                        changeOccurD += 1  
                if((d2 > d3) or d2 == 0) and (d3 != 0):
                    if(c2 != 0) and (((c2 + d3) < d2) or d2 == 0):
                        d2 = c2 + d3
                        changeOccurD += 1 
                if((d2 > d5) or d2 == 0) and (d5 != 0):
                    if(e2 != 0) and (((e2 + d5) < d2) or d2 == 0):
                        d2 = e2 + d5
                        changeOccurD += 1  
            if changeOccurD > 0:
                f.write("Updating DV matrix at node D\nNew DV matrix at node D = %d %d %d %d %d\n\n" % (d1, d2, d3, d4, d5))
            else:
                f.write("No change in DV at node D\n\n")
            position += 1
            if position == 3:
                f.write("Sending DV to node E\nNode E received DV from B\n")
                if((e2 > e1) or e2 == 0) and (e1 != 0):
                    if(a2 != 0) and (((a2 + e1) < e2) or e2 == 0):
                        e2 = a2 + e1
                        changeOccurE += 1  
                if((e2 > e3) or e2 == 0) and (e3 != 0):
                    if(c2 != 0) and (((c2 + e3) < e2) or e2 == 0):
                        e2 = c2 + e3
                        changeOccurE += 1  
                if((e2 > e4) or e2 == 0) and (e4 != 0):
                    if(d2 != 0) and (((d2 + e4) < e2) or e2 == 0):
                        e2 = d2 + e4
                        changeOccurE += 1  
            if changeOccurD > 0:
                f.write("Updating DV matrix at node E\nNew DV matrix at node E = %d %d %d %d %d\n" % (e1, e2, e3, e4, e5))
            else:
                f.write("No change in DV at node E\n")
            position += 1
            f.write("-------\n")
        if(changeOccurA == 0) and (changeOccurB == 0) and (changeOccurC == 0) and (changeOccurD == 0) and (changeOccurE == 0):
            stop += 1
            updated = 1
        else:
            stop = 0
            updated = 0
        if(stop == 5):
            break
        position = 0
        currLine += 1
        roundNum += 1
#---------------------------------------B Round Finishes----------------------------------------------------------------------------------#       
    if currLine == 2:
        changeOccurA = 0
        changeOccurB = 0
        changeOccurC = 0
        changeOccurD = 0
        changeOccurE = 0
        f.write("Round %d: C\n" % (roundNum))
        f.write("Current DV matrix = \n")
        f.write("%d %d %d %d %d\n" % (a1, a2, a3, a4, a5))
        f.write("%d %d %d %d %d\n" % (b1, b2, b3, b4, b5))
        f.write("%d %d %d %d %d\n" % (c1, c2, c3, c4, c5))
        f.write("%d %d %d %d %d\n" % (d1, d2, d3, d4, d5))
        f.write("%d %d %d %d %d\n" % (e1, e2, e3, e4, e5))
        f.write("Last DV matrix = \n")
        f.write("%d %d %d %d %d\n" % (oldA1, oldA2, oldA3, oldA4, oldA5))
        f.write("%d %d %d %d %d\n" % (oldB1, oldB2, oldB3, oldB4, oldB5))
        f.write("%d %d %d %d %d\n" % (oldC1, oldC2, oldC3, oldC4, oldC5))
        f.write("%d %d %d %d %d\n" % (oldD1, oldD2, oldD3, oldD4, oldD5))
        f.write("%d %d %d %d %d\n" % (oldE1, oldE2, oldE3, oldE4, oldE5))
        oldA1 = a1
        oldA2 = a2
        oldA3 = a3
        oldA4 = a4
        oldA5 = a5
        oldB1 = b1
        oldB2 = b2
        oldB3 = b3
        oldB4 = b4
        oldB5 = b5
        oldC1 = c1
        oldC2 = c2
        oldC3 = c3
        oldC4 = c4
        oldC5 = c5
        oldD1 = d1
        oldD2 = d2
        oldD3 = d3
        oldD4 = d4
        oldD5 = d5
        oldE1 = e1
        oldE2 = e2
        oldE3 = e3
        oldE4 = e4
        oldE4 = e5
        if(updated == 0):
            f.write("Updated from last DV matrix or the same? Updated\n")
        else:
            f.write("Updated from last DV matrix or the same? Not updated\n")
        f.write("\n")
        while position < 4:
            if position == 0:
                f.write("Sending DV to node A\nNode A received DV from C\n")
                if((a3 > a2) or a3 == 0) and (a2 != 0):
                    if(b3 != 0) and (((b3 + a2) < a3) or a3 == 0):
                        a3 = b3 + a2
                        changeOccurA += 1
                if((a3 > a4) or a3 == 0) and (a4 != 0):
                    if(d3 != 0) and (((d3 + a4) < a3) or a3 == 0):
                        a3 = d3 + a4
                        changeOccurA += 1
                if((a3 > a5) or a3 == 0) and (a5 != 0):
                    if(e3 != 0) and (((e3 + a5) < a3) or a3 == 0):
                        a3 = e3 + a5
                        changeOccurA += 1
            if changeOccurA > 0:
                f.write("Updating DV matrix at node A\nNew DV matrix at node A = %d %d %d %d %d\n\n" % (a1, a2, a3, a4, a5))
            else:
                f.write("No change in DV at node A\n\n")
            position += 1
            if position == 1:
                f.write("Sending DV to node B\nNode B received DV from C\n")
                if((b3 > b1) or b3 == 0) and (b1 != 0):
                    if(a3 != 0) and (((a3 + b1) < b3) or b3 == 0):
                        b3 = a3 + b1
                        changeOccurB += 1
                if((b3 > b4) or b3 == 0) and (b4 != 0):
                    if(d3 != 0) and (((d3 + b4) < b3) or b3 == 0):
                        b3 = d3 + b4
                        changeOccurB += 1
                if((b3 > b5) or b3 == 0) and (b5 != 0):
                    if(e3 != 0) and (((e3 + b5) < b3) or b3 == 0):
                        b3 = e3 + b5
                        changeOccurB += 1
            if changeOccurB > 0:
                f.write("Updating DV matrix at node B\nNew DV matrix at node B = %d %d %d %d %d\n\n" % (b1, b2, b3, b4, b5))
            else:
                f.write("No change in DV at node B\n\n")
            position += 1
            if position == 2:
                f.write("Sending DV to node D\nNode D received DV from C\n")
                if((d3 > d1) or d3 == 0) and (d1 != 0):
                    if(a3 != 0) and (((a3 + d1) < d3) or d3 == 0):
                        d3 = a3 + d1
                        changeOccurD += 1
                if((d3 > d2) or d3 == 0) and (d2 != 0):
                    if(b3 != 0) and (((b3 + d2) < d3) or d3 == 0):
                        d3 = b3 + d2
                        changeOccurD += 1
                if((d3 > d5) or d3 == 0) and (d5 != 0):
                    if(e3 != 0) and (((e3 + d5) < d3) or d3 == 0):
                        d3 = e3 + d5
                        changeOccurD += 1
            if changeOccurD > 0:
                f.write("Updating DV matrix at node D\nNew DV matrix at node D = %d %d %d %d %d\n\n" % (d1, d2, d3, d4, d5))
            else:
                f.write("No change in DV at node D\n\n")
            position += 1
            if position == 3:
                f.write("Sending DV to node E\nNode E received DV from C\n")
                if((e3 > e1) or e3 == 0) and (e1 != 0):
                    if(a3 != 0) and (((a3 + e1) < e3) or e3 == 0):
                        e3 = a3 + e1
                        changeOccurE += 1
                if((e3 > e2) or e3 == 0) and (e2 != 0):
                    if(b3 != 0) and (((b3 + e2) < e3) or e3 == 0):
                        e3 = b3 + e2
                        changeOccurE += 1
                if((e3 > e4) or e3 == 0) and (e4 != 0):
                    if(d3 != 0) and (((d3 + e4) < e3) or e3 == 0):
                        e3 = d3 + e4
                        changeOccurE += 1 
            if changeOccurE > 0:
                f.write("Updating DV matrix at node E\nNew DV matrix at node E = %d %d %d %d %d\n" % (e1, e2, e3, e4, e5))
            else:
                f.write("No change in DV at node E\n")
            position += 1
            f.write("-------\n")
        if(changeOccurA == 0) and (changeOccurB == 0) and (changeOccurC == 0) and (changeOccurD == 0) and (changeOccurE == 0):
            stop += 1
            updated = 1
        else:
            stop = 0
            updated = 0
        if(stop == 5):
            break
        position = 0
        currLine += 1
        roundNum += 1
#---------------------------------------C Round Finishes----------------------------------------------------------------------------------#       
    if currLine == 3:
        changeOccurA = 0
        changeOccurB = 0
        changeOccurC = 0
        changeOccurD = 0
        changeOccurE = 0
        f.write("Round %d: D\n" % (roundNum))
        f.write("Current DV matrix = \n")
        f.write("%d %d %d %d %d\n" % (a1, a2, a3, a4, a5))
        f.write("%d %d %d %d %d\n" % (b1, b2, b3, b4, b5))
        f.write("%d %d %d %d %d\n" % (c1, c2, c3, c4, c5))
        f.write("%d %d %d %d %d\n" % (d1, d2, d3, d4, d5))
        f.write("%d %d %d %d %d\n" % (e1, e2, e3, e4, e5))
        f.write("Last DV matrix = \n")
        f.write("%d %d %d %d %d\n" % (oldA1, oldA2, oldA3, oldA4, oldA5))
        f.write("%d %d %d %d %d\n" % (oldB1, oldB2, oldB3, oldB4, oldB5))
        f.write("%d %d %d %d %d\n" % (oldC1, oldC2, oldC3, oldC4, oldC5))
        f.write("%d %d %d %d %d\n" % (oldD1, oldD2, oldD3, oldD4, oldD5))
        f.write("%d %d %d %d %d\n" % (oldE1, oldE2, oldE3, oldE4, oldE5))
        oldA1 = a1
        oldA2 = a2
        oldA3 = a3
        oldA4 = a4
        oldA5 = a5
        oldB1 = b1
        oldB2 = b2
        oldB3 = b3
        oldB4 = b4
        oldB5 = b5
        oldC1 = c1
        oldC2 = c2
        oldC3 = c3
        oldC4 = c4
        oldC5 = c5
        oldD1 = d1
        oldD2 = d2
        oldD3 = d3
        oldD4 = d4
        oldD5 = d5
        oldE1 = e1
        oldE2 = e2
        oldE3 = e3
        oldE4 = e4
        oldE4 = e5
        if(updated == 0):
            f.write("Updated from last DV matrix or the same? Updated\n")
        else:
            f.write("Updated from last DV matrix or the same? Not updated\n")
        f.write("\n")
        while position < 4:
            if position == 0:
                f.write("Sending DV to node A\nNode A received DV from D\n")
                if((a4 > a2) or a4 == 0) and (a2 != 0):
                    if(b4 != 0) and (((b4 + a2) < a4) or a4 == 0):
                        a4 = b4 + a2
                        changeOccurA += 1
                if((a4 > a3) or a4 == 0) and (a3 != 0):
                    if(c4 != 0) and (((c4 + a3) < a4) or a4 == 0):
                        a4 = c4 + a3
                        changeOccurA += 1
                if((a4 > a5) or a4 == 0) and (a5 != 0):
                    if(e4 != 0) and (((e4 + a5) < a4) or a4 == 0):
                        a4 = e4 + a5
                        changeOccurA += 1
            if changeOccurA > 0:
                f.write("Updating DV matrix at node A\nNew DV matrix at node A = %d %d %d %d %d\n\n" % (a1, a2, a3, a4, a5))
            else:
                f.write("No change in DV at node A\n\n")
            position += 1
            if position == 1:
                f.write("Sending DV to node B\nNode B received DV from D\n")
                if((b4 > b1) or b4 == 0) and (b1 != 0):
                    if(a4 != 0) and (((a4 + b1) < b4) or b4 == 0):
                        b4 = a4 + b1
                        changeOccurB += 1
                if((b4 > b3) or b4 == 0) and (b3 != 0):
                    if(c4 != 0) and (((c4 + b3) < b4) or b4 == 0):
                        b4 = c4 + b3
                        changeOccurB += 1
                if((b4 > b5) or b4 == 0) and (b5 != 0):
                    if(e4 != 0) and (((e4 + b5) < b4) or b4 == 0):
                        b4 = e4 + b5
                        changeOccurB += 1
            if changeOccurB > 0:
                f.write("Updating DV matrix at node B\nNew DV matrix at node B = %d %d %d %d %d\n\n" % (b1, b2, b3, b4, b5))
            else:
                f.write("No change in DV at node B\n\n")
            position += 1
            if position == 2:
                f.write("Sending DV to node C\nNode C received DV from D\n")
                if((c4 > c1) or c4 == 0) and (c1 != 0):
                    if(a4 != 0) and (((a4 + c1) < c4) or c4 == 0):
                        c4 = a4 + c1
                        changeOccurC += 1
                if((c4 > c2) or c4 == 0) and (c2 != 0):
                    if(b4 != 0) and (((b4 + c2) < c4) or c4 == 0):
                        c4 = b4 + c2
                        changeOccurC += 1
                if((c4 > c5) or c4 == 0) and (c5 != 0):
                    if(e4 != 0) and (((e4 + c5) < c4) or c4 == 0):
                        c4 = e4 + c5
                        changeOccurC += 1
            if changeOccurC > 0:
                f.write("Updating DV matrix at node C\nNew DV matrix at node C = %d %d %d %d %d\n\n" % (c1, c2, c3, c4, c5))
            else:
                f.write("No change in DV at node C\n\n")
            position += 1
            if position == 3:
                f.write("Sending DV to node E\nNode E received DV from D\n")
                if((e4 > e1) or e4 == 0) and (e1 != 0):
                    if(a4 != 0) and (((a4 + e1) < e4) or e4 == 0):
                        e4 = a4 + e1
                        changeOccurE += 1
                if((e4 > e2) or e4 == 0) and (e2 != 0):
                    if(b4 != 0) and (((b4 + e2) < e4) or e4 == 0):
                        e4 = b4 + e2
                        changeOccurE += 1
                if((e4 > e3) or e4 == 0) and (e3 != 0):
                    if(c4 != 0) and (((c4 + e3) < e4) or e4 == 0):
                        e4 = c4 + e3
                        changeOccurE += 1
            if changeOccurD > 0:
                f.write("Updating DV matrix at node E\nNew DV matrix at node E = %d %d %d %d %d\n" % (e1, e2, e3, e4, e5))
            else:
                f.write("No change in DV at node E\n")
            position += 1
            f.write("-------\n")
        if(changeOccurA == 0) and (changeOccurB == 0) and (changeOccurC == 0) and (changeOccurD == 0) and (changeOccurE == 0):
            stop += 1
            updated = 1
        else:
            stop = 0
            updated = 0
        if(stop == 5):
            break
        position = 0
        currLine += 1
        roundNum += 1
#---------------------------------------D Round Finishes----------------------------------------------------------------------------------# 
    if currLine == 4:
        changeOccurA = 0
        changeOccurB = 0
        changeOccurC = 0
        changeOccurD = 0
        changeOccurE = 0
        f.write("Round %d: E\n" % (roundNum))
        f.write("Current DV matrix = \n")
        f.write("%d %d %d %d %d\n" % (a1, a2, a3, a4, a5))
        f.write("%d %d %d %d %d\n" % (b1, b2, b3, b4, b5))
        f.write("%d %d %d %d %d\n" % (c1, c2, c3, c4, c5))
        f.write("%d %d %d %d %d\n" % (d1, d2, d3, d4, d5))
        f.write("%d %d %d %d %d\n" % (e1, e2, e3, e4, e5))
        f.write("Last DV matrix = \n")
        f.write("%d %d %d %d %d\n" % (oldA1, oldA2, oldA3, oldA4, oldA5))
        f.write("%d %d %d %d %d\n" % (oldB1, oldB2, oldB3, oldB4, oldB5))
        f.write("%d %d %d %d %d\n" % (oldC1, oldC2, oldC3, oldC4, oldC5))
        f.write("%d %d %d %d %d\n" % (oldD1, oldD2, oldD3, oldD4, oldD5))
        f.write("%d %d %d %d %d\n" % (oldE1, oldE2, oldE3, oldE4, oldE5))
        oldA1 = a1
        oldA2 = a2
        oldA3 = a3
        oldA4 = a4
        oldA5 = a5
        oldB1 = b1
        oldB2 = b2
        oldB3 = b3
        oldB4 = b4
        oldB5 = b5
        oldC1 = c1
        oldC2 = c2
        oldC3 = c3
        oldC4 = c4
        oldC5 = c5
        oldD1 = d1
        oldD2 = d2
        oldD3 = d3
        oldD4 = d4
        oldD5 = d5
        oldE1 = e1
        oldE2 = e2
        oldE3 = e3
        oldE4 = e4
        oldE4 = e5
        if(updated == 0):
            f.write("Updated from last DV matrix or the same? Updated\n")
        else:
            f.write("Updated from last DV matrix or the same? Not updated\n")
        f.write("\n")
        while position < 4:
            if position == 0:
                f.write("Sending DV to node A\nNode A received DV from E\n")
                if((a5 > a2) or a5 == 0) and (a2 != 0):
                    if(b5 != 0) and (((b5 + a2) < a5) or a5 == 0):
                        a5 = b5 + a2
                        changeOccurA += 1
                if((a5 > a3) or a5 == 0) and (a3 != 0):
                    if(c5 != 0) and (((c5 + a3) < a5) or a5 == 0):
                        a5 = c5 + a3
                        changeOccurA += 1
                if((a5 > a4) or a5 == 0) and (a4 != 0):
                    if(d5 != 0) and (((d5 + a4) < a5) or a5 == 0):
                        a5 = d5 + a4
                        changeOccurA += 1
            if changeOccurA > 0:
                f.write("Updating DV matrix at node A\nNew DV matrix at node A = %d %d %d %d %d\n\n" % (a1, a2, a3, a4, a5))
            else:
                f.write("No change in DV at node A\n\n")
            position += 1
            if position == 1:
                f.write("Sending DV to node B\nNode B received DV from E\n")
                if((b5 > b1) or b5 == 0) and (b1 != 0):
                    if(a5 != 0) and (((a5 + b1) < b5) or b5 == 0):
                        b5 = a5 + b1
                        changeOccurB += 1
                if((b5 > b3) or b5 == 0) and (b3 != 0):
                    if(c5 != 0) and (((c5 + b3) < b5) or b5 == 0):
                        b5 = c5 + b3
                        changeOccurB += 1
                if((b5 > b4) or b5 == 0) and (b4 != 0):
                    if(d5 != 0) and (((d5 + b4) < b5) or b5 == 0):
                        b5 = d5 + b4
                        changeOccurB += 1
            if changeOccurB > 0:
                f.write("Updating DV matrix at node B\nNew DV matrix at node B = %d %d %d %d %d\n\n" % (b1, b2, b3, b4, b5))
            else:
                f.write("No change in DV at node B\n\n")
            position += 1
            if position == 2:
                f.write("Sending DV to node C\nNode C received DV from E\n")
                if((c5 > c1) or c5 == 0) and (c1 != 0):
                    if(a5 != 0) and (((a5 + c1) < c5) or c5 == 0):
                        c5 = a5 + c1
                        changeOccurC += 1
                if((c5 > c2) or c5 == 0) and (c2 != 0):
                    if(b5 != 0) and (((b5 + c2) < c5) or c5 == 0):
                        c5 = b5 + c2
                        changeOccurC += 1
                if((c5 > c4) or c5 == 0) and (c4 != 0):
                    if(d5 != 0) and (((d5 + c4) < c5) or c5 == 0):
                        c5 = d5 + c4
                        changeOccurC += 1
            if changeOccurC > 0:
                f.write("Updating DV matrix at node C\nNew DV matrix at node C = %d %d %d %d %d\n\n" % (c1, c2, c3, c4, c5))
            else:
                f.write("No change in DV at node C\n\n")
            position += 1
            if position == 3:
                f.write("Sending DV to node D\nNode D received DV from E\n")
                if((d5 > d1) or d5 == 0) and (d1 != 0):
                    if(a5 != 0) and (((a5 + d1) < d5) or d5 == 0):
                        d5 = a5 + d1
                        changeOccurD += 1
                if((d5 > d2) or d5 == 0) and (d2 != 0):
                    if(b5 != 0) and (((b5 + d2) < d5) or d5 == 0):
                        d5 = b5 + d2
                        changeOccurD += 1
                if((d5 > d3) or d5 == 0) and (d3 != 0):
                    if(c5 != 0) and (((c5 + d3) < d5) or d5 == 0):
                        d5 = c5 + d3
                        changeOccurD += 1
            if changeOccurD > 0:
                f.write("Updating DV matrix at node D\nNew DV matrix at node D = %d %d %d %d %d\n" % (d1, d2, d3, d4, d5))
            else:
                f.write("No change in DV at node D\n")
            position += 1
            f.write("-------\n")
        if(changeOccurA == 0) and (changeOccurB == 0) and (changeOccurC == 0) and (changeOccurD == 0) and (changeOccurE == 0):
            stop += 1
            updated = 1
        else:
            stop = 0
            updated = 0
        position = 0
        if(stop != 5):
            currLine = 0
        else:
            break
        roundNum += 1
#---------------------------------------E Round Finishes----------------------------------------------------------------------------------# 
#At the end of the loop I write out the final output of each row that forms the final matrix.
f.write("Final output:\n")
f.write("Node A DV: %d %d %d %d %d\n" % (a1, a2, a3, a4, a5))
f.write("Node B DV: %d %d %d %d %d\n" % (b1, b2, b3, b4, b5))
f.write("Node C DV: %d %d %d %d %d\n" % (c1, c2, c3, c4, c5))
f.write("Node D DV: %d %d %d %d %d\n" % (d1, d2, d3, d4, d5))
f.write("Node E DV: %d %d %d %d %d\n\n" % (e1, e2, e3, e4, e5))
#Then I do some simple math to find out when the nodes stopped updating.
roundNum = roundNum - 4
f.write("Number of rounds till convergence (Round # when one of the nodes last updated its DV) = %d\n" % (roundNum))
f.write("-------\n")
#And finally I close the output file and end the program.
f.close()