def points(games):
    points = 0
    
    for game in games:
        x, y = game.split(":")
        if x > y: 
            points += 3
        elif x == y:
            points +=1 
        else:
            pass
        
    return points
