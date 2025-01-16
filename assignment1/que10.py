#10.1
import sys
try:
    num1=int(sys.argv[1])
    num2=int(sys.argv[2])
    print(num1*num2)
except IndexError:
    print("error: please provide two number as commandline arguments")
except ValueError:
    print("error:please enter valid numbers")

#10.2
import sys
strig= sys.argv[1]
print(len(strig))

  
