import time
import sys, os

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("useage : ", sys.argv[0], " EXE_FILE_NAME INPUT_FILE_NAME")
        sys.exit(0)

    start = time.time() # check time
    os.system(os.getcwd() + "/" + sys.argv[1] + " < " + os.getcwd() + "/" + sys.argv[2]) # get absolute path, set pipe, exec file
    end = time.time() # check time
    print("time: ", end - start)
