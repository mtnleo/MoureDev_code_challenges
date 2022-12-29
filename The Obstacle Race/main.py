## Create a function that evaluates if an athlete
## has completed an obstacle race:
"""
The function will get two parameters:
    - An array/list that can only contain two strings: "run" or "jump"
    - A string that represents the track, and can only contain "_" (ground)
      or "|" (hurdle)
The function will print the outcome of the race:
    - if the athlete has a "run" in "_" (ground) and "jump" in "|" (hurdle)
      it'll be correct, and the track string will stay the same
    - if the athlete "jump"s on "_", the track symbol will be replaced for an "x"
    - if the athlete "run"s on "|", the track symbol will be replaced for a "/"
- The function will return a boolean, that indicated whether the athlete
finished the race or not;
He can't make any mistakes (jumps on ground, or run on hurdles)

"""
def validate_track(track):
    for letter in track:
        if letter != "_" and letter != "|":
            print("Invalid track, please try again")
            return False

    return True

def validate_athlete_race(race):
    for word in race:
        if word.lower() != "run" and word.lower() != "jump":
            print("Invalid athlete moves, please try again")
            return False
    
    return True

def vaulting(athlete_race, track):
    if validate_track(track) == False:
        return False

    if validate_athlete_race(athlete_race) == False:
        return False
    
    if len(track) <= len(athlete_race):
        race_track = list(track)
        for i in range(0, len(track)):
            if race_track[i] == "_" and athlete_race[i].lower() == "jump":
                race_track[i] = "x"
            elif track[i] == "|" and athlete_race[i].lower() == "run":
                race_track[i] = "/"

        print("Track before the race:  ", "".join(track))
        print("------------------")
        print("Track after the race:   ", "".join(race_track))

    try:
        if "".join(track) == "".join(race_track):
            return True
        else:
            return False
    except:
        return False

    
    
    

if __name__ == "__main__":
    athlete_race = ["run", "run", "jump", "Run", "jump","run"]
    track = "__|_|_"

    print(vaulting(athlete_race, track))

