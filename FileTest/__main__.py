"""
    Curso Python
    pruebas con los flujos de ficheros
"""

import os

class ManageFile:
    listLines = {}
    encoding = 'UTF-8'
    newFileName = ''
    actualFileName = ''

    def __init__(self, fileName, newFileName, encoding):
        self.actualFileName = str(fileName)
        self.newFileName = str(newFileName)
        self.encoding = str(encoding)

        #   File Stream
        try:
            file = open(str(fileName), 'r', encoding=self.encoding)
            file.seek(0)
            count = 1
            for line in file.readlines():
                self.listLines[count] = line
                count += 1
            #   self.listLines = file.readlines()
            print('File is successfully loaded to buffer')
            print('Size of the loaded file is: ', (os.stat(str(fileName))).st_size)
            if len(self.listLines) > 0:
                print('File content: ')
                print('----------------------------------------------------------------')
                self.__printFileLines(self.listLines)
                print('\n----------------------------------------------------------------')
            else:
                print('File is empty')
            file.close()
            del file
        except FileNotFoundError:
            print("No such file or directory: 'sds'")

    def __printFileLines(self, listLines):
        for line in listLines.keys():
            print("{}: {}".format(line, listLines[line]), end='')

    def printFileLines(self):
        if not self.listLines:
            print('File is empty')
        else:
            print('----------------------------------------------------------------')
            for line in self.listLines.keys():
                print("{}: {}".format(line, self.listLines[line]), end='')
            print('\n----------------------------------------------------------------')

    def changeLines(self, *args):
        dictionary = {}
        flag = False
        #   Check for correct input format
        if len(args) % 2 == 0:
            for i in range(0, len(args) - 1, 2):
                try:
                    if isinstance(args[i], int) and 0 < int(args[i]) <= len(self.listLines):
                        flag = True
                        for var in range(0, len(args)-1, 2):
                            dictionary[args[int(var)]] = args[var + 1]
                    else:
                        flag = False
                        print("Error in input format: ", args)
                        print("The number of line trying to change is not exist")
                        break
                except:
                    flag = False
                    print("Error in input format: ", args)
                    print("Incorrect type of number")
                    break

        else:
            flag = False
            print("Error in input format: ", args)

        if flag:
            for i in dictionary.keys():
                self.listLines[i] = dictionary[i] + str('\n')
            print("Operation completed successfully")

    def writeLinesToFile(self):
        file = open(str(self.newFileName), 'w', encoding=self.encoding)
        file.seek(0)
        file.writelines(self.listLines.values())
        file.close()
        del file

    def getLinesByText(self, textToFind):
        dictionary = {}
        count = 1
        for line in self.listLines.keys():
            if str(textToFind).lower() in self.listLines[line].lower():
                dictionary[count] = self.listLines[line]
            count += 1

        if not dictionary:
            print("Algorithm can't find occurrences in lines")
        else:
            print("Algorithm found occurrences in the following lines: ", dictionary.keys())

        op = int(input("""What do you want to do with that lines?
        Input 1 for print the lines,
        Input 2 for delete them,
        Input 3 for export them to a new file: """))

        if op == 1:
            for i in dictionary.keys():
                print("{}: {} ".format(i, dictionary[i]), end='')
        elif op == 2:
            self.deleteLines(dictionary)
        elif op == 3:
            filename = input("Please type a filename: ")
            encodef = input("Please type encoding (Ex: UTF-8): ")
            file = open(str(filename), 'w', encoding=encodef)
            file.writelines(dictionary.values())

    def deleteLines(self, lines):
        auxDict = {}
        count = 1
        for i in self.listLines.keys():
            if i not in lines.keys():
                auxDict[count] = self.listLines[i]
                count += 1
        self.listLines = auxDict




"""
actualFile = 'ReleaseNotes.html' #input("Name of actual file: ")
newFile = 'lala.txt' #input("Name of new file: ")
encode = 'UTF-8'

manager = ManageFile(actualFile, newFile, encode)
manager.getLinesByText('href')
manager.printFileLines()
"""