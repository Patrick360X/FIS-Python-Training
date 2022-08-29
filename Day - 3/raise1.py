try:
    age = 800
    if age > 100:
        raise Exception("Ghost")
    else:
        print("Human")
except:
    print("I am a Ghost")