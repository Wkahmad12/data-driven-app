import requests
from tkinter import Entry, Button, Frame, Scrollbar, Text, Label, messagebox
from PIL import Image, ImageTk
import PIL
print("Pillow version:", PIL.__version__)
import tkinter as tk
from tkinter import Listbox, OptionMenu, StringVar

def switch_frame(frame):
    frame.tkraise()

def page_one():
    switch_frame(frame1)

def click_this():
    messagebox.showinfo("ABOUT", "Using Tkinter, the included Python code builds a basic movie recommendation application with a graphical user interface. The program lets users search for movies, shows a list of results in an easy-to-use interface, and provides comprehensive facts on the movies they've chosen, such as cast bios, synopses, titles, and release dates. By retrieving real-time movie data, the integration with The Movie Database (TMDb) API improves the usefulness of the application. Navigating the application, seeing movie details, and enjoying a visual depiction of movie posters are all available to users. The code creates an interactive and aesthetically pleasing movie recommendation experience by fusing API interactions with Tkinter's GUI features.")

movie = []
api_key = "6e065691f23ab4af3809eff24561360f"
#send request to tmbd api
def movie_search(api_key, query):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': api_key,
        'query': query
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data.get('results', [])
#get data from api
def Get_details(api_key, movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data
#trigger when user serch for movie
def On_search():
    global movies
    query = Sbar_input.get()
    if query:
        movies = movie_search(api_key, query)
        display_results(movies)

def Select_movie(event):
    global movies
    selected_index = flim_list.curselection()
    if selected_index:
        selected_movie = movies[selected_index[0]]
        movie_details(selected_movie)
        movie_image(selected_movie)
#display movie image which are selected
def movie_image(movie):
    image_url = movie.get('poster_path')  #poster path
    if image_url:
        image_url = f"https://image.tmdb.org/t/p/w500/{image_url}"
        image = Image.open(requests.get(image_url, stream=True).raw)
        image = image.resize((200, 300), resample=Image.BICUBIC)



        image = ImageTk.PhotoImage(image)
        picure_label.config(image=image)
        picure_label.image = image
    else:
        
        pass
#display detail of movie
def movie_details(movie):
    info.config(state=tk.NORMAL)
    info.delete(1.0, tk.END)

    TITLE = movie.get('title', 'N/A')
    Overview = movie.get('overview', 'No overview available.')
    id_movie= movie.get('id')
    release = movie.get('release_date', 'N/A')

    info.insert(tk.END, f"\nTitle: {TITLE}\nRelease Date: {release}\nOverview: {Overview}\n")

    movie_details = Get_details(api_key, id_movie)
    characters = movie_details.get('credits', {}).get('cast', [])
    if characters:
        info.insert(tk.END, "\nCharacters:\n")
        for character in characters:
            character_name = character.get('name', 'N/A')
            info.insert(tk.END, f" - {character_name}\n")

    info.config(state=tk.DISABLED)
#for reult on frame
def display_results(movies):
    flim_list.delete(0, tk.END)

    for movie in movies:
        title = movie.get('title', 'N/A')
        flim_list.insert(tk.END, title)



# main frame
king = tk.Tk()
king.title("Movie recommendation")
king.geometry("600x500")
#frame 1 
frame = Frame(king)
#background image
pic_frame = ImageTk.PhotoImage(Image.open("R (2).jpeg"))
pic_label = Label(frame, image=pic_frame)
pic_label.place(x=0, y=0, width=600, height=500)
#button of start
but1 = Button(frame, text="Start", command=page_one, border=5)
but1.place(x=220, y=350, width=170)
#button of about
but2 = Button(frame, text="ABOUT", command=click_this, border=5, bg="red")
but2.place(x=220, y=410, width=170)
#end of frame
frame.place(x=0, y=0, width=600, height=500)
#frame 2
frame1 = Frame(king)
#background image frame 2
tasweeer_frame = ImageTk.PhotoImage(Image.open("R (1).jpeg"))
tasweer_label = Label(frame1, image=tasweeer_frame)
tasweer_label.place(x=0, y=0, width=600, height=500)
#title
tt = Label(frame1, text="MOVIE BOX", font=('Arial', 30, 'bold'), bg="black", fg="red")
tt.place(x=0, y=0, width=600, height=60)# place use for allignment
#search bar 
Sbar_input = Entry(frame1, font=('Arial', 12), bd=5)
Sbar_input.place(x=200, y=70, width=200)
#serch button
btn = Button(frame1, text="Search", command=On_search, bd=5,bg="lightgrey",fg="white")
btn.place(x=420, y=70, width=70)


#listbox for movie list
flim_list = Listbox(frame1, font=('Arial', 12), bd=5,bg="black",fg="white")
flim_list.place(x=10, y=100, width=180, height=380)
flim_list.bind("<<ListboxSelect>>", Select_movie)
#frame for detail of movie
info_framee = Frame(frame1, bd=5, bg="black")
info_framee.place(x=200, y=110, width=400, height=200)
#wrap is used to breakdown text
info = Text(info_framee, wrap="word", font=('Arial', 12), bd=5, bg="black", fg="white")
info.pack(side="left", fill="both", expand=True)
#scroll bar
scroll = Scrollbar(info_framee, command=info.yview)
scroll.pack(side="right", fill="y")

info.config(yscrollcommand=scroll.set)
#fetched image frame
imgg_frame = Frame(frame1, bd=5, bg="black")
imgg_frame.place(x=200, y=320, width=400, height=170)

picure_label = Label(imgg_frame,bg="black" ,bd=5)
picure_label.pack(side="left", fill="both", expand=True)

#end of frame 2
frame1.place(x=0, y=0, width=600, height=500)

#switch frame from 1 to 2
switch_frame(frame)

king.mainloop()
