text = "yoooooo\n This is some text\nHave a good one!\n"

with open("lab running.txt","a") as file:  # vastavalt "w" write või "a" append saad kas üle kirjutada või lisada failile teksti

    file.write(text)