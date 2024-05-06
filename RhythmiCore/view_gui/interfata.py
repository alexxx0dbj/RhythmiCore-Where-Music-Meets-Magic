global tree_biblioteca, tree_melodie_rating

import hashlib
def open_biblioteca_utilizator():
    # Function definition goes here in future
    pass

import tkinter as tk
from tkinter import messagebox, ttk
import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\Programe_facultate\instantclient_21_12")


# Database connection parameters
connStr = 'bd033/bd033@bd-dc.cs.tuiasi.ro:1539/orcl'


# Function to connect to the Oracle database
def create_connection():
    return cx_Oracle.connect(connStr)

# Function to verify login credentials
def login(email, password):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM utilizator WHERE email = '{email}' AND parola = '{password}'")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            open_biblioteca_utilizator()
        return result
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
    return None

# Function to register a new user
def register(name, email, password):
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO utilizator (nume, email, parola) VALUES ('{name}', '{email}', '{password}')")
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", "User registered successfully.")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# Function to switch to the sign-up frame
def show_signup_frame():
    login_frame.pack


    login_frame.pack_forget()
    signup_frame.pack()

# Function to switch to the login frame
def show_login_frame():
    signup_frame.pack_forget()
    login_frame.pack()

# GUI for the Login Page
def create_login_frame(container):
    login_frame = tk.Frame(container)

    # fonts for labels and entries
    label_font = ('Arial', 12)
    entry_font = ('Arial', 12)

    # Email Label and Entry
    tk.Label(login_frame, text="Email:", font=label_font).grid(row=0, column=0, padx=10, pady=10)
    email_entry = tk.Entry(login_frame, font=entry_font)
    email_entry.grid(row=0, column=1, padx=10, pady=10)

    # Password Label and Entry
    tk.Label(login_frame, text="Password:", font=label_font).grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(login_frame, show="*", font=entry_font)
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # Login Button
    login_button = tk.Button(login_frame, text="Login", font=('Arial', 10), command=lambda: perform_login(email_entry.get(), password_entry.get()))
    login_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Sign Up Button
    signup_button = tk.Button(login_frame, text="Sign Up", font=('Arial', 10), command=show_signup_frame)
    signup_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Centering the frame in the container
    login_frame.pack(padx=20, pady=20)

    return login_frame

import tkinter as tk

def create_signup_frame(container):
    frame = tk.Frame(container)
    entry_width = 40

    tk.Label(frame, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(frame,width=entry_width)
    name_entry.grid(row=0, column=1)

    tk.Label(frame, text="Email:").grid(row=1, column=0)
    email_entry = tk.Entry(frame,width=entry_width)
    email_entry.grid(row=1, column=1)

    tk.Label(frame, text="Password:").grid(row=2, column=0)
    password_entry = tk.Entry(frame, show="*",width=entry_width)
    password_entry.grid(row=2, column=1)

    tk.Label(frame, text="Confirm Password:").grid(row=3, column=0)
    confirm_password_entry = tk.Entry(frame, show="*", width=entry_width)
    confirm_password_entry.grid(row=3, column=1)

    register_button = tk.Button(frame, text="Register",
    command=lambda: perform_registration(name_entry.get(), email_entry.get(),
    password_entry.get(), confirm_password_entry.get()))
    register_button.grid(row=4, column=1)

    login_button = tk.Button(frame, text="Login", command=show_login_frame)
    login_button.grid(row=5, column=1)

    return frame



# Function to perform the login action
def perform_login(email, password):
    user = login(email, password)
    if user:
        if email.lower().startswith('admin@'):            
            open_admin_window()  # Open admin window for admin users
        else:
            messagebox.showinfo("Success", "You are now logged in.")
            user_id = user[0]
            open_biblioteca_utilizator_window(user_id)  # Open regular user window
    else:
        messagebox.showerror("Failed", "Login failed. User not found.\nPlease check your credentials.")


# Function to perform the registration action
def perform_registration(name, email, password, confirm_password):
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
    else:
        try:
            # Attempt to register the user in the database
            register(name, email, password)
        except Exception as e:
            messagebox.showerror("Database Error", str(e))







# -------------ADMIN WINDOW ----------------------------
def open_admin_window():
    admin_window = tk.Toplevel()
    admin_window.title("Admin Dashboard")

    # Define the columns for the Treeview
    columns = ('ID', 'Email', 'Password (Hashed)', 'Song Count')
    tree_users = ttk.Treeview(admin_window, columns=columns, show='headings')
    
    # Define the column headings
    for col in columns:
        tree_users.heading(col, text=col)

    # Adjust the column widths (optional)
    tree_users.column('ID', width=100)
    tree_users.column('Email', width=200)
    tree_users.column('Password (Hashed)', width=300)
    tree_users.column('Song Count', width=150)

    tree_users.pack(fill='both', expand=True)

    # Function to update the Treeview with user data
    def update_tree():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            query = """
            SELECT u.id_utilizator, u.email, u.parola, COUNT(bu.id_melodie)
            FROM utilizator u
            LEFT JOIN bilbiotecautilizator bu ON u.id_utilizator = bu.id_utilizator
            WHERE LOWER(u.email) NOT LIKE 'admin@%'
            GROUP BY u.id_utilizator, u.email, u.parola
            ORDER BY u.id_utilizator
        """

            cursor.execute(query)
            users = cursor.fetchall()

            # Clear existing data in the Treeview
            tree_users.delete(*tree_users.get_children())

            # Inserting new data
            for user in users:
                hashed_password = hashlib.sha256(user[2].encode()).hexdigest()  # Hashing the password
                tree_users.insert("", tk.END, values=(user[0], user[1], hashed_password, user[3]))

            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
    def delete_inactive_users():
        response = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete all users without registrations and not admin?")
        if response:
            try:
                conn = create_connection()
                cursor = conn.cursor()

                # SQL query to delete users
                delete_query = """
                    DELETE FROM utilizator
                    WHERE id_utilizator NOT IN (SELECT id_utilizator FROM bilbiotecautilizator)
                    AND LOWER(email) NOT LIKE '%admin@%'
                """
                cursor.execute(delete_query)
                conn.commit()

                messagebox.showinfo("Success", "Inactive users deleted successfully.")

                cursor.close()
                conn.close()
            except Exception as e:
                messagebox.showerror("Database Error", str(e))

    # New Treeview for admin users
    admin_columns = ('ID', 'Name', 'Email', 'Password (Hashed)')
    tree_admin_users = ttk.Treeview(admin_window, columns=admin_columns, show='headings')

    for col in admin_columns:
        tree_admin_users.heading(col, text=col)
        tree_admin_users.column(col, width=120)

    tree_admin_users.pack(fill='both', expand=True)

    # Function to update the Treeview with admin user data
    def update_tree_admin_users():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            query = """
            SELECT id_utilizator, nume, email, parola
            FROM utilizator
            WHERE LOWER(email) LIKE 'admin@%'
            """
            cursor.execute(query)
            admin_users = cursor.fetchall()
            # Clear existing data in the Treeview
            tree_admin_users.delete(*tree_admin_users.get_children())

            # Inserting new data
            for user in admin_users:
                hashed_password = hashlib.sha256(user[3].encode()).hexdigest()  # Hashing the password
                tree_admin_users.insert("", tk.END, values=(user[0], user[1], user[2], hashed_password))

            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))


    # Button to fetch and display user data
    fetch_button = tk.Button(admin_window, text="Refresh User Data", command=update_tree)
    fetch_button.pack()

    # Button to delete inactive users
    delete_button = tk.Button(admin_window, text="Delete Inactive Users", command=delete_inactive_users)
    delete_button.pack()

    # Button to fetch and display admin user data
    fetch_admin_users_button = tk.Button(admin_window, text="Show Admin Users", command=update_tree_admin_users)
    fetch_admin_users_button.pack()

    # Button to open the music information window
    music_info_button = tk.Button(admin_window, text="Open Music Info", command=open_music_info_window)
    music_info_button.pack()

    # Initial call to populate the data
    update_tree()




# -----------------SONGS ALBUMS ARTISTS ETC. WINDOW----------------
def open_music_info_window():
    music_info_window = tk.Toplevel()
    music_info_window.title("Music Information")

    # Top section frame to hold Album, Artist, Melodie, and Genuri Muzicale
    top_section_frame = tk.Frame(music_info_window)
    top_section_frame.pack(fill="both", expand=True)

    # ---------------------------SONGS---------------------------------------------------------

    songs_section = tk.LabelFrame(top_section_frame, text="Songs")
    songs_section.pack(side="left", fill="both", expand="yes", padx=10, pady=10)
    # Define the columns for the Treeview
    columns = ('ID', 'Song Name') 
    tree_songs = ttk.Treeview(songs_section, columns=columns, show='headings')

    # Define the column headings
    for col in columns:
        tree_songs.heading(col, text=col)
        tree_songs.column(col, width=160)  

    tree_songs.pack(fill='both', expand=True)

    # Function to update the Treeview with song data
    def update_tree_songs():
        try:
            conn = create_connection()
            cursor = conn.cursor()

            # Query to fetch songs data
            query = "SELECT id_melodie, nume FROM melodie ORDER BY id_melodie ASC"

            cursor.execute(query)
            songs = cursor.fetchall()

            # Clear existing data in the Treeview
            tree_songs.delete(*tree_songs.get_children())

            # Inserting new data
            for song in songs:
                tree_songs.insert("", tk.END, values=song)

            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    # Initial call to populate the data
    update_tree_songs()

    # Function to insert a new song
    def insert_song():
        insert_window = tk.Toplevel()
        insert_window.title("Insert New Song")

        tk.Label(insert_window, text="Song Name:").grid(row=0, column=0)
        song_name_entry = tk.Entry(insert_window)
        song_name_entry.grid(row=0, column=1)

        def save_new_song():
            song_name = song_name_entry.get()
            try:
                conn = create_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO melodie (nume) VALUES (:name)", {"name": song_name})
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Success", "New song added successfully.")
                insert_window.destroy()
                update_tree_songs()

            except Exception as e:
                messagebox.showerror("Database Error", str(e))

        save_button = tk.Button(insert_window, text="Save", command=save_new_song)
        save_button.grid(row=1, column=1)

    # Function to edit an existing song name
    def edit_song():
        edit_window = tk.Toplevel()
        edit_window.title("Edit Song Name")

        tk.Label(edit_window, text="Song ID:").grid(row=0, column=0)
        song_id_entry = tk.Entry(edit_window)
        song_id_entry.grid(row=0, column=1)

        tk.Label(edit_window, text="New Song Name:").grid(row=1, column=0)
        new_song_name_entry = tk.Entry(edit_window)
        new_song_name_entry.grid(row=1, column=1)

        def update_song_name():
            song_id = song_id_entry.get()
            new_song_name = new_song_name_entry.get()
            try:
                conn = create_connection()
                cursor = conn.cursor()
                cursor.execute("UPDATE melodie SET nume = :name WHERE id_melodie = :id", {"name": new_song_name, "id": song_id})
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Success", "Song name updated successfully.")
                edit_window.destroy()
                update_tree_songs()  # Refresh the artist list

            except Exception as e:
                messagebox.showerror("Database Error", str(e))

        update_button = tk.Button(edit_window, text="Update", command=update_song_name)
        update_button.grid(row=2, column=1)

    insert_button = tk.Button(songs_section, text="Insert New Song", command=insert_song)
    insert_button.pack(side='left', padx=5, pady=5)

    # Button to edit an existing song
    edit_button = tk.Button(songs_section, text="Edit Song Name", command=edit_song)
    edit_button.pack(side='left', padx=5, pady=5)

    # Button to fetch and display song data
    refresh_button = tk.Button(songs_section, text="Refresh Songs", command=update_tree_songs)
    refresh_button.pack(side='left', padx=5, pady=5)




    #-------------------------------ARTISTS------------------------------------------

    artist_section = tk.LabelFrame(top_section_frame, text="Artists")
    artist_section.pack(side="left", fill="both", expand="yes", padx=10, pady=10)

    # Artist Treeview
    artist_columns = ('ID', 'Artist Name')
    tree_artists = ttk.Treeview(artist_section, columns=artist_columns, show='headings')

    for col in artist_columns:
        tree_artists.heading(col, text=col)
        tree_artists.column(col, width=120)

    tree_artists.pack(fill='both', expand=True)

    # Update the Treeview with artist data
    def update_tree_artists():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            query = "SELECT id_artist, nume FROM artist ORDER BY id_artist ASC"
            cursor.execute(query)
            artists = cursor.fetchall()
            tree_artists.delete(*tree_artists.get_children())
            for artist in artists:
                tree_artists.insert("", tk.END, values=artist)
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def add_artist():
        add_window = tk.Toplevel()
        add_window.title("Add New Artist")

        tk.Label(add_window, text="Artist Name:").grid(row=0, column=0)
        artist_name_entry = tk.Entry(add_window)
        artist_name_entry.grid(row=0, column=1)

        def save_artist():
            artist_name = artist_name_entry.get()
            try:
                conn = create_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO artist (nume) VALUES (:name)", {"name": artist_name})
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Success", "Artist added successfully.")
                add_window.destroy()
                update_tree_artists()  # Refresh the artist list
            except Exception as e:
                messagebox.showerror("Database Error", str(e))

        save_button = tk.Button(add_window, text="Save", command=save_artist)
        save_button.grid(row=1, column=1)
        
    def edit_artist():
        edit_window = tk.Toplevel()
        edit_window.title("Edit Artist Name")

        tk.Label(edit_window, text="Artist ID:").grid(row=0, column=0)
        artist_id_entry = tk.Entry(edit_window)
        artist_id_entry.grid(row=0, column=1)

        tk.Label(edit_window, text="New Artist Name:").grid(row=1, column=0)
        new_artist_name_entry = tk.Entry(edit_window)
        new_artist_name_entry.grid(row=1, column=1)

        def update_artist_name():
            artist_id = artist_id_entry.get()
            new_artist_name = new_artist_name_entry.get()
            try:
                conn = create_connection()
                cursor = conn.cursor()
                cursor.execute("UPDATE artist SET nume = :name WHERE id_artist = :id", {"name": new_artist_name, "id": artist_id})
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Success", "Artist name updated successfully.")
                edit_window.destroy()
                update_tree_artists()  # Refresh the artist list
            except Exception as e:
                messagebox.showerror("Database Error", str(e))
        update_button = tk.Button(edit_window, text="Update", command=update_artist_name)
        update_button.grid(row=2, column=1)

    # Add, Edit, and Refresh buttons for artists
    add_artist_button = tk.Button(artist_section, text="Add Artist", command=add_artist)
    add_artist_button.pack(side='left', padx=5, pady=5)

    edit_artist_button = tk.Button(artist_section, text="Edit Artist", command=edit_artist)
    edit_artist_button.pack(side='left', padx=5, pady=5)

    refresh_artist_button = tk.Button(artist_section, text="Refresh Artists", command=update_tree_artists)
    refresh_artist_button.pack(side='left', padx=5, pady=5)

    
    # Initial call to populate artist data
    update_tree_artists()


    #-------------------------------ALBUMS------------------------------------------
    # ----- Album Section -----
    album_section = tk.LabelFrame(top_section_frame, text="Albums")
    album_section.pack(side="left", fill="both", expand=True, padx=10, pady=5)

    # Album Treeview
    album_columns = ('ID', 'Album Name')
    tree_albums = ttk.Treeview(album_section, columns=album_columns, show='headings')
    for col in album_columns:
        tree_albums.heading(col, text=col)
        tree_albums.column(col, width=120)
    tree_albums.pack(fill='both', expand=True)

    def update_tree_albums():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            query = "SELECT id_album, nume FROM album ORDER BY id_album ASC"
            cursor.execute(query)
            albums = cursor.fetchall()
            tree_albums.delete(*tree_albums.get_children())
            for album in albums:
                tree_albums.insert("", tk.END, values=album)
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))


    # Initial call to populate the data
    update_tree_albums()

    def add_album():
        add_window = tk.Toplevel()
        add_window.title("Add New Album")

        tk.Label(add_window, text="Album Name:").grid(row=0, column=0)
        album_name_entry = tk.Entry(add_window)
        album_name_entry.grid(row=0, column=1)

        def save_new_album():
            album_name = album_name_entry.get()
            # Here, you should add your database logic to insert a new album
            try:
                conn = create_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO album (nume) VALUES (:name)", {"name": album_name})
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Success", "New album added successfully.")
                add_window.destroy()
                update_tree_albums()  # Refresh the album list
            except Exception as e:
                messagebox.showerror("Database Error", str(e))

        save_button = tk.Button(add_window, text="Save", command=save_new_album)
        save_button.grid(row=1, column=1)

    def edit_album():
        edit_window = tk.Toplevel()
        edit_window.title("Edit Album")

        tk.Label(edit_window, text="Album ID:").grid(row=0, column=0)
        album_id_entry = tk.Entry(edit_window)
        album_id_entry.grid(row=0, column=1)

        tk.Label(edit_window, text="New Album Name:").grid(row=1, column=0)
        new_album_name_entry = tk.Entry(edit_window)
        new_album_name_entry.grid(row=1, column=1)

        def update_album():
            album_id = album_id_entry.get()
            new_album_name = new_album_name_entry.get()
            # Here, add your database logic to update the album
            try:
                conn = create_connection()
                cursor = conn.cursor()
                cursor.execute("UPDATE album SET nume = :name WHERE id_album = :id", {"name": new_album_name, "id": album_id})
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Success", "Album updated successfully.")
                edit_window.destroy()
                update_tree_albums()  # Refresh the album list
            except Exception as e:
                messagebox.showerror("Database Error", str(e))

        update_button = tk.Button(edit_window, text="Update", command=update_album)
        update_button.grid(row=2, column=1)


    # Buttons for Album
    add_album_button = tk.Button(album_section, text="Add Album", command=add_album)
    add_album_button.pack(side='left', padx=5, pady=5)

    edit_album_button = tk.Button(album_section, text="Edit Album", command=edit_album)
    edit_album_button.pack(side='left', padx=5, pady=5)

    refresh_album_button = tk.Button(album_section, text="Refresh Albums", command=update_tree_albums)
    refresh_album_button.pack(side='left', padx=5, pady=5)




    #-------------------------------GENRES------------------------------------------
    genre_section = tk.LabelFrame(top_section_frame, text="Music Genres")
    genre_section.pack(side="right", fill="both", expand=True, padx=10, pady=5)

    # Genre Treeview
    genre_columns = ('ID', 'Genre Name')
    tree_genres = ttk.Treeview(genre_section, columns=genre_columns, show='headings')
    for col in genre_columns:
        tree_genres.heading(col, text=col)
        tree_genres.column(col, width=120)
    tree_genres.pack(fill='both', expand=True)

    def update_tree_genres():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            query = "SELECT id_gen_muzical, nume FROM genmuzical ORDER BY id_gen_muzical ASC"
            cursor.execute(query)
            genres = cursor.fetchall()
            tree_genres.delete(*tree_genres.get_children())
            for genre in genres:
                tree_genres.insert("", tk.END, values=genre)
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    # Initial call to populate the genre data
    update_tree_genres()

    def add_genre():
        add_window = tk.Toplevel()
        add_window.title("Add New Genre")

        tk.Label(add_window, text="Genre Name:").grid(row=0, column=0)
        genre_name_entry = tk.Entry(add_window)
        genre_name_entry.grid(row=0, column=1)

        def save_new_genre():
            genre_name = genre_name_entry.get()
            try:
                conn = create_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO genmuzical (nume) VALUES (:name)", {"name": genre_name})
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Success", "New genre added successfully.")
                add_window.destroy()
                update_tree_genres()  # Refresh the genre list
            except Exception as e:
                messagebox.showerror("Database Error", str(e))

        save_button = tk.Button(add_window, text="Save", command=save_new_genre)
        save_button.grid(row=1, column=1)

    def edit_genre():
        edit_window = tk.Toplevel()
        edit_window.title("Edit Genre")

        tk.Label(edit_window, text="Genre ID:").grid(row=0, column=0)
        genre_id_entry = tk.Entry(edit_window)
        genre_id_entry.grid(row=0, column=1)

        tk.Label(edit_window, text="New Genre Name:").grid(row=1, column=0)
        new_genre_name_entry = tk.Entry(edit_window)
        new_genre_name_entry.grid(row=1, column=1)

        def update_genre():
            genre_id = genre_id_entry.get()
            new_genre_name = new_genre_name_entry.get()
            try:
                conn = create_connection()
                cursor = conn.cursor()
                cursor.execute("UPDATE genmuzical SET nume = :name WHERE id_gen_muzical = :id", {"name": new_genre_name, "id": genre_id})
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Success", "Genre updated successfully.")
                edit_window.destroy()
                update_tree_genres()  # Refresh the genre list
            except Exception as e:
                messagebox.showerror("Database Error", str(e))

        update_button = tk.Button(edit_window, text="Update", command=update_genre)
        update_button.grid(row=2, column=1)


    # Add, Edit, and Refresh buttons for genres
    add_genre_button = tk.Button(genre_section, text="Add Genre", command=add_genre)
    add_genre_button.pack(side='left', padx=5, pady=5)

    edit_genre_button = tk.Button(genre_section, text="Edit Genre", command=edit_genre)
    edit_genre_button.pack(side='left', padx=5, pady=5)

    refresh_genre_button = tk.Button(genre_section, text="Refresh Genres", command=update_tree_genres)
    refresh_genre_button.pack(side='left', padx=5, pady=5)



    # ---------------------------DETALII MELODIE (Song Details) -----------------------------
    details_section = tk.LabelFrame(music_info_window, text="Detalii Melodie")
    details_section.pack(fill="both", expand=True, padx=10, pady=10)

    # Define the columns for the Treeview
    detail_columns = ('Song ID', 'Song Name','Artist Name', 'Album Name', 'Other Details')
    tree_details = ttk.Treeview(details_section, columns=detail_columns, show='headings')

    # Define the column headings
    for col in detail_columns:
        tree_details.heading(col, text=col)
        tree_details.column(col, width=120)  

    tree_details.pack(fill='both', expand=True)

    # Function to update the Treeview with song details
    def update_tree_details():
        try:
            conn = create_connection()
            cursor = conn.cursor()

            # Adjust this query to fetch the relevant song details
            query = """
            SELECT m.id_melodie, m.nume, a.nume, al.nume, dm.detalii
            FROM detaliimelodie dm
            JOIN melodie m ON dm.id_melodie = m.id_melodie
            JOIN artist a ON dm.id_artist = a.id_artist
            JOIN album al ON dm.id_album = al.id_album
            ORDER BY m.id_melodie
            """
            cursor.execute(query)
            details = cursor.fetchall()

            # Clear existing data in the Treeview
            tree_details.delete(*tree_details.get_children())

            # Inserting new data
            for detail in details:
                tree_details.insert("", tk.END, values=detail)

            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    # Initial call to populate the data
    update_tree_details()

    # Add Refresh Button for Detalii Melodie
    refresh_details_button = tk.Button(details_section, text="Refresh Details", command=update_tree_details)
    refresh_details_button.pack(side='left', padx=5, pady=5)

    # Add Button for Detalii Melodie
    add_details_button = tk.Button(details_section, text="Add New", command=open_add_detail_window)
    add_details_button.pack(side='left', padx=5, pady=5)

    
    
    
    
    
    # ---------------------------DETALII GENURI (Genre Details) -----------------------------
    genre_details_section = tk.LabelFrame(music_info_window, text="Detalii Genuri")
    genre_details_section.pack(fill="both", expand=True, padx=10, pady=10)

    # Define the columns for the Treeview
    genre_detail_columns = ('Song ID', 'Song Name', 'Genre Name')
    tree_genre_details = ttk.Treeview(genre_details_section, columns=genre_detail_columns, show='headings')

    # Define the column headings
    for col in genre_detail_columns:
        tree_genre_details.heading(col, text=col)
        tree_genre_details.column(col, width=120)

    tree_genre_details.pack(fill='both', expand=True)

    # Function to update the Treeview with genre details
    def update_tree_genre_details():
        try:
            conn = create_connection()
            cursor = conn.cursor()

            # Adjust this query to fetch the relevant genre details
            query = """
            SELECT m.id_melodie, m.nume, g.nume
            FROM detaliigenuri dg
            JOIN melodie m ON dg.melodie_id_melodie = m.id_melodie
            JOIN genmuzical g ON dg.genmuzical_id_gen_muzical = g.id_gen_muzical
            ORDER BY m.id_melodie
            """
            cursor.execute(query)
            details = cursor.fetchall()

            # Clear existing data in the Treeview
            tree_genre_details.delete(*tree_genre_details.get_children())

            # Inserting new data
            for detail in details:
                tree_genre_details.insert("", tk.END, values=detail)

            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    # Initial call to populate the data
    update_tree_genre_details()

    # Add Refresh Button for Detalii Genuri
    refresh_genre_details_button = tk.Button(genre_details_section, text="Refresh Genre Details", command=update_tree_genre_details)
    refresh_genre_details_button.pack(side='left', padx=5, pady=5)

    add_genre_details_button = tk.Button(genre_details_section, text="Add New Genre Detail", command=open_add_genre_detail_window)
    add_genre_details_button.pack(side='left', padx=5, pady=5)


def open_add_genre_detail_window():
    add_window = tk.Toplevel()
    add_window.title("Add New Genre Detail")

    # Fetch data for ComboBoxes
    songs = fetch_songs()  # Assuming this function returns a list of tuples (id, name)
    genres = fetch_genres()  # Similar function for genres

    # ComboBox for Song Selection
    tk.Label(add_window, text="Select Song:").grid(row=0, column=0)
    song_var = tk.StringVar()
    song_combobox = ttk.Combobox(add_window, textvariable=song_var, values=[f"{song[1]}" for song in songs])
    song_combobox.grid(row=0, column=1)

    # ComboBox for Genre Selection
    tk.Label(add_window, text="Select Genre:").grid(row=1, column=0)
    genre_var = tk.StringVar()
    genre_combobox = ttk.Combobox(add_window, textvariable=genre_var, values=[f"{genre[1]}" for genre in genres])
    genre_combobox.grid(row=1, column=1)

    # Save Button
    save_button = tk.Button(add_window, text="Save", command=lambda: save_new_genre_detail(songs, genres, song_var, genre_var))
    save_button.grid(row=2, column=1)

def save_new_genre_detail(songs, genres, song_var, genre_var):
    song_id = next((song[0] for song in songs if song[1] == song_var.get()), None)
    genre_id = next((genre[0] for genre in genres if genre[1] == genre_var.get()), None)

    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO detaliigenuri (melodie_id_melodie, genmuzical_id_gen_muzical) VALUES (:song_id, :genre_id)", 
                       {"song_id": song_id, "genre_id": genre_id})
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", "New genre detail added successfully.")
    except Exception as e:
        messagebox.showerror("Database Error", str(e))


def fetch_genres():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_gen_muzical, nume FROM genmuzical ORDER BY nume")
        genres = cursor.fetchall()
        cursor.close()
        conn.close()
        return genres
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return []


# Function to open a new window for adding details
def open_add_detail_window():
    add_window = tk.Toplevel()
    add_window.title("Add New Detail")

    # Fetch data for ComboBoxes
    songs = fetch_songs()  # Returns a list of tuples (id, name)
    artists = fetch_artists()  # Similar function for artists
    albums = fetch_albums()  # Similar function for albums

    # Create ComboBoxes for song, artist, and album
    tk.Label(add_window, text="Select Song:").grid(row=0, column=0)
    song_var = tk.StringVar()
    song_combobox = ttk.Combobox(add_window, textvariable=song_var, values=[song[1] for song in songs])
    song_combobox.grid(row=0, column=1)

    tk.Label(add_window, text="Select Artist:").grid(row=1, column=0)
    artist_var = tk.StringVar()
    artist_combobox = ttk.Combobox(add_window, textvariable=artist_var, values=[artist[1] for artist in artists])
    artist_combobox.grid(row=1, column=1)

    tk.Label(add_window, text="Select Album:").grid(row=2, column=0)
    album_var = tk.StringVar()
    album_combobox = ttk.Combobox(add_window, textvariable=album_var, values=[album[1] for album in albums])
    album_combobox.grid(row=2, column=1)

    # Label and Entry for Additional Details
    tk.Label(add_window, text="Additional Details:").grid(row=3, column=0)
    details_entry = tk.Entry(add_window)
    details_entry.grid(row=3, column=1)

    # Save Button
    save_button = tk.Button(add_window, text="Save", command=lambda: save_new_detail(songs, artists, albums, song_var, artist_var, album_var, details_entry))
    save_button.grid(row=4, column=1)

def save_new_detail(songs, artists, albums, song_var, artist_var, album_var, details_entry):
    song_id = next((song[0] for song in songs if song[1] == song_var.get()), None)
    artist_id = next((artist[0] for artist in artists if artist[1] == artist_var.get()), None)
    album_id = next((album[0] for album in albums if album[1] == album_var.get()), None)
    detalii = details_entry.get()

    # Insert data into the database
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO detaliimelodie (id_melodie, id_artist, id_album, detalii) VALUES (:song_id, :artist_id, :album_id, :detalii)", {"song_id": song_id, "artist_id": artist_id, "album_id": album_id, "detalii": detalii})
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", "New detail added successfully.")
        

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

  


def fetch_songs():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_melodie, nume FROM melodie ORDER BY nume")  # Assuming 'melodie' is your songs table
        songs = cursor.fetchall()
        cursor.close()
        conn.close()
        return songs
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return []

def fetch_artists():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_artist, nume FROM artist ORDER BY nume")  # Assuming 'artist' is your artists table
        artists = cursor.fetchall()
        cursor.close()
        conn.close()
        return artists
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return []

def fetch_albums():
    try:
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_album, nume FROM album ORDER BY nume")  # Assuming 'album' is your albums table
        albums = cursor.fetchall()
        cursor.close()
        conn.close()
        return albums
    except Exception as e:
        messagebox.showerror("Database Error", str(e))
        return []



# -----------------------USER WINDOW---------------------------
# Function to create a new window with a button to show data from 'biblioteca_utilizator'
def open_biblioteca_utilizator_window(user_id):
    global tree_biblioteca, tree_melodie_rating

    # Create a new window
    new_window = tk.Toplevel()
    new_window.title("Biblioteca Utilizator")

    # Function to fetch user data
    def fetch_user_data_biblioteca():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            # Adjust this query based on your actual table names and column names
            query = f"""
           SELECT bu.id_biblioteca_utilizator, m.nume, bu.nota
            FROM bilbiotecautilizator bu
            JOIN melodie m ON bu.id_melodie = m.id_melodie
            WHERE bu.id_utilizator = {user_id}
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            
            # Clear existing data in the treeview
            for i in tree_biblioteca.get_children():
                tree_biblioteca.delete(i)

            # Inserting new data
            for row in rows:
                tree_biblioteca.insert("", tk.END, values=row)
            
            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    # Create a Treeview widget to show the data
    tree_biblioteca = ttk.Treeview(new_window, columns=('ID', 'Song Name', 'Note'), show='headings')
    tree_biblioteca.heading('ID', text='ID')
    tree_biblioteca.heading('Song Name', text='Song Name')
    tree_biblioteca.heading('Note', text='Note')
    tree_biblioteca.pack(fill='both', expand=True)

    # Add a button to fetch the data
    fetch_button = tk.Button(new_window, text="Show Biblioteca Info", command=fetch_user_data_biblioteca)
    fetch_button.pack()

    # Initial call to fetch and display data
    fetch_user_data_biblioteca()
    
    # Button to open insert data window
    insert_data_btn = tk.Button(new_window, text="Insert for Biblioteca Utilizator ", command=lambda: open_insert_data_window(user_id))
    insert_data_btn.pack()

    # Button to delete the user and their biblioteca utilizator entries
    delete_button = tk.Button(new_window, text="Delete User and Biblioteca", command=lambda: delete_user_and_biblioteca(user_id, new_window, root))
    delete_button.pack()

    # Function to fetch user data
    def fetch_user_data_melodie_rating():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            # Query to fetch user data including songs and their ratings
        
            # query = f"""
            # SELECT m.id_melodie, m.nume AS "Nume Melodie", r.rating AS "Rating", r.numar_voturi AS "Numar Voturi"
            # FROM melodie m
            # LEFT JOIN ratingmelodie r ON m.id_melodie = r.id_melodie
            # conn.commit()
            
            # artists, albums and genres
            query = """
            SELECT m.id_melodie, m.nume AS "Song Name", rm.rating AS "Rating", rm.numar_voturi AS "Number of Votes",
                LISTAGG(a.nume, ', ') WITHIN GROUP (ORDER BY a.nume) AS "Artists",
                al.nume AS "Album",
                LISTAGG(g.nume, ', ') WITHIN GROUP (ORDER BY g.nume) AS "Genres"
            FROM melodie m
            LEFT JOIN ratingmelodie rm ON m.id_melodie = rm.id_melodie
            LEFT JOIN detaliimelodie dm ON m.id_melodie = dm.id_melodie
            LEFT JOIN artist a ON dm.id_artist = a.id_artist
            LEFT JOIN album al ON dm.id_album = al.id_album
            LEFT JOIN detaliigenuri dg ON m.id_melodie = dg.melodie_id_melodie
            LEFT JOIN genmuzical g ON dg.genmuzical_id_gen_muzical = g.id_gen_muzical
            GROUP BY m.id_melodie, m.nume, rm.rating, rm.numar_voturi, al.nume
            ORDER BY m.id_melodie
            """
            cursor.execute(query)
            rows = cursor.fetchall()

            # Clear existing data in the treeview
            for i in tree_melodie_rating.get_children():
                tree_melodie_rating.delete(i)

            # Inserting new data
            for row in rows:
                tree_melodie_rating.insert("", tk.END, values=row)

            cursor.close()
            conn.close()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def count_votes_for_songs():
        try:
            conn = create_connection()
            cursor = conn.cursor()

            # Calculate the number of votes for each song
            cursor.execute("""
            UPDATE ratingmelodie rm
            SET numar_voturi = (
            SELECT COUNT(bu.id_biblioteca_utilizator)
            FROM bilbiotecautilizator bu
            WHERE rm.id_melodie = bu.id_melodie)
            """)
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Success", "Vote counts updated successfully.")
            # fetch_user_data_melodie_rating()

        except Exception as e:
            messagebox.showerror("Database Error", str(e))
    

    def calculate_song_rating():
        try:
            conn = create_connection()
            cursor = conn.cursor()

            # Calculate average user rating for each song
            cursor.execute("""
            UPDATE ratingmelodie rm
            SET rating = (
                SELECT COALESCE(AVG(bu.nota), 0)
                FROM bilbiotecautilizator bu
                WHERE bu.id_melodie = rm.id_melodie
            )
            """)
            
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Success", "Song ratings updated successfully.")
            fetch_user_data_melodie_rating()


        except Exception as e:
            messagebox.showerror("Database Error", str(e))

    def delete_user_and_biblioteca(user_id, biblioteca_window, main_window):
        # Confirmation dialog
        response = messagebox.askyesno("Confirm", "Are you sure you want to delete this user and all their data?")
        if response:
            try:
                conn = create_connection()
                cursor = conn.cursor()

                # Delete user data from bilbiotecautilizator
                cursor.execute(f"DELETE FROM bilbiotecautilizator WHERE id_utilizator = {user_id}")

                # Delete user from utilizator
                cursor.execute(f"DELETE FROM utilizator WHERE id_utilizator = {user_id}")
                conn.commit()

                # Close the biblioteca window and return to login
                biblioteca_window.destroy()
                main_window.deiconify()
                
                messagebox.showinfo("Success", "User and data deleted successfully.")

                cursor.close()
                conn.close()
            except Exception as e:
                messagebox.showerror("Database Error", str(e))

    # Create a Treeview widget to show user data
    tree_melodie_rating = ttk.Treeview(new_window, columns=('ID', 'Song Name', 'Song Rating', 'Number of Votes', 'Artists', 'Albums', 'Music Genre'), show='headings')
    tree_melodie_rating.heading('ID', text='ID')
    tree_melodie_rating.heading('Song Name', text='Song Name')
    tree_melodie_rating.heading('Song Rating', text='Song Rating')
    tree_melodie_rating.heading('Number of Votes', text='Number of Votes')
    tree_melodie_rating.heading('Artists', text='Artists')
    tree_melodie_rating.heading('Albums', text='Albums')
    tree_melodie_rating.heading('Music Genre', text='Music Genre')

    tree_melodie_rating.pack(fill='both', expand=True)

    # Add a button to fetch and display user data
    fetch_button = tk.Button(new_window, text="Show Melodie and Rating info", command=fetch_user_data_melodie_rating)
    fetch_button.pack()

    # Create buttons for calculating ratings and counting votes
    calculate_rating_button = tk.Button(new_window, text="Calculate Song Ratings", command=calculate_song_rating)
    calculate_rating_button.pack()

    count_votes_button = tk.Button(new_window, text="Count Votes for Songs", command=count_votes_for_songs)
    count_votes_button.pack()





    # Initial call to fetch and display user data
    fetch_user_data_melodie_rating()
    fetch_user_data_biblioteca()





# Function to open the window for inserting or updating data in 'bilbioteca utilizator'

def open_insert_data_window(user_id):
    insert_window = tk.Toplevel()
    insert_window.title("Insert Data")

    # Fetch songs from the database
    def fetch_songs():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT id_melodie, nume FROM melodie")  # Adjust query as needed
            songs = cursor.fetchall()
            cursor.close()
            conn.close()
            return songs
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
            return []

    # Dropdown for song selection
    songs = fetch_songs()
    song_var = tk.StringVar()
    song_combobox = ttk.Combobox(insert_window, textvariable=song_var, values=[f"{song[0]} - {song[1]}" for song in songs])
    song_combobox.grid(row=0, column=1)
    tk.Label(insert_window, text="Select Song:").grid(row=0, column=0)

    # Entry for note
    tk.Label(insert_window, text="Note:").grid(row=1, column=0)
    note_entry = tk.Entry(insert_window)
    note_entry.grid(row=1, column=1)


    # Function to insert or update data in the database
    def insert_or_update_data():
        song_id = song_var.get().split(" - ")[0]
        note = note_entry.get()
        try:
            conn = create_connection()
            cursor = conn.cursor()

            # Check if the entry exists
            check_query = f"SELECT COUNT(*) FROM bilbiotecautilizator WHERE id_utilizator = {user_id} AND id_melodie = {song_id}"
            cursor.execute(check_query)
            exists = cursor.fetchone()[0] > 0

            if exists:
                # Update the note if the entry exists
                update_query = f"UPDATE bilbiotecautilizator SET nota = '{note}' WHERE id_utilizator = {user_id} AND id_melodie = {song_id}"
                cursor.execute(update_query)
                messagebox.showinfo("Success", "Note updated successfully")
            else:
                # Insert new data if the entry does not exist
                insert_query = f"INSERT INTO bilbiotecautilizator (id_utilizator, id_melodie, nota) VALUES ({user_id}, {song_id}, '{note}')"
                cursor.execute(insert_query)
                messagebox.showinfo("Success", "Data inserted successfully")

            conn.commit()
            cursor.close()
            conn.close()
            

        except Exception as e:
            messagebox.showerror("Database Error", str(e))

        # Submit button
    submit_button = tk.Button(insert_window, text="Submit", command=insert_or_update_data)
    submit_button.grid(row=3, column=1)

# Function to open a new window displaying songs and their ratings from the 'melodie' and 'rating_melodie' tables
def open_songs_window():
    songs_window = tk.Toplevel()
    songs_window.title("All Songs with Ratings")

    # Function to fetch all songs and their ratings
    def fetch_all_songs_with_ratings():
        try:
            conn = create_connection()
            cursor = conn.cursor()
            # Join 'melodie' and 'rating_melodie' tables to get songs and their ratings
            query = """
            SELECT m.id_melodie, m.nume, rm.rating
            FROM melodie m
            LEFT JOIN rating_melodie rm ON m.id_melodie = rm.id_melodie
            """
            cursor.execute(query)
            songs_with_ratings = cursor.fetchall()
            cursor.close()
            conn.close()
            return songs_with_ratings
        except Exception as e:
            messagebox.showerror("Database Error", str(e))
            return []

    # Create a Treeview widget to display songs and their ratings
    all_songs_with_ratings = fetch_all_songs_with_ratings()
    tree = ttk.Treeview(songs_window, columns=('ID', 'Song Name', 'Rating'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Song Name', text='Song Name')
    tree.heading('Rating', text='Rating')
    tree.pack(fill='both', expand=True)

    # Insert all songs with ratings into the Treeview
    for song in all_songs_with_ratings:
        tree.insert("", tk.END, values=song)



# Main window
root = tk.Tk()
root.title("Music Database Login")

# Frames
login_frame = create_login_frame(root)
signup_frame = create_signup_frame(root)

login_frame.pack()

root.mainloop()



