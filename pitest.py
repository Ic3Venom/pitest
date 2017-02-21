def test( testLen ):
    i = 0

    try:
        if testLen == 1:
            userInput = int( raw_input('Enter the next digit: 3.') )

        elif testLen == 2:
            i = int( raw_input('What digit would you like to start on?:' ) )
            testLen = 1
            userInput = int( raw_input( 'Continue from digit %d: ' % i) )

        elif testLen == 10:
            userInput = int( raw_input( 'Enter the next ten digits: 3.' ) )

    except:
        print 'Something went wrong when obtaining user offset! Exiting program.'
        exit(1)

    with open('pi.bin', 'r') as f:
        f.seek(i)

        try:
            byte = int( f.read(testLen) )

        except:
            print 'Something went wrong when reading index %d of pi.bin! Exiting program.' % i
            exit(1)

        while byte != '':
            if userInput == byte:
                i    += testLen
                byte = int( f.read(testLen) )
            else:
                print 'You remembered %d digits of pi! (Typed %d instead of %d)' % (i, userInput, byte)
                break

            try:
                if testLen in [1 , 2]:
                    output = '%d: ' % (i + 1)

                elif testLen == 10:
                    output = '%d->%d: ' % i, (i + 10)

                else:
                    output = "Enter all digits up to the feynman point:"

                userInput = int( raw_input(output) )

            except:
                print 'Something went wrong when obtaining user input! Exiting program.'
                exit(1)
        else:
            print 'You got to all the way to the Feynman point! Congratulations!'

def main():
    while True:
        print 'What pi test would you like to take? (type \'help\' for help)'
        userInput = raw_input(">>> ")

        if userInput.lower() == 'help':
            print '\nWelcome to the pitest.py help page!\n'
            print 'For single digit reciting, type \'1\' or \'single\''
            print 'For ten digits at a time, type \'2\' or \'ten\''
            print 'For the all digits at once, type \'3\' or \'all\''
            print 'To start reciting at a certain, type \'4\' or \'position\''
            print '\nAny bugs, issues, requests? Put them in the GitHub repo.\n'

        elif userInput.lower() == 'quit':
            exit(0)

        elif userInput.lower() in ['1', 'single']:
            test(1)
            break

        elif userInput.lower() in ['2', 'ten']:
            test(10)
            break

        elif userInput.lower() in ['3', 'all']:
            test(-1)
            break

        elif userInput.lower() in ['4', 'position']:
            test(2)
            break

if __name__ == '__main__':
    main()

    exit(0)
