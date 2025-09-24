with open("output.txt","w") as file:
    data=input("Enter text to write to the file: " )
    file.write(data)
    print("Data successfully written to output.txt.",end="\n\n")
with open("output.txt","a") as file:
    data=input("Enter additional text to append: ")
    file.write("\n"+data)
    print("Data successfully appended.",end="\n\n")
with open("output.txt","r") as file:
    content=file.read()
    print("Final content of output.txt:")
    print(content)
