# Music-Management

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


Aplikasi Manajemen Musik Sederhana ini dibuat menggunakan Python. Aplikasi ini memungkinkan pengguna untuk mengelola koleksi musik mereka, termasuk menambahkan, mencari lagu dalam koleksi, membuat playlist, dan menambahkan lagu pada playlist.


## Fitur

- Menambahkan Lagu (judul lagu, artis, album, tahun rilis, genre)
- Menampilkan semua lagu dalam koleksi.
- Mencari lagu berdasarkan judul, artis, album, tahun rilis, serta genre
- Membuat Playlist

## Persyaratan Sistem

- Python 3.x
- Modul `customtkinter`
- Modul `tkinter`
- Modul `PIL`
- MySQL Database

## Instalasi

1. Clone repository ini:

    ```bash
    git clone https://github.com/RizqiRahcman/Music-Management.git
    ```
2. Install the module with pip:

    ```bash
    pip3 install customtkinter
    ```

3. Instal dependensi yang diperlukan:

    ```bash
    pip install customtkinter pillow mysql-connector-python
    ```

4. Pastikan Anda telah mengatur database MySQL dengan nama `musicmanagements` dan tabel `lagu`, `playlist`, dan `playlist_lagu` sesuai dengan struktur berikut:

    ```sql
    CREATE TABLE lagu (
        id INT AUTO_INCREMENT PRIMARY KEY,
        judul VARCHAR(255),
        artis VARCHAR(255),
        album VARCHAR(255),
        tahun_rilis INT,
        genre VARCHAR(255)
    );

    CREATE TABLE playlist (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nama_playlist VARCHAR(255)
    );

    CREATE TABLE playlist_lagu (
        playlist_id INT,
        lagu_id INT,
        FOREIGN KEY (playlist_id) REFERENCES playlist(id),
        FOREIGN KEY (lagu_id) REFERENCES lagu(id)
    );
    ```

## Penggunaan

1. Jalankan aplikasi:

    ```bash
    main.py
    ```

2. Gunakan sidebar di sebelah kiri untuk menavigasi fitur-fitur yang tersedia:
    - Tambah Lagu
    - Lihat Lagu
    - Cari Lagu
    - Buat Playlist
    - Lihat Playlist
    - Tambah Lagu ke Playlist

## Struktur Proyek

music_management/
├── Addsongs.png
├── album.png
├── addplaylist.png
├── Search.png
├── play.png
├── logo_2.png
├── list_icon.png
├── musicmanagement.sql
├── main.py
└── README.md



## License

MIT

**Free Software, Hell Yeah!**
