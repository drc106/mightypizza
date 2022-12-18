

"""
    Class Name:     VaidInput
    Writen by:      D Cravens
    Version:        1.0
    Date created:   11-19-2022
    Revised date:   12-18-2022
    Description :   This class is responsible for collecting and verifying user input for the Mighty Pizza app.

"""

class VaidInput:
    # check_input takes an argument name usrInput
    # and checks if the usrInput is a string, interger, or a float
    # returns "str" for string, "ini" for integer, or "float" for float 
    def check_input(this, usrInput):
        try:
            # Convert it into integer
            int(usrInput)
            # is a ini return ini
            return "ini"
        except ValueError:
            try:
                # Convert it into float
                float(usrInput)
                # is a float return float
                return "float"
            except ValueError:
                # is a string return str
                return "str"

    # check_user_input Checks user input, arguments: dType, usrInput
    # Checks to see if user input is a string, interger, or a float and returns True or False
    # Argument dType is a string only can be "str" for string, "ini" for integer, or "float" for float
    # Argument usrInput takes the user input data
    def check_user_input(this, dType: str, usrInput):
        # Check to see if dType or usrInput is empty
        if dType == "" or usrInput == "":
            # dType and/or usrInput is empty raise an Exception
            raise Exception("dType or usrInput cannot be empty")
        else:
            # Check to see if dType is str, ini, or float
            if dType == "str" or dType == "ini" or dType == "float":
                # 
                if this.check_input(usrInput) == dType:
                    return True
                else:
                     return False
            else:
                raise Exception("dType has to be set to str, ini, or float")          
def main():
    try:
        app = VaidInput()
        if app.check_user_input("ini3", "jjj"):
            print("yes")
        else:
            print("no")
    except Exception as e:
        print(e)
    
if __name__ == '__main__':
    main()