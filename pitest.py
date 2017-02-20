def test( testLen ):
    print 'Lets begin! 3. ...'

    with open('pi.bin', 'r') as f:
        byte = int( f.read(testLen) )
        i    = 0
        while byte != "":
            if i == 1
                userInput = int( raw_input("Enter the next digit (%d):" % (i + 3)) )
            elif i == 10
                userInput = int( raw_input("Enter the next ten digits (%d-%d):" % (i + 3), (i + 13)) )
            else:
                userInput = int( raw_input("Enter all digits up to the feynman point: ")


            if not userInput == byte:
                print 'You recited %d digits of pi (Typed %d instead of %d)' % (i, int(userInput), int(byte))
                break

            i    += 1
            byte = int( f.read(1) )
        else:
            print 'You recited all the way to the Feynman point! Congratulations!'''

def main():
    while True:
        print 'What pi test would you like to take? (type \'help\' for help)'
        userInput = raw_input(">>> ")

        if userInput.lower() == 'help':
            print '\nWelcome to the pitest.py help page!\n'
            print 'For single digit reciting, type \'1\' or \'single\''
            print 'For ten digits at a time, type \'2\' or \'ten\''
            print 'For the all digits at once, type \'3\' or \'all\''
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

if __name__ == '__main__':
    main()

    exit(0)
