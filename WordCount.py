#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0
  charCount = 0
  
  for line in textFile:
    lineCount = lineCount + 1
    word = line.split()
    for w in word:
      wordCount = wordCount +1
      charCount += len(line)
    #print(line)
  
  print("lines:", lineCount)
  print("Word:", wordCount)
  print("character:", charCount)
  

if __name__ == '__main__':
  main()
