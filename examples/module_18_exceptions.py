options = {"OPT1":"This gonna be fun!",
           "OPT2":"This not gonna be fun!",
           "OPT3":"This gonna be bad!"
           }

try:
    defa = options['OPT4']
except:
    print("This is not an option!")

print("program keeps running....")

try:
    defa = options['OPT4']
except:
    print("This is still not an option!")
finally:
    print("Your options are:")
    for opt in options:
        print(opt)