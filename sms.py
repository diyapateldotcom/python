import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror

def send_sms(number,message):
    url = 'https://www.fast2sms.com/dev/bulkV2'
    params = {
        'authorization' : 'QRjbFuK2B7KXarWWgOpipNAtiAFrQ4uWo171Fko3SNOU1LeZZSLHYqN6kqAS',
        'sender_id' : 'TXTIND',
        'message' : message,
        'language' : 'english',

        'route' : 'p',
        'numbers' : number
    }

    response = requests.get(url, params=params)
    dic = response.json()                        #retuns dictionary
    print(dic)
    return dic.get('return')

def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0",END)
    r = send_sms(num,msg)
    if r:
        showinfo("Send Success","Successfully Sent")
    else:
        showerror("Error","Somthing went wrong..")

#Creating  GUI
root=Tk()
root.title("Message Sender")
root.geometry("400x550")
font=("Helvetica",22,"bold")

textNumber = Entry(root, font=font)  #give only one line
textNumber.pack(fill=X, pady=20)

textMsg = Text(root)
textMsg.pack(fill=X)

sendBtn = Button(root,text="SEND SMS", command=btn_click)
sendBtn.pack()

root.mainloop()