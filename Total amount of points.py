games = ('1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3')
def points(games):
    our_points = 0
    for game in games:
        if game[0] > game[2]:
            our_points = our_points + 3
        elif game[0] == game[2]:
            our_points = our_points + 1
    return our_points
print(points(games))