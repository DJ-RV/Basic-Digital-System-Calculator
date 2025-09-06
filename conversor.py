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

outputBox = ctk.CTkLabel(outputFrame, text="el pepe" )
outputBox.pack()



#=====Tkinter Code=====#


def getDecimalPart(part, base):
    result = ""
    match base:
        case 2:
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
            for each in 
            return
        case 16:
            
            return
    
    return "ñonga"

def toBinary(n, type):
    if type == "binary":
        for i in n:
            if i != "0" and i != "1" and i != ".":
                return "input is not binary"
        return n
    elif type == "octal":
        return
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
            partWhole = n
            while partWhole > 0:
                if partWhole % 2 == 0:
                    resultWhole += "0"
                else:
                    resultWhole += "1"
                partWhole = partWhole // 2
            result = resultWhole[::-1]
            return result
    elif type == "hexadecimal":
        return
    return

def toOctal(n, type):
    
    return

def toDecimal(n, type):
    if type == "binary":
        result = ""
        if "." in n:
            result = 0
            power = 0
            split = n.split(".")
            partWhole = split[0]
            partDecimal = split[1]
            partWhole = partWhole[::-1]
            for i in partWhole:
                result = result + int(i)*pow(2,power)
            result = result + getDecimalPart(partDecimal, 10)
            
        return result
        result = 0
        power = 0
        n = n[::-1]
        for i in n:
            result = result + int(i)*pow(2,power)
    return

def toHexadecimal(n, type):
    
    return

def showOut(output):
    outputBox.configure(text=output)
    return

def run():
    entryType = entryDropdown.get()
    outputType = outputDropdown.get()
    n = digitEntry.get()
    result=""
    print("haps")
    match outputType:
        case "binary":
            print("haps")
            result = toBinary(n,entryType)
            showOut(result)
            return
        case "octal":
            return
        case "decimal":
            return
        case "hexadecimal":
            return
        case _:
            return
    return


runButton = ctk.CTkButton(
    master=app, text="Calculate",
    command=run)
runButton.grid(row=1,column=2,padx=5)

        
app.mainloop()