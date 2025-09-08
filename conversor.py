import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Base Converter")
app.geometry("600x400")

entryTypeLabel = ctk.CTkLabel(app, text="Input base:")
entryTypeLabel.grid(row=0,column=0)

entryType = ""
entryOptions = ["binary","octal","decimal","hexadecimal"]
def entry_dropdown_change(choice):
    entryType = choice
    return

entryDropdown = ctk.CTkOptionMenu(
    master=app,
    values=entryOptions,
    command=entry_dropdown_change
)
entryDropdown.grid(row=1,column=0)

outputTypeLabel = ctk.CTkLabel(app, text="Output base:")
outputTypeLabel.grid(row=2,column=0)

outputType = ""
outputOptions = ["binary","octal","decimal","hexadecimal"]
def output_dropdown_change(choice):
    outputType = choice
    return

outputDropdown = ctk.CTkOptionMenu(
    master=app,
    values=outputOptions,
    command=output_dropdown_change
)
outputDropdown.grid(row=3,column=0,padx=5)

entryLabel = ctk.CTkLabel(app, text="Enter your number here:")
entryLabel.grid(row=0,column=1)

digitEntry = ctk.CTkEntry(app, placeholder_text="number", width=300)
digitEntry.grid(row=1,column=1)

outputLabel = ctk.CTkLabel(app, text="Output number:")
outputLabel.grid(row=2,column=1)

outputFrame = ctk.CTkFrame(app, height=50)
outputFrame.grid(row=3,column=1)

outputBox = ctk.CTkLabel(outputFrame, text="el pepe", width=300)
outputBox.pack()



#=====Tkinter Code=====#


def getDecimalPart(part, base):
    match base:
        case 2:
            result = ""
            while part > 0.1:
                part = part * 2
                if part > 1:
                    part = part - 1
                    result = result + "1"
                else:
                    result = result + "0"
            return result
        case 8:
            
            return
        case 10:
            result = 0
            for i in range(1,len(part) + 1):
                result = result + int(part[i-1])*pow(2,-i)
            return result
        case 16:
            convers = {
                "0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
                "A":10,"B":11,"C":12,"D":13,"E":14,"F":15
            }
            result = 0
            for i in range(1,len(part) + 1):
                result = result + convers[part[i-1]]*pow(16,-i)
            return result
    
    return "ñonga"

def toBinary(n, type):
    if type == "binary":
        for i in n:
            if i != "0" and i != "1" and i != ".":
                return "input is not binary"
        return n
    elif type == "octal":
        n = str(toDecimal(n,"octal"))
        return toBinary(n,"decimal")
    elif type == "decimal":
        #si es decimal y tiene parte decimal se ejecuta el if
        if "." in str(n):
            print("eldiablo")
            split = str(n).split(".") 
            partWhole = int(split[0])
            partDecimal = float("0." + split[1])
            resultWhole = ""
            resultDecimal = ""
            while partWhole > 0:
                if partWhole % 2 == 0:
                    resultWhole += "0"
                else:
                    resultWhole += "1"
                partWhole = partWhole // 2
            resultWhole = resultWhole[::-1]
            
            resultDecimal = getDecimalPart(partDecimal,2)
            result = resultWhole + "." + resultDecimal
            return result
        else:
            resultWhole = ""
            partWhole = int(n)
            while partWhole > 0:
                if partWhole % 2 == 0:
                    resultWhole += "0"
                else:
                    resultWhole += "1"
                partWhole = partWhole // 2
            result = resultWhole[::-1]
            return result
    elif type == "hexadecimal":
        n = toDecimal(n,"hexadecimal")
        return toBinary(n,"decimal")
    return

def toOctal(n, type):
    if type == "binary":
        n = str(toDecimal(n, "binary"))
        return toOctal(n, "decimal")
    elif type == "octal":
        return n
    elif type == "decimal":
        if "." in str(n):
            print("eldiablo")
            split = str(n).split(".") 
            partWhole = float(split[0])
            partDecimal = float("0." + split[1])
            resultWhole = ""
            resultDecimal = ""
            while partWhole > 0:
                if partWhole % 8 == 0:
                    resultWhole += "0"
                else:
                    aux = partWhole / 8
                    aux = aux - int(aux)
                    aux = int(aux * 8)
                    resultWhole += str(aux)
                partWhole = partWhole // 8
            resultWhole = resultWhole[::-1]

            #lo hago aquí noma que flojera hacer una funcion
            while partDecimal > 0.1:
                partDecimal = partDecimal * 8
                if partDecimal > 1:
                    resultDecimal += str(int(partDecimal))
                    partDecimal = partDecimal - int(partDecimal)
                else:
                    resultDecimal = resultDecimal + "0"

            
            result = resultWhole + "." + resultDecimal
            return result
        else:
            resultWhole = ""
            partWhole = float(n)
            while partWhole > 0:
                if partWhole % 8 == 0:
                    resultWhole += "0"
                else:
                    aux = partWhole / 8
                    aux = aux - int(aux)
                    aux = int(aux * 8)
                    resultWhole = resultWhole + str(aux)
                partWhole = partWhole // 8
            result = resultWhole[::-1]
            return result
    elif type == "hexadecimal":
        n = str(toDecimal(n,"hexadecimal"))
        return toOctal(n,"decimal")
    return

#Convierte de cualquier base a deicimal
def toDecimal(n, type):
    if type == "binary":
        for i in n:
            if i != "0" and i != "1" and i != ".":
                return "input is not binary"
        if "." in n:
            result = 0
            power = 0
            split = n.split(".")
            partWhole = split[0]
            partDecimal = split[1]
            partWhole = partWhole[::-1]
            for i in partWhole:
                result = result + int(i)*pow(2,power)
                power = power + 1

            result = result + getDecimalPart(partDecimal, 10)
            return result
        
        else:
            result = 0
            power = 0
            n = n[::-1]
            for i in n:
                result = result + int(i)*pow(2,power)
                power = power + 1
            return result
    elif type == "octal":
        if "." in n:
            result = 0
            power = 0
            split = n.split(".")
            partWhole = split[0]
            partDecimal = split[1]
            partWhole = partWhole[::-1]
            for i in partWhole:
                result = result + int(i)*pow(8,power)
                power = power + 1
            result = result + getDecimalPart(partDecimal, 8)
            return result
        else:
            result = 0
            power = 0
            n = n[::-1]
            for i in n:
                result = result + int(i)*pow(8,power)
                power = power + 1
            return result
    elif type == "decimal":
        return n
    elif type == "hexadecimal":

        convers = {
            "0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,
            "A":10,"B":11,"C":12,"D":13,"E":14,"F":15
        }
        
        if "." in n:
            result = 0
            power = 0
            split = n.split(".")
            partWhole = split[0]
            partDecimal = float( "0." + split[1])
            partWhole = partWhole[::-1]
            for i in partWhole:
                result = result + convers[i]*pow(16,power)
                power = power + 1
            result = result + getDecimalPart(partDecimal, 16)
            return result
        else:
            result = 0
            power = 0
            n = n[::-1]
            for i in n:
                result = result + convers[i]*pow(16,power)
                power = power + 1
            return result
    return 



#transformacion a hexadecimal
def toHexadecimal(n, type):
    if type == "binary":
        n = str(toDecimal(n, "binary"))
        return toHexadecimal(n, "decimal")
    elif type == "octal":
        n = str(toDecimal(n, "octal"))
        return toHexadecimal(n, "decimal")
    elif type == "decimal":

        invers = {
            "0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9",
            "10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"
        }

        if "." in str(n):
            print("eldiablo")
            split = str(n).split(".") 
            partWhole = float(split[0])
            partDecimal = float("0." + split[1])
            resultWhole = ""
            resultDecimal = ""
            while partWhole > 0:
                if partWhole % 16 == 0:
                    resultWhole += "0"
                else:
                    aux = partWhole / 16
                    aux = aux - int(aux)
                    aux = int(aux * 16)
                    resultWhole += invers[str(aux)]
                partWhole = partWhole // 16
            resultWhole = resultWhole[::-1]

            #lo hago aquí noma que flojera hacer una funcion
            while partDecimal > 0.1:
                partDecimal = partDecimal * 16
                if partDecimal > 1:
                    resultDecimal += invers[str(int(partDecimal))]
                    partDecimal = partDecimal - int(partDecimal)
                else:
                    resultDecimal = resultDecimal + "0"

            
            result = resultWhole + "." + resultDecimal
            return result
        else:
            resultWhole = ""
            partWhole = float(n)
            while partWhole > 0:
                if partWhole % 16 == 0:
                    resultWhole += "0"
                else:
                    aux = partWhole / 16
                    aux = aux - int(aux)
                    aux = int(aux * 16)
                    resultWhole = resultWhole + invers[str(aux)]
                partWhole = partWhole // 16
            result = resultWhole[::-1]
            return result
    elif type == "hexadecimal":
        return n
    return

def showOut(output):
    outputBox.configure(text=output)
    return

def run():
    entryType = entryDropdown.get()
    outputType = outputDropdown.get()
    n = digitEntry.get()
    result=""
    match outputType:
        case "binary":
            result = toBinary(n,entryType)
            showOut(result)
            return
        case "octal":
            result = toOctal(n,entryType)
            showOut(result)
            return
        case "decimal":
            result = toDecimal(n,entryType)
            showOut(result)
            return
        case "hexadecimal":
            result = toHexadecimal(n,entryType)
            showOut(result)
            return
        case _:
            return
    return


runButton = ctk.CTkButton(
    master=app, text="Calculate",
    command=run)
runButton.grid(row=1,column=2,padx=5)

        
app.mainloop()