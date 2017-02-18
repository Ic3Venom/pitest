def test1():
    pass
def test2():
    pass
def test3():
    pass


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
            test1()
            break

        elif userInput.lower() in ['2', 'ten']:
            test2()
            break

        elif userInput.lower() in ['3', 'all']
            test3()
            break
if __name__ == '__main__':
    main()

    exit(0)
