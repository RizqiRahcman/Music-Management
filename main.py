import customtkinter as ctk
from tkinter import ttk
from PIL import Image
import mysql.connector

app = ctk.CTk()
app.geometry("856x645")
app.resizable(0, 0)

ctk.set_appearance_mode("light")


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="musicmanagements"
    )


def TambahLagu():
    global title_entry, artist_entry, album_entry, year_entry, genre_entry

    def save_song():
        # Mengambil data dari input fields
        judul = title_entry.get()
        artis = artist_entry.get()
        album = album_entry.get()
        tahun_rilis = year_entry.get()
        genre = genre_entry.get()

        # Membuat koneksi ke database
        conn = connect_to_database()
        # Membuat kursor
        cursor = conn.cursor()

        # Query untuk menyimpan lagu ke database
        query = "INSERT INTO lagu (judul, artis, album, tahun_rilis, genre) VALUES (%s, %s, %s, %s, %s)"
        data = (judul, artis, album, tahun_rilis, genre)

        try:
            # Menjalankan query
            cursor.execute(query, data)

            # Commit perubahan ke database
            conn.commit()

                # Memberi pesan jika penyimpanan berhasil
            success_label.configure(text="Lagu berhasil disimpan!")
            app.after(3000, lambda: success_label.configure(text=""))  
        except mysql.connector.Error as err:
            # Memberi pesan jika terjadi error
            success_label.configure(text=f"Error: {err}")
        finally:
            # Menutup kursor dan koneksi
            cursor.close()
            conn.close()

    for widget in main_view.winfo_children():
        widget.destroy()

    tambahlagu_frame = ctk.CTkFrame(master=main_view, fg_color="transparent")
    tambahlagu_frame.pack(anchor="center", padx=27, pady=(100, 0))

    title_label = ctk.CTkLabel(master=tambahlagu_frame, text="Judul:", font=("Arial", 14))
    title_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")
    title_entry = ctk.CTkEntry(master=tambahlagu_frame, width=300)
    title_entry.grid(row=0, column=1, padx=20, pady=10)

    artist_label = ctk.CTkLabel(master=tambahlagu_frame, text="Artis:", font=("Arial", 14))
    artist_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
    artist_entry = ctk.CTkEntry(master=tambahlagu_frame, width=300)
    artist_entry.grid(row=1, column=1, padx=20, pady=10)

    album_label = ctk.CTkLabel(master=tambahlagu_frame, text="Album:", font=("Arial", 14))
    album_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
    album_entry = ctk.CTkEntry(master=tambahlagu_frame, width=300)
    album_entry.grid(row=2, column=1, padx=20, pady=10)

    year_label = ctk.CTkLabel(master=tambahlagu_frame, text="Tahun Rilis:", font=("Arial", 14))
    year_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
    year_entry = ctk.CTkEntry(master=tambahlagu_frame, width=300)
    year_entry.grid(row=3, column=1, padx=20, pady=10)

    genre_label = ctk.CTkLabel(master=tambahlagu_frame, text="Genre:", font=("Arial", 14))
    genre_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")
    genre_entry = ctk.CTkEntry(master=tambahlagu_frame, width=300)
    genre_entry.grid(row=4, column=1, padx=20, pady=10)

    # Button untuk menyimpan lagu
    save_button = ctk.CTkButton(master=tambahlagu_frame, text="Simpan", command=save_song, width=200, height=40, font=("Arial", 14))
    save_button.grid(row=5, column=0, columnspan=2, pady=20)

    success_label = ctk.CTkLabel(master=tambahlagu_frame, text="", font=("Arial", 14), text_color="green")
    success_label.grid(row=6, column=0, columnspan=2, pady=10)


def view_song():
    for widget in main_view.winfo_children():
        widget.destroy()

    view_window = ctk.CTkFrame(master=main_view, fg_color="#fff", width=780, height=650)
    view_window.pack_propagate(0)
    view_window.pack(side="top", fill="both", expand=True)

    # Membuat treeview untuk menampilkan daftar lagu dalam bentuk tabel
    columns = ("Judul", "Artis", "Album", "Tahun Rilis", "Genre")
    tree = ttk.Treeview(view_window, columns=columns, show="headings", height=30)

      # Mengatur lebar kolom
    tree.column("Judul", width=200, anchor="center")
    tree.column("Artis", width=150, anchor="center")
    tree.column("Album", width=150, anchor="center")
    tree.column("Tahun Rilis", width=100, anchor="center")
    tree.column("Genre", width=150, anchor="center")
    
    # Mengatur lebar kolom
    for col in columns:
        tree.heading(col, text=col)
        

    # Menambahkan scrollbar
    scrollbar = ttk.Scrollbar(view_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    tree.pack(fill="both", expand=True)

    # Membuat koneksi ke database
    conn = connect_to_database()
    cursor = conn.cursor()

    # Query untuk mengambil semua lagu dari tabel lagu
    query = "SELECT * FROM lagu"

    try:
        # Menjalankan query
        cursor.execute(query)

        # Memasukkan data lagu ke dalam treeview
        for song in cursor.fetchall():
            tree.insert("", "end", values=song[1:])
    except mysql.connector.Error as err:
        # Memberi pesan jika terjadi error
        print(f"Error: {err}")
    finally:
        # Menutup kursor dan koneksi
        cursor.close()
        conn.close()


def search_song():
    def perform_search():
        keyword = search_entry.get()

        # Membuat koneksi ke database
        conn = connect_to_database()
        cursor = conn.cursor()

        # Query untuk mencari lagu berdasarkan keyword
        query = (
            "SELECT * FROM lagu "
            "WHERE judul LIKE %s OR artis LIKE %s OR album LIKE %s OR genre LIKE %s"
        )
        data = (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")

        try:
            # Menjalankan query
            cursor.execute(query, data)

            # Menghapus hasil pencarian sebelumnya
            for row in tree.get_children():
                tree.delete(row)

            # Memasukkan data lagu yang cocok ke dalam treeview
            for song in cursor.fetchall():
                tree.insert("", "end", values=song[1:])
        except mysql.connector.Error as err:
            # Memberi pesan jika terjadi error
            print(f"Error: {err}")
        finally:
            # Menutup kursor dan koneksi
            cursor.close()
            conn.close()

    for widget in main_view.winfo_children():
        widget.destroy()

    search_window = ctk.CTkFrame(master=main_view, fg_color="#fff", width=780, height=650)
    search_window.pack_propagate(0)
    search_window.pack(side="top", fill="both", expand=True)

    search_entry = ctk.CTkEntry(master=search_window, width=400, placeholder_text="Masukkan keyword pencarian")
    search_entry.pack(pady=20)

    search_button = ctk.CTkButton(master=search_window, text="Cari", command=perform_search)
    search_button.pack(pady=10)

    # Membuat treeview untuk menampilkan hasil pencarian dalam bentuk tabel
    columns = ("Judul", "Artis", "Album", "Tahun Rilis", "Genre")
    tree = ttk.Treeview(search_window, columns=columns, show="headings")

    # Mengatur lebar kolom
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")

    # Menambahkan scrollbar
    scrollbar = ttk.Scrollbar(search_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    tree.pack(fill="both", expand=True)


# Create Playlist function
def create_playlist():
    def save_playlist():
        # Mengambil nama playlist dari input field
        nama_playlist = playlist_name_entry.get()

        # Membuat koneksi ke database
        conn = connect_to_database()
        cursor = conn.cursor()

        # Query untuk menyimpan playlist ke dalam database
        query = "INSERT INTO playlist (nama_playlist) VALUES (%s)"
        data = (nama_playlist,)

        try:
            # Menjalankan query
            cursor.execute(query, data)

            # Commit perubahan ke database
            conn.commit()

             # Memberi pesan jika penyimpanan berhasil
            success_label.configure(text="Playlist berhasil ditambahkan!")
            app.after(3000, lambda: success_label.configure(text=""))  # Menghapus pesan setelah 3 detik
        except mysql.connector.Error as err:
            # Memberi pesan jika terjadi error
            success_label.configure(text=f"Error: {err}")
        finally:
            # Menutup kursor dan koneksi
            cursor.close()
            conn.close()

    for widget in main_view.winfo_children():
        widget.destroy()

    create_playlist_window = ctk.CTkFrame(master=main_view, fg_color="#fff", width=780, height=650)
    create_playlist_window.pack_propagate(0)
    create_playlist_window.pack(side="top", fill="both", expand=True)

    playlist_name_label = ctk.CTkLabel(master=create_playlist_window, text="Nama Playlist:", font=("Arial", 14))
    playlist_name_label.pack(pady=20)

    playlist_name_entry = ctk.CTkEntry(master=create_playlist_window, width=400, placeholder_text="Masukkan nama playlist")
    playlist_name_entry.pack(pady=10)

    save_button = ctk.CTkButton(master=create_playlist_window, text="Simpan Playlist", command=save_playlist)
    save_button.pack(pady=10)

    success_label = ctk.CTkLabel(master=create_playlist_window, text="", font=("Arial", 14), text_color="green")
    success_label.pack(anchor="center", pady=10)

def view_playlist_songs():
    def view_songs_in_playlist(playlist_id):
        # Membuat koneksi ke database
        conn = connect_to_database()
        cursor = conn.cursor()

        # Query untuk mengambil lagu-lagu dalam playlist
        query = "SELECT l.judul, l.artis, l.album, l.tahun_rilis, l.genre " \
                 "FROM lagu l " \
                 "JOIN playlist_lagu pl ON l.id = pl.lagu_id " \
                 "WHERE pl.playlist_id = %s"
        data = (playlist_id,)

        try:
            # Menjalankan query
            cursor.execute(query, data)

            # Menghapus hasil pencarian sebelumnya
            for row in tree.get_children():
                tree.delete(row)

            # Memasukkan data lagu-lagu dalam playlist ke dalam treeview
            for song in cursor.fetchall():
                tree.insert("", "end", values=song)
        except mysql.connector.Error as err:
            # Memberi pesan jika terjadi error
            print(f"Error: {err}")
        finally:
            # Menutup kursor dan koneksi
            cursor.close()
            conn.close()

    for widget in main_view.winfo_children():
        widget.destroy()

    view_playlist_window = ctk.CTkFrame(master=main_view, fg_color="#fff", width=780, height=650)
    view_playlist_window.pack_propagate(0)
    view_playlist_window.pack(side="top", fill="both", expand=True)

    playlist_label = ctk.CTkLabel(master=view_playlist_window, text="Pilih Playlist:", font=("Arial", 14))
    playlist_label.pack(pady=10)

    # Combobox untuk memilih playlist
    playlist_combobox = ttk.Combobox(master=view_playlist_window, width=50)
    playlist_combobox.pack(pady=10)

    # Mengambil daftar playlist dari database
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nama_playlist FROM playlist")
    playlists = cursor.fetchall()
    cursor.close()
    conn.close()

    playlist_combobox['values'] = [f"{playlist[0]} - {playlist[1]}" for playlist in playlists]

    view_button = ctk.CTkButton(master=view_playlist_window, text="Lihat Lagu", command=lambda: view_songs_in_playlist(playlist_combobox.get().split(" - ")[0]))
    view_button.pack(pady=10)

    # Membuat treeview untuk menampilkan lagu-lagu dalam playlist
    columns = ("Judul", "Artis", "Album", "Tahun Rilis", "Genre")
    tree = ttk.Treeview(view_playlist_window, columns=columns, show="headings")

    # Mengatur lebar kolom
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor="center")

    # Menambahkan scrollbar
    scrollbar = ttk.Scrollbar(view_playlist_window, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    tree.pack(fill="both", expand=True)

# Function to add song to playlist
def add_song_to_playlist():
    def save_to_playlist():
        selected_song = song_combobox.get()
        selected_playlist = playlist_combobox.get()

        # Memisahkan ID dari nama lagu dan playlist
        song_id = selected_song.split(" - ")[0]
        playlist_id = selected_playlist.split(" - ")[0]

        # Membuat koneksi ke database
        conn = connect_to_database()
        cursor = conn.cursor()

        # Query untuk menambahkan lagu ke playlist
        query = "INSERT INTO playlist_lagu (playlist_id, lagu_id) VALUES (%s, %s)"
        data = (playlist_id, song_id)

        try:
            # Menjalankan query
            cursor.execute(query, data)

            # Commit perubahan ke database
            conn.commit()

               # Memberi pesan jika penyimpanan berhasil
            success_label.configure(text="Lagu Berhasil Ditambahkan Ke Playlist!")
            app.after(3000, lambda: success_label.configure(text=""))  
        except mysql.connector.Error as err:
            # Memberi pesan jika terjadi error
            success_label.configure(text=f"Error: {err}")
        finally:
            # Menutup kursor dan koneksi
            cursor.close()
            conn.close()

    for widget in main_view.winfo_children():
        widget.destroy()

    add_to_playlist_window = ctk.CTkFrame(master=main_view, fg_color="#fff", width=780, height=650)
    add_to_playlist_window.pack_propagate(0)
    add_to_playlist_window.pack(side="top", fill="both", expand=True)

    song_label = ctk.CTkLabel(master=add_to_playlist_window, text="Pilih Lagu:", font=("Arial", 14))
    song_label.pack(pady=10)


    # Combobox untuk memilih lagu
    song_combobox = ttk.Combobox(master=add_to_playlist_window, width=50)
    song_combobox.pack(pady=10)

    # Mengambil daftar lagu dari database
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT id, judul FROM lagu")
    songs = cursor.fetchall()
    cursor.close()
    conn.close()

    song_combobox['values'] = [f"{song[0]} - {song[1]}" for song in songs]

    playlist_label = ctk.CTkLabel(master=add_to_playlist_window, text="Pilih Playlist:", font=("Arial", 14))
    playlist_label.pack(pady=10)

    # Combobox untuk memilih playlist
    playlist_combobox = ttk.Combobox(master=add_to_playlist_window, width=50)
    playlist_combobox.pack(pady=10)

    # Mengambil daftar playlist dari database
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nama_playlist FROM playlist")
    playlists = cursor.fetchall()
    cursor.close()
    conn.close()

    playlist_combobox['values'] = [f"{playlist[0]} - {playlist[1]}" for playlist in playlists]

    save_button = ctk.CTkButton(master=add_to_playlist_window, text="Tambahkan ke Playlist", command=save_to_playlist)
    save_button.pack(pady=20)

    success_label = ctk.CTkLabel(master=add_to_playlist_window, text="", font=("Arial", 14), text_color="green")
    success_label.pack(anchor="center", pady=10)
    


sidebar_frame = ctk.CTkFrame(master=app, fg_color="#3D52A0", width=176, height=650, corner_radius=0)
sidebar_frame.pack_propagate(0)
sidebar_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open("logo_2.png")
logo_img = ctk.CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(200, 200))

ctk.CTkLabel(master=sidebar_frame, text="", image=logo_img).pack(pady=(10, 0), anchor="center")

# Add songs
add_songs_img = Image.open("Addsongs.png")
add_songs = ctk.CTkImage(dark_image=add_songs_img, light_image=add_songs_img)
ctk.CTkButton(master=sidebar_frame, image=add_songs, text="Tambah Lagu", fg_color="transparent", font=("Arial Bold", 14),
              text_color="#fff", hover_color="#7091E6", anchor="w", command=TambahLagu).pack(anchor="center", ipady=5, pady=(20, 0))

# View songs
view_songs_img = Image.open("album.png")
view_songs = ctk.CTkImage(dark_image=view_songs_img, light_image=view_songs_img)
ctk.CTkButton(master=sidebar_frame, image=view_songs, text="Lihat Lagu", fg_color="transparent", font=("Arial Bold", 14),
              text_color="#fff", hover_color="#7091E6", anchor="w", command=view_song).pack(anchor="center", ipady=5, pady=(16, 0))

# Tambahkan tombol "Buat Playlist" ke dalam sidebar_frame
create_playlist_img = Image.open("addplaylist.png")
create_playlist_icon = ctk.CTkImage(dark_image=create_playlist_img, light_image=create_playlist_img)
create_playlist_button = ctk.CTkButton(master=sidebar_frame, image=create_playlist_icon, text="Buat Playlist", fg_color="transparent",
                                       font=("Arial Bold", 14), text_color="#fff", hover_color="#7091E6",
                                       anchor="w", command=create_playlist)
create_playlist_button.pack(anchor="center", ipady=5, pady=(16, 0))

# Search songs
search_songs_img = Image.open("Search.png")
search_songs = ctk.CTkImage(dark_image=search_songs_img, light_image=search_songs_img)
ctk.CTkButton(master=sidebar_frame, image=search_songs, text="Cari Lagu", fg_color="transparent", font=("Arial Bold", 14),
              text_color="#fff", hover_color="#7091E6", anchor="w", command=search_song).pack(anchor="center", ipady=5, pady=(16, 0))

# Tambahkan tombol "Lihat Lagu di Playlist" ke dalam sidebar_frame
view_playlist_img = Image.open("play.png")
view_playlist_icon = ctk.CTkImage(dark_image=view_playlist_img, light_image=view_playlist_img)
view_playlist_button = ctk.CTkButton(master=sidebar_frame, image=view_playlist_icon,text= "Lihat Playlist", fg_color="transparent",
                                     font=("Arial Bold", 14), text_color="#fff", hover_color="#7091E6",
                                     anchor="w", command=view_playlist_songs)
view_playlist_button.pack(anchor="center", ipady=5, pady=(16, 0))

# Add song to playlist
# Tidak menggunakan gambar untuk tombol ini
add_song_to_playlist_image = Image.open("addplaylist.png")
add_song_to_playlist_icon = ctk.CTkImage(dark_image=add_song_to_playlist_image, light_image=add_song_to_playlist_image)
add_song_to_playlist_button = ctk.CTkButton(master=sidebar_frame, image=add_song_to_playlist_icon, text="Tambah ke Playlist", fg_color="transparent",
                                            font=("Arial Bold", 14), text_color="#fff", hover_color="#7091E6",
                                            anchor="w", command=add_song_to_playlist)
add_song_to_playlist_button.pack(anchor="center", ipady=5, pady=(16, 0))

# Main View
main_view = ctk.CTkFrame(master=app, fg_color="#fff", width=780, height=650, corner_radius=0)
main_view.pack_propagate(0)
main_view.pack(side="top", fill="both", expand=True)

app.mainloop()
