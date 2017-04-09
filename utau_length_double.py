import sys

# parameters handle
if len(sys.argv) > 2:
    inputname = sys.argv[1]
    print('input file name: ', inputname)
    outputname = sys.argv[2]
    print('output file name: ', outputname)
elif len(sys.argv) > 1:
    inputname = sys.argv[1]
    print('input file name: ', inputname)
    outputname = input('output file name: ')
else:
    inputname = input('input file name: ')
    outputname = input('output file name: ')
print()
if inputname == outputname:
    print('Error: the file names are same.')
    sys.exit(1)

# start file handle
inputfile = open(inputname, 'r')
outputfile = open(outputname, 'w')
while True:
    inputline = inputfile.readline()
    if not inputline: break
#    print(inputline, end='')

    if inputline[0] == '[':
        print(inputline, end='')

    keys = inputline.split('=')
    if len(keys) == 2:
        if keys[0] == 'Tempo' or keys[0] == 'Length':
            outputline = '%s=%.2f\n' % (keys[0], float(keys[1]) * 2)
            print(inputline[:-1], '\t->\t', outputline)    
        else:
            outputline = inputline
    else:
        outputline = inputline

    outputfile.write(outputline)
outputfile.close()
inputfile.close()
