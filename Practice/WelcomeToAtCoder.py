class practice:
    def __init__(self):
        self.numArray = [1, 2, 5]
        self.s = 'test'

    def calculate(self):
        sum = 0
        numCount = 0
        for num in self.numArray:
            if (1 <= num <= 1000):
                sum += num
                numCount += 1
            else:
                break
        if (numCount == 3 and self.s):
            return ' '.join([str(sum), self.s])
        else:
            return 'Error'

def main():
    prac = practice()
    result = prac.calculate()
    print(result)

if __name__ == '__main__':
    main()