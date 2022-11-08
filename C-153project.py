from tkinter import*
import random
root= Tk()
root.title("Password Generater")
root.geometry("400x400")
root.configure(background= "violet")

input1= Entry(root)
label_input= Label(root)
label= Label(root)
array_3d= [[[1,2,3,4,5,6],["head","tail"],["a","b","c","d","e"," f","h","i"]]]
print(array_3d[0][2][3]) 


def new_password():
    random1= random.randint(0,5)
    random2= random.randint(0,1)
    random3= random.randint(0,7)
    letter1= str(array_3d[0][0][random1])
    letter2= str(array_3d[0][1][random2])
    letter3=str(array_3d[0][2][random3])
    label["text"]= "new password id "+letter1+letter2+letter3
    label_input["text"]= "guessed password is"+ str(input1.get())
btn= Button(root,text= "new password", command= new_password)
label_input.place(relx=0.5, rely=0.4, anchor= CENTER)
input1.place(relx=0.5, rely=0.3, anchor=CENTER)
btn.place(relx= 0.5,rely=0.5, anchor=CENTER)
label.place(relx=0.5, rely=0.6, anchor=CENTER)   
root.mainloop()      