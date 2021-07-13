import requests
import tkinter as tk

def getNews():
    api_key="329bd053697746228e5ad0d494262032"
    url = "https://newsapi.org/v2/top-headlines?country=in&apikey="+api_key
    news = requests.get(url).json()
    articles = news["articles"]
    my_articles = []
    my_news = ""
    for article in articles:
        my_articles.append(article["title"])
    for i in range(10):
            my_news= my_news+str(i+1)+my_articles[i]+"\n"
            print(my_news)

canvas=tk.Tk()
canvas.geometry("500x250")
canvas.title("News App")
canvas.configure(background="White")

button=tk.Button(canvas,font =24,text ="Reload", bg = "Black", fg="White", command = getNews)
button.pack(pady = 20)
label=tk.label
label.pack(canvas,font =18,justify ="left")
label.pack(pady=20)


getNews()
canvas.mainloop()

