from hashlib import sha1
import time

# Define variables for global usage.
passwordList = []
dictionary = []
solutionTable = []
userSelection = ""

# Read in the files (passwords.txt) & (dictionary.txt).
def fileLoader():
    print(
        "User Selection:\n 1 = Noah Hamilton\n"
        "2 = James Hunter Ireland\n 3 = Sascha Heinzel\n"
    )
    userInput = input("Who are you?:")
    userSelection = userInput
    if userSelection == "1":
        passwordFile = "C:\\Users\\idach\\Documents\\USF\\SchoolWork\\S22\\Cryptography & Data Security\\passwords.txt"
        dictionaryFile = "C:\\Users\\idach\\Documents\\USF\\SchoolWork\\S22\\Cryptography & Data Security\\dictionary.txt"
    if userSelection == "2":
        passwordFile = "/Users/jhunterireland/Desktop/Course Work/Cryptography & DS Spring 2022/Project files/passwords.txt"
        dictionaryFile = "/Users/jhunterireland/Desktop/Course Work/Cryptography & DS Spring 2022/Project files/dictionary.txt"
    if userSelection == "3":
        passwordFile = "C:\\Users\\heinz\\Desktop\\USF\\Cryptography & Data Security\\Project\\Project files\\passwords.txt"
        dictionaryFile = "C:\\Users\\heinz\\Desktop\\USF\\Cryptography & Data Security\\Project\\Project files\\dictionary.txt"
    if userSelection == "4":
        passwordFile = "passwords.txt"
        dictionaryFile = "dictionary.txt"

    with open(passwordFile) as f:
        passwordList = f.readlines()
    with open(dictionaryFile, encoding="utf-8-sig") as g:
        dictionaryList = g.readlines()

    # Remove carriage returns in dictionaryList.
    for word in dictionaryList:
        word = word.strip()
        dictionary.append(word)

    # Remove carriage returns in passwordList and create solutionTable variable for export.
    for line in passwordList:
        entry = []
        line = line.strip()
        user = line.split(" ")[0]
        hashPwd = line.split(" ")[1]
        plaintext = ""
        entry.append(user)
        entry.append(hashPwd)
        entry.append(plaintext)
        solutionTable.append(entry)


# Return the number of remaining passwords
def getRemainingPasswords():
    pwdsRemaining = 0
    for index, pwd in enumerate(solutionTable):
        if pwd[2] == "":
            pwdsRemaining += 1
    # print("Passwords remaining: " + str(pwdsRemaining))
    return pwdsRemaining


# Attempt single string as password.
def singleStrCracker():
    print("Begin singleStrCracker function.")
    # Read the first value from the dictionary.
    for word in dictionary:
        shaAttempt = sha1(word.encode("ascii"))
        attemptedHashPwd = shaAttempt.hexdigest()
        for index, pwd in enumerate(solutionTable):
            if attemptedHashPwd == pwd[1]:
                print(
                    "Password hash matched for User ID:"
                    + str(index + 1)
                    + " using "
                    + word
                )
                # Put password into table.
                solutionTable[index][2] = word
    print("Finished singleStrCracker function.")


# Attempt two strings as password.
def doubleStrCracker():
    print("Beginning doubleStrCracker function.")
    # Read the first word from the dictionary.
    for firstWord in dictionary:
        for secondWord in dictionary:
            combo = firstWord + secondWord
            shaAttempt = sha1(combo.encode("ascii"))
            attemptedHashPwd = shaAttempt.hexdigest()
            for index, pwd in enumerate(solutionTable):
                if attemptedHashPwd == pwd[1]:
                    print(
                        "Password hash matched for User ID:"
                        + str(index + 1)
                        + " using "
                        + firstWord
                        + " "
                        + secondWord
                    )
                    # Put password into table.
                    solutionTable[index][2] = combo
    print("Finished doubleStrCracker function.")


# Attempt single string plus numbers as password.
def strNumCracker():
    print("Beginning strNumCracker function.")
    # Read the first value from the dictionary.
    for word in dictionary:
        # Attempt 0 -> 99999.
        for numDigits in range(5):
            countLength = "%0" + str(numDigits + 1) + "d"
            for i in range(pow(10, numDigits + 1)):
                testValue = countLength % i
                combo = word + testValue
                shaAttempt = sha1(combo.encode("ascii"))
                attemptedHashPwd = shaAttempt.hexdigest()
                for index, pwd in enumerate(solutionTable):
                    if attemptedHashPwd == pwd[1]:
                        print(
                            "Password hash matched for User ID:"
                            + str(index + 1)
                            + " using "
                            + combo
                        )
                        # Put password into table.
                        solutionTable[index][2] = combo
    print("Finished strNumCracker function.")


# Attempt numeric combinations as password.
def numCracker():
    print("Begin numCracker function.")
    # Attempt 0 -> 9999999999.
    for numDigits in range(10):
        countLength = "%0" + str(numDigits + 1) + "d"
        for i in range(pow(10, numDigits + 1)):
            testValue = countLength % i
            shaAttempt = sha1(testValue.encode("ascii"))
            attemptedHashPwd = shaAttempt.hexdigest()
            for index, pwd in enumerate(solutionTable):
                if attemptedHashPwd == pwd[1]:
                    print(
                        "Password hash matched for User ID:"
                        + str(index + 1)
                        + " using "
                        + testValue
                    )
                    # Put password into table.
                    solutionTable[index][2] = testValue
    print("Finished numCracker function.")


# Attempt two strings plus numbers at the end as password.
def doubleStrNumCracker():
    print("Beginning doubleStrNumCracker function.")
    # Read the first word from the dictionary.
    for firstWord in dictionary:
        # Read the second word from the dictionary.
        for secondWord in dictionary:
            # Attempt 0 -> 99999.
            for numDigits in range(3):
                countLength = "%0" + str(numDigits + 1) + "d"
                for i in range(pow(10, numDigits + 1)):
                    testValue = countLength % i
                    combo = firstWord + secondWord + testValue
                    shaAttempt = sha1(combo.encode("ascii"))
                    attemptedHashPwd = shaAttempt.hexdigest()
                    for index, pwd in enumerate(solutionTable):
                        if attemptedHashPwd == pwd[1]:
                            print(
                                "Password hash matched for User ID:"
                                + str(index + 1)
                                + " using "
                                + firstWord
                                + " "
                                + secondWord
                                + " "
                                + testValue
                            )
                            # Put password into table.
                            solutionTable[index][2] = combo
    print("Finished doubleStrNumCracker function.")


# Attempt three strings as password.
def tripleStrCracker():
    print("Beginning tripleStrCracker function.")
    # Read the first value from the dictionary.
    for firstWord in dictionary:
        # Read the second word from the dictionary.
        for secondWord in dictionary:
            # Read the third word from the dictionary.
            for thirdWord in dictionary:
                if getRemainingPasswords() == 0:
                    print("Finished doubleStrCracker function.")
                    return
                combo = firstWord + secondWord + thirdWord
                shaAttempt = sha1(combo.encode("ascii"))
                attemptedHashPwd = shaAttempt.hexdigest()
                for index, pwd in enumerate(solutionTable):
                    if attemptedHashPwd == pwd[1]:
                        print(
                            "Password hash matched for User ID:"
                            + str(index + 1)
                            + " using "
                            + firstWord
                            + " "
                            + secondWord
                            + " "
                            + thirdWord
                        )
                        # Put password into table.
                        solutionTable[index][2] = combo
    print("Finished tripleStrCracker function.")


def exportSolutionTable():
    print(solutionTable)
    f = open("solutionTable.txt", "w")
    for item in solutionTable:
        f.write(" ".join(item) + "\n")
    f.close


# Process Flow
# Ask user who they are (file paths)
# Read in text files (dictionary.txt and passwords.txt)
# Initialized Hacked Password Solution Table
# Attempt singleStrCracker
# After running a type of cracking, status update -- remove found passwords
# (inside of function) and actively report progress
# Attempt the numCracker()
# Report Progress
# Repeat with strNum, doubleStr, doubleStrNum, tripleStr, tripleStrNum,
# Report progress each time
# Exit when all passwords have been cracked


# Shape of Solution Table
# UserID Hashed-Password PlainText-Password

fileLoader()
try:

    startTime = time.perf_counter()
    singleStrCracker()
    exportSolutionTable()
    endTime = time.perf_counter()
    print("Password Cracker took: " + str(endTime - startTime) + " seconds!")
    print("Passwords Remaining: " + str(getRemainingPasswords()))

    startTime = time.perf_counter()
    doubleStrCracker()
    exportSolutionTable()
    endTime = time.perf_counter()
    print("Password Cracker took: " + str(endTime - startTime) + " seconds!")
    print("Passwords Remaining: " + str(getRemainingPasswords()))

    startTime = time.perf_counter()
    strNumCracker()
    exportSolutionTable()
    endTime = time.perf_counter()
    print("Password Cracker took: " + str(endTime - startTime) + " seconds!")
    print("Passwords Remaining: " + str(getRemainingPasswords()))

    startTime = time.perf_counter()
    numCracker()
    exportSolutionTable()
    endTime = time.perf_counter()
    print("Password Cracker took: " + str(endTime - startTime) + " seconds!")
    print("Passwords Remaining: " + str(getRemainingPasswords()))

    startTime = time.perf_counter()
    doubleStrNumCracker()
    exportSolutionTable()
    endTime = time.perf_counter()
    print("Password Cracker took: " + str(endTime - startTime) + " seconds!")

    startTime = time.perf_counter()
    tripleStrCracker()
    exportSolutionTable()
    endTime = time.perf_counter()
    print("Password Cracker took: " + str(endTime - startTime) + " seconds!")
    print("Passwords Remaining: " + str(getRemainingPasswords()))
except KeyboardInterrupt:
    print("\nHALT PASSWORD CRACKER")
    exportSolutionTable()
