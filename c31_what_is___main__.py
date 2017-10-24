print("About to import support lib")
# noinspection PyProtectedMember
import c31_what_is___main__support as s
print("Done importing support lib")

def main():
    print()
    print("The variable value is {}.".format(s.var))
    # print("The name of the executed python module is {}".format(__name__))

print("Main app name: {}".format(__name__))

if __name__ == '__main__':
    main()
