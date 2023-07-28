

for i in range(-1,len(data)):
    if player1 == data[i][0]:
        if xstat == 'Accuracy':
            xstat_player1.append(data[i][5])
        if xstat == 'Big Time Throws':
            xstat_player1.append(data[i][11])

