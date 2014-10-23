__author__ = 'Mohamed'
import pickle

class Expression(object):

    names = []
    matrix = None
    file = None
    def __init__(self,path):
        self.file = open(path,'r')


    def load(self):

        contents = self.file.readlines()



        line = contents[0]

        parts = line.split()

        self.names = parts

        size = len(contents[1:])

        self.matrix = []

        for line in contents[1:]:
            parts = line.split()

            self.matrix.append(list(parts))



        self.file.close()







if __name__ == '__main__':

    file = '/home/snouto/Desktop/normalizedDawn.table'

    expression = Expression(file)
    expression.load()

    pickle.dump(expression.matrix,open('/home/snouto/Desktop/expressionData.bin','wb'),protocol=2)
    print("Pickling done ")





