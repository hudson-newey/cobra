def main():
    message: string = ""
    MYMESSAGE: string = "this is a test"
    myPrint(MYMESSAGE + message)
    print("high")
fn myPrint(text: str):
    print(text)
# this should trigger a warning
myVariable1: string = "foo"
my_variable2: string = "bar"
main()
