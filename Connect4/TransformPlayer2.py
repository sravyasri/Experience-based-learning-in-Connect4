import string
fp=open("Player2","r")
fp1=open("Player2Final","a+")

for line in fp:
    if "end" not in line:
        line = line.split(",")
        if len(line)==2:
            newboard = string.replace(line[0], "2", "3")
            board = string.replace(newboard, "1", "2")
            finalboard = string.replace(board, "3", "1")
            if "P1" in line[1]:
                fp1.write(finalboard + ",P2" + "\n")
            else:
                fp1.write(finalboard + ",P1" + "\n")
        else:
            newboard = string.replace(line[0], "2", "3")
            board = string.replace(newboard, "1", "2")
            finalboard = string.replace(board, "3", "1")
#             fp1.write(finalboard + line[1]+line[2])
            if "P1" in line[1]:
                if "-" in line[2]:
                    line[2] = line[2].replace("-","")
#                 else:
#                     line[2] = line[2].replace("-","")
                fp1.write(finalboard + ",P2," + line[2])
            else:
                fp1.write(finalboard + ",P1," + line[2])
    else:
        fp1.write("end"+"\n")

fp1.close()  
fp.close()  
    
    
    
#       board=board.split(" ")
    
            
