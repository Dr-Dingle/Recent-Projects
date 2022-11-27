import sys

def response(x):
    print('Thank you have a nice day!')

#stops the program  

def chart(x):
    filename = 'airportdata.txt'
    mode = 'r'
    try:
        fileObj = open(filename, mode)
        for lines in fileObj:
            print(lines)

    except:
        print("Unable to open file")
        sys.exit
    
#Open the file for readin and reads it 

def choices(h):
    
    if h=='1':
         
         try:
             filename = open('airportdata.txt')
             content = filename.readlines()
             print(content[4:0])
         except:
            print("Unable to open file")
            sys.exit

#I ran into problems here so you can disregard whats already here

#This is the main area that needs to be modified. It needs to take the users input and (preferably) reads the file and takes the number and prints it,
#confirminig if this is waht the user truly wished

def main():
    x=input('Hello, would you like to take a look at our available flight options? Press "Y" to view options or press "N" to quit')
    if x=="N" or x=="n":
        print(response(x))

#ask the user if they want to search their flying options. If yes then it opens and reads the files in the chart fuction. If not then it closes in the response function.
#upon reading this there needs to a loop after it gets done runnin the code.

    if x=="Y" or x=="y":
        print(chart(x))
        h=input('Which of the options above best supports your interest (select 1-5)?')
    
#this is where theyr supposed to select their option promtpting the choices function



        
main()
