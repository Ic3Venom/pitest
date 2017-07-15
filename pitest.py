import struct

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
        print 'Something went wrong when initial user input! Exiting program.'
        exit(1)

    with open('pi10000.bin', 'rb') as f:
        while True:
            try:
                f.seek(i + 3)
                i += testLen
                byte = int( struct.unpack( str(testLen) + 's', f.read(testLen) )[0] )
            except:
                print 'Something went wrong when reading index %d of pi.bin! Exiting program.' % i
                raw_input()
                exit(1)

            if byte is None:
                print 'You got to all the way to 10,000 digits! Congratulations!'
            elif not userInput == byte:
                print 'You remembered %d digits of pi! (Typed %d instead of %d)' % (i, userInput, byte)
                break

            try:
                if testLen in [1 , 2]:
                    output = '%d: ' % (i + 1)

                elif testLen == 10:
                    output = '%d->%d: ' % (i, (i + 10))
                else:
                    print 'Something went terribly wrong! Report this at the GitHub repo.'

                userInput = int( raw_input(output) )

            except:
                print 'Something went wrong when obtaining user input! Exiting program.'
                raw_input()
                exit(1)

def main():
    while True:
        print 'What pi test would you like to take? (type \'help\' for help)'
        userInput = raw_input(">>> ")

        if userInput.lower() == 'help':
            print '\nWelcome to the pitest.py help page!'
            print 'Listing all input modes:'
            print '* For single digit reciting, type \'1\' or \'single\''
            print '* For ten digits at a time, type \'2\' or \'ten\''
            print '* To start reciting at a certain, type \'4\' or \'position\''
            print 'Any bugs, issues, requests, suggestions? Put them in the GitHub repo.\n'

        elif userInput.lower() == 'quit':
            exit(0)

        elif userInput.lower() in ['1', 'single']:
            test(1)
            break

        elif userInput.lower() in ['2', 'ten']:
            test(10)
            break

        elif userInput.lower() in ['4', 'position']:
            test(2)
            break

        raw_input()

if __name__ == '__main__':
    main()

    exit(0)
