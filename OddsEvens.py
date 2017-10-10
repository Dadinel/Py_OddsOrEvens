from random import randrange

def printLine():
    print( "-" * 25 )

def printError():
    print( "The values needs be integer." )

def breakLine():
    print( "\n" )

printLine()
print( "Odds or Evens" )
printLine()

print( "\nChoose:" )
print( "1 - Odd" )
print( "2 - Even\n" )

choose = 0
player = 0

try:
    choose = int( input( "Option: " ) )

    if choose != 1 and choose != 2:
        raise print( "The choise value needs be one or two." )
except:
    printError()
else:
    try:
        #print( "\nChoose a number: ???" )
        player = int( input( "\nChoose a number: " ) )
    except:
        printError()
    else:
        computer = randrange( 1 , 10 )
        result = player % computer

        winner = "You loose! =("
        cpuchose = ""
        youchose = ""

        if choose == 1:
            youchose = "Odd"
            cpuchose = "Even"
        else:
            youchose = "Even"
            cpuchose = "Odd"

        breakLine()
        printLine()
        print( "CPU is {0} and chose {1}".format( cpuchose , computer ) )
        print( "You is {0} and chose {1}".format( youchose , player ) )
        printLine()

        breakLine()
        printLine()
        print( "Winner" )
        printLine()

        if choose == 1:
            if result == 0:
                winner = "You win! =)"
        else:
            if result > 0:
                winner = "You win! =)"

        print( winner )
        printLine()
