playlists = []

# data login (username dan password)
users = {
    'admin': 'admin123',
    'user': 'user123'
}

# menambah lagu
def tambah_lagu(title, genre, mood):
    playlists.append({"title": title, "genre": genre, "mood": mood})

# menampilkan semua lagu dalam playlist
def tampilkan_playlist():
    if not playlists:
        print("Playlist kosong.")
    else:
        print("\nPlaylist:")
        for index, song in enumerate(playlists, start=1):
            print(f"{index}. {song['title']} ({song['genre']}, {song['mood']})")

# mengupdate data lagu
def update_lagu(index, title, genre, mood):
    if 0 <= index < len(playlists):
        playlists[index] = {"title": title, "genre": genre, "mood": mood}
        print(f"Lagu {title} berhasil diupdate.")
    else:
        print("Lagu tidak ditemukan.")

# menghapus lagu
def hapus_lagu(index):
    if 0 <= index < len(playlists):
        removed_song = playlists.pop(index)
        print(f"Lagu '{removed_song['title']}' berhasil dihapus.")
    else:
        print("Lagu tidak ditemukan.")

# filter berdasarkan genre
def filter_by_genre(genre):
    return [song for song in playlists if song["genre"].lower() == genre.lower()]

# filter berdasarkan mood
def filter_by_mood(mood):
    return [song for song in playlists if song["mood"].lower() == mood.lower()]

# mencari lagu berdasarkan judul
def search_song(title):
    return [song for song in playlists if title.lower() in song["title"].lower()]

# fungsi login
def login():
    print("\n=== Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Cek apakah username dan password ada dalam dictionary users
    if username not in users and password not in users.values():
        print("Username dan password salah.")
        return None
    
    # Cek apakah username ada dalam dictionary users
    if username not in users:
        print("Username Salah.")
        return None
    
    # Cek apakah password yang dimasukkan sesuai
    if users.get(username) != password:
        print("Password salah.")
        return None
    
    # Jika username dan password benar
    print(f"\nSelamat datang, {username}!")
    return username

# menu untuk Admin
def menu_admin():
    tambah_lagu("Drunk text", "Pop", "Sad")
    tambah_lagu("Patience", "Pop", "Sad")
    tambah_lagu("The Scientist", "Rock", "Chill")
    tambah_lagu("Apocalypse", "Pop", "Chill")
    tambah_lagu("No.1 Party Anthem", "Rock", "Happy")
    tambah_lagu("Glimpse of Us", "Pop", "Sad")
    tambah_lagu("Forever Young", "Pop", "Happy")
    tambah_lagu("Yellow", "Pop", "Romance")
    tambah_lagu("Cloks", "Rock", "Sad")
    tambah_lagu("Atlantis", "Pop", "Sad")
    while True:
        print("Menu Admin:")
        print("1. Tambah lagu")
        print("2. Tampilkan playlist")
        print("3. Update lagu")
        print("4. Hapus lagu")
        print("5. Filter musik berdasarkan genre")
        print("6. Filter musik berdasarkan suasana hati")
        print("7. Pencarian lagu")
        print("8. Keluar")

        choice = input("Pilih opsi (1-8): ")

        if choice == '1':
            title = input("Masukkan judul lagu: ")
            genre = input("Masukkan genre (Pop / Rock): ")
            mood = input("Masukkan suasana hati (happy, chill, Sad, Romance.): ")
            tambah_lagu(title, genre, mood)
            print(f"Lagu '{title}' berhasil ditambahkan ke playlist.")
        
        elif choice == '2':
            tampilkan_playlist()

        elif choice == '3':
            tampilkan_playlist()
            index = int(input("Masukkan nomor lagu yang ingin diupdate: ")) - 1
            title = input("Masukkan judul lagu baru: ")
            genre = input("Masukkan genre baru (Pop / Rock): ")
            mood = input("Masukkan suasana hati baru (happy, chill, Sad, Romance.): ")
            update_lagu(index, title, genre, mood)

        elif choice == '4':
            tampilkan_playlist()
            index = int(input("Masukkan nomor lagu yang ingin dihapus: ")) - 1
            hapus_lagu(index)
        
        elif choice == '5':
            genre = input("Masukkan genre (Pop / Rock): ")
            songs = filter_by_genre(genre)
            if songs:
                print(f"\nPlaylist untuk genre '{genre}':")
                for song in songs:
                    print(f"- {song['title']}")
            else:
                print("Genre tidak ditemukan.")
        
        elif choice == '6':
            mood = input("Masukkan suasana hati (happy, chill, Sad, Romance.): ")
            songs = filter_by_mood(mood)
            if songs:
                print(f"\nPlaylist untuk suasana hati '{mood}':")
                for song in songs:
                    print(f"- {song['title']}")
            else:
                print("Tidak ada lagu untuk suasana hati tersebut.")
        
        elif choice == '7':
            title = input("Masukkan judul lagu: ")
            songs = search_song(title)
            if songs:
                print(f"\nHasil pencarian untuk '{title}':")
                for song in songs:
                    print(f"- {song['title']}")
            else:
                print("Lagu tidak ditemukan.")
        
        elif choice == '8':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menu untuk user
def menu_user():
    tambah_lagu("Drunk text", "Pop", "Sad")
    tambah_lagu("Patience", "Pop", "Sad")
    tambah_lagu("The Scientist", "Rock", "Chill")
    tambah_lagu("Apocalypse", "Pop", "Chill")
    tambah_lagu("No.1 Party Anthem", "Rock", "Happy")
    tambah_lagu("Glimpse of Us", "Pop", "Sad")
    tambah_lagu("Forever Young", "Pop", "Happy")
    tambah_lagu("Yellow", "Pop", "Romance")
    tambah_lagu("Cloks", "Rock", "Sad")
    tambah_lagu("Atlantis", "Pop", "Sad")
    while True:
        print("Menu User:")
        print("1. Tambah lagu")
        print("2. Tampilkan playlist")
        print("3. Filter musik berdasarkan genre")
        print("4. Filter musik berdasarkan suasana hati")
        print("5. Pencarian lagu")
        print("6. Keluar")

        choice = input("Pilih opsi (1-6): ")

        if choice == '1':
            title = input("Masukkan judul lagu: ")
            genre = input("Masukkan genre (Pop / Rock): ")
            mood = input("Masukkan suasana hati (happy, chill, Sad, Romance.): ")
            tambah_lagu(title, genre, mood)
            print(f"Lagu '{title}' berhasil ditambahkan ke playlist.")
        
        elif choice == '2':
            tampilkan_playlist()

        elif choice == '3':
            genre = input("Masukkan genre (Pop / Rock): ")
            songs = filter_by_genre(genre)
            if songs:
                print(f"\nPlaylist untuk genre '{genre}':")
                for song in songs:
                    print(f"- {song['title']}")
            else:
                print("Genre tidak ditemukan.")
        
        elif choice == '4':
            mood = input("Masukkan suasana hati (happy, chill, Sad, Romance.): ")
            songs = filter_by_mood(mood)
            if songs:
                print(f"\nPlaylist untuk suasana hati '{mood}':")
                for song in songs:
                    print(f"- {song['title']}")
            else:
                print("Tidak ada lagu untuk suasana hati tersebut.")
        
        elif choice == '5':
            title = input("Masukkan judul lagu: ")
            songs = search_song(title)
            if songs:
                print(f"\nHasil pencarian untuk '{title}':")
                for song in songs:
                    print(f"- {song['title']}")
            else:
                print("Lagu tidak ditemukan.")
        
        elif choice == '6':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def main():
    # sistem login
    username = None
    while username is None:
        username = login()

    if username == 'admin':
        menu_admin()
    elif username == 'user':
        menu_user()

main()