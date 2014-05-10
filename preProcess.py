#!/usr/bin/python2.7

import csv

class PlayerInfo:
    def __init__(self, position, height, weight):
        if(position.strip() == 'G'):
            self.position = 1
        if(position.strip() == 'F'):
            self.position = 3
        if(position.strip() == 'C'):
            self.position = 2
        self.height = height
        self.weight = weight
    def __str__(self):
        return 'Position: ' + str(self.position) + ', Height: ' + str(self.height) + ', Weight: ' + str(self.weight) 
    def __repr__(self):
        return 'Position: ' + str(self.position) + ', Height: ' + str(self.height) + ', Weight: ' + str(self.weight) 

class PlayerStats:
# order of stats
# asts, blk, dreb, fga, fgm, fta, ftm, height, oreb, pf, pts, stl, to, tpa, tpm, weight 
    def __init__(self, mins, pts, oreb, dreb, asts, stl, blk, to, 
        pf, fga, fgm, fta, ftm, tpa, tpm, height, weight, position):
        self.mins = mins
        #self.pts = self.__per_100_mins(pts)
        self.oreb = self.__per_100_mins(oreb)
        self.dreb = self.__per_100_mins(dreb)
        self.asts = self.__per_100_mins(asts)
        self.stl = self.__per_100_mins(stl)
        self.blk = self.__per_100_mins(blk)
        self.to = self.__per_100_mins(to)
        self.pf = self.__per_100_mins(pf)
        self.fga = self.__per_100_mins(fga)
        self.fgm = self.__per_100_mins(fgm)
        self.fta = self.__per_100_mins(fta)
        self.ftm = self.__per_100_mins(ftm)
        self.tpa = self.__per_100_mins(tpa)
        self.tpm = self.__per_100_mins(tpm)
        self.height = (float(height) - 77)/28  # (score - mean) / (max-min)
        self.heightSquare = str((self.height) * (self.height))
        self.weight = (float(weight) - 207)/197 # (score - mean) / (max-min)
        self.weightSquare = str((self.weight) * (self.weight))
        self.heightWeight = str((self.height) * (self.weight))
        self.position = position

    def __per_100_mins(self, stat):
        return (float(stat) * 100) / (float) (self.mins)
        #return stat

    def __str__(self):
        keys = sorted(self.__dict__.keys())
        keys.remove('position')
        keys.remove('mins')
        return ', '.join(str(self.__dict__[key]) for key in keys)

         
def main():
    playerPosDict = {}
    with open('players.csv', 'rU') as posFile:
        positionReader = csv.reader(posFile, delimiter=',')
        for row in positionReader:
            if(len(row) == 12):
                if(row[3] != '' and row[3] != 'NULL' 
                    and row[6] != 'NULL' and row[7] != 'NULL'
                    and row[8] != 'NULL'):
                    playerPosDict[row[0].strip()] = PlayerInfo(row[3], 
                        (float(row[6])*12)+float(row[7]), row[8])
    print 'playerInfoCount: ' + str(len(playerPosDict))
    posFile.close()
    with open('player_career.csv', 'rU') as statFile:
        finalStatCount = 0;
        features_file = open('features.csv', 'w');
        position_file = open('position.csv', 'w');
        statReader = csv.reader(statFile, delimiter=',')
        for row in statReader:
            if(row[3] != '' and int(row[5]) > 100):
                id = row[0].strip()
                if id in playerPosDict:
                    playerInfo = playerPosDict[id]
                    position = playerInfo.position
                    height = playerInfo.height
                    weight = playerInfo.weight
                    playerStats = PlayerStats(row[5],row[6],row[7],row[8],
                        row[10],row[11],row[12],row[13],row[14],row[15],row[16],
                        row[17],row[18],row[19],row[20], height, weight, position)
                    if position == 1 or position == 2:
                        finalStatCount = finalStatCount + 1
                        features_file.write(str(playerStats) + '\n')
                        position_file.write(str(position) + '\n')
    print 'finalStatCount: ' + str(finalStatCount)
    statFile.close()
    features_file.close()
    position_file.close()

if __name__ == "__main__":
    main()
