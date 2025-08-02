#basic concepts
# file = open("sample.txt","w")                #"hello" or 'hello' both will work
# file.write("hello mr. how do u do")
# file.close()

# file = open('sample.txt','r')
# content = file.read()
# file.close()
# print("content of sample file is:",content)   #print(f"content of sample file is:{content}")

#FILE MANAGER JO TXT FILES PER HI WORK KAREGA NOT BINARY FILES

import os

def create_files(filename):
    try:                                         #try saare errors batayega ki if file name jo user ne bataya h vo already exists ya kuvh bhi error jis vajah se file ni banai jaa skti
        with open(filename,'x') as f:            #with se close() likhna ni padega,x mode creates new file n ensures existing file me overwrite na krdo tum by raising fileexisterror
            print(f"File {filename}:Created Successfully!")

    except FileExistsError:                          
        print(f"File {filename} already exists!")

    except Exception as E:                       #koi bhi or possible error 
        print("An error occured!")

def view_all_files():
    files = os.listdir()                         #humari current directory ki sari files ko list krdega jo jo available h
    if not files:                                #basically sabke namo ki list bana dega
        print("No files found!")

    else:
        print("Files in directory:")
        for file in files:
            print(file)

def del_file(filename):
    try:
        os.remove(filename)
        print(f"File {filename}:Deleted successfully!")

    except FileNotFoundError:
        print(f"File {filename}:Not found!")

    except Exception as E:
        print("An error occured!")

def read_file(filename):
    try:
        with open(filename,'r') as f:
            content = f.read()
            print(f"Content of file {filename}:\n",content)

    except FileNotFoundError:
        print(f"File {filename}:Not found!")

    except Exception as E:
        print("Some error occurred!")

def edit_file(filename):                            #yeh write hi banaya h humne with a mode to append rather than overwrite on the file
    try:
        with open(filename,'a') as f:               #hum yaha per edit ko add mann re h that user wants to add more data to the file
            content = input("Enter data you want to add:\n")
            f.write(content + "\n")                 #content plus new line taki dubara func call ho to new line se content add hoye
            print(f"Content added to {filename}:Successfully")

    except FileNotFoundError:
         print(f"File {filename} :Not found!")

    except Exception as E:
        print("Some error occurred!")

def main():
    print("*-*-*-FILE MANAGER PROGRAM-*-*-*")
    print("1.Create\n2.View\n3.Read\n4.Delete\n5.Edit/Write\n6.Exit")

    while True:
        ch = int(input("Enter your choice:"))

        if ch == 6:
            print("Program closed!!!")
            break
        elif ch == 1:
            file=input("Enter filename:")
            create_files(file)

        elif ch == 2:
            view_all_files()

        elif ch == 3:
            file=input("Enter filename:")
            read_file(file)

        elif ch == 4:
            file=input("Enter filename:")
            del_file(file)

        elif ch == 5:
            file=input("Enter filename:")
            edit_file(file)

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

