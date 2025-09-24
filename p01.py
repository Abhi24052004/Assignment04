try:
    with open("sampl.txt","r") as file:
        lines = file.readlines()
    count=0
    print("Reading file content:")
    for line in lines:
        count+=1
        print(f"Line {count}: {line}",end='')
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
