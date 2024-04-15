from socket import *

def find_the_request (sentence):

    first_line = sentence.split('\n')[0]
    server_request = first_line.split(' ')[1]

    return server_request

def Type (server_request) :

    out = ""

    if  server_request in ["/", "/localfile.html", "/index.html", "/main_en.html", "/en", "/ar"]:
        out = f'HTTP/1.1 200 OK\nContent-Type: text/html\n\n',"UTF-8"

    elif server_request == "/styles.css":
        out = f'HTTP/1.1 200 OK\nContent-Type: text/css\n\n',"UTF-8"

    elif server_request == "/th.jpg":
        out = f'HTTP/1.1 200 OK\nContent-Type: image/jpeg\n\n',"latin-1"

    elif server_request == "/img2.png":
        out = f'HTTP/1.1 200 OK\nContent-Type: image/png\n\n',"latin-1"
    
    elif server_request in ["/laptops.txt", "/SortByName", "/SortByPrice"]:
        out = f'HTTP/1.1 200 OK\nContent-Type: text/plain\n\n',"UTF-8"

    elif server_request in ["/azn", "/so", "/bzu"]:
        out = f'HTTP/1.1 307 Temporary Redirect\nContent-Type: text/html\n',"UTF-8"

    else :
        out = f'HTTP/1.1 404 Not Found\nContent-Type: text/html\n\n',"UTF-8"
        print("error")

    return out

def get_second_word_as_integer(line):
    # Split the line into words
    words = line.split()
    
    # Check if there is at least a second word
    if len(words) > 1:
        try:
            # Try to convert the second word to an integer
            return int(words[1])
        except ValueError:
            pass
    
    # If there is no second word or it's not an integer, return a large value
    return float('inf')

def sort_the_file (method):

    with open('laptops.txt', 'r') as file:
        # Read the lines into a list
        if method ==1 :
            lines = file.readlines()
        elif method ==2:
            lines = sorted(file.readlines(), key=get_second_word_as_integer)

    if method ==1:
        lines.sort()

    # Alternatively, if you want to sort in descending order, you can use:
    # lines.sort(reverse=True)

    # Open the file for writing (this will overwrite the original file)
    with open('SortedFile.txt', 'w') as file:
        # Write the sorted lines back to the file
        file.writelines(lines)

    f = open("SortedFile.txt", "rb")
    return f.read()


serverPort = 12345
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print ("The server is ready to receive")

reqLine =""
while True:
    try:
        connectionSocket, addr= serverSocket.accept()
        sentence = connectionSocket.recv(2048).decode()

        ip = addr[0]
        port = addr[1]

        server_request = ""

        if len(sentence) > 1:
            server_request = find_the_request(sentence)
        else:
        # Handle the error here
            pass
        

        Content_Type,charset = Type(server_request)

        reqLine =reqLine + str(server_request)

        print("server_request = |"+ server_request+"|")
        print("Content_Type = |"+Content_Type+"|")
        print("charset = |"+charset+"|")


        if charset == "" :
            connectionSocket.send(Content_Type.encode())
        else :
            connectionSocket.send(Content_Type.encode(charset))
        
        
        if server_request in ["/", "/index.html", "/main_en.html", "/en"]:
            f1 = open("main_en.html", "rb")
            data1 = f1.read()
            connectionSocket.send(data1)
            f1.close()

        elif server_request == "/ar":
            f9 = open("HTar.html", "rb")
            data9 = f9.read()
            connectionSocket.send(data9)
            f9.close()


        elif server_request == "/localfile.html":
            f6 = open("localfile.html", "rb")
            data6 = f6.read()
            connectionSocket.send(data6)
            f6.close()


        elif server_request == "/styles.css":
            f2 = open("styles.css", "rb")
            data2=f2.read()
            connectionSocket.send(data2)
            f2.close()

        
        elif server_request == "/th.jpg":
            f3 = open("th.jpg", "rb")
            data3=f3.read()
            connectionSocket.send(data3)
            f3.close()
            

        elif server_request == "/img2.png":
            f4 = open("img2.png", "rb")
            data4=f4.read()
            connectionSocket.send(data4)
            f4.close()


        elif server_request == "/laptops.txt":
            f5 = open("laptops.txt", "rb")
            data5=f5.read()
            connectionSocket.send(data5)
            f5.close()


        elif server_request == "/SortByName":
            data6 = sort_the_file(1)
            connectionSocket.send(data6)


        elif server_request == "/SortByPrice":
            data7 = sort_the_file(2)
            connectionSocket.send(data7)


        elif server_request == "/azn":
            connectionSocket.send("Location: http://www.amazon.com\n\n".encode())
        elif server_request == "/so":
            connectionSocket.send("Location: http://www.stackoverflow.com\n\n".encode())
        elif server_request == "/bzu":
            connectionSocket.send("Location: https://www.birzeit.edu\n\n".encode())

        
        else :
            f8 = open("errorStep.html", "rb")
            data8 = f8.read()
            connectionSocket.send(data8)
            f8.close()


        connectionSocket.close()

        print(reqLine)


    except OSError:
        print ("IO error")
    else:
        print ("OK")
