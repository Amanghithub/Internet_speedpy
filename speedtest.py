from tkinter import *
import speedtest

root = Tk()

root.title("Speed Test")
root.geometry("500x300")
root.configure(background="#9376E0")

lbl_heading = Label(root,text="Internet Speed Test",font=("Segoe Print",20,"bold"),fg="pink",bg="#9376E0")
lbl_heading.place(relx=0.5,rely=0.1,anchor=CENTER)

lbl_download = Label(root,text="Download Speed",font=("Segoe Print",15),bg="#9376E0",fg="#F6FFA6")
lbl_download.place(relx=0.2,rely=0.3,anchor=CENTER)

lbl_upload = Label(root,text="Upload Speed",font=("Segoe Print",15),fg="blue",bg="#9376E0")
lbl_upload.place(relx=0.8,rely=0.3,anchor=CENTER)

lbl_downshow = Label(root,font=("Yu Gothic Light",12),fg="#F6FFA6",bg="#9376E0")
lbl_downshow.place(relx=0.2,rely=0.4,anchor=CENTER)

lbl_upshow = Label(root,font=("Yu Gothic Light",12),fg="blue",bg="#9376E0")
lbl_upshow.place(relx=0.8,rely=0.4,anchor=CENTER)

def check_speed():
    print("Checking Speed")
    sp = speedtest.Speedtest()
    download_speed = round(sp.download()/1000000,2)
    lbl_downshow["text"]=str(download_speed)+"Mbps"
    upload_speed = round(sp.upload()/1000000,2)
    lbl_upshow["text"]=str(upload_speed)+"Mbps"

btn = Button(root,text="Check Speed",command=check_speed)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()