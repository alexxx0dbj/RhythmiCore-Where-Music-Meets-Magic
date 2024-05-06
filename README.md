# <p align="center"><span style="font-style: italic; font-weight: bold;">RhythmiCore-Where-Music-Meets-Magic</span></p>

## Database Application in Oracle SQL with Tkinter Python Interface
### Project Title: GUI similar to Spotify Database Management System

### Key Responsibilities:

- **Oracle Database Design with Entity Relationship Diagram**
- **Database Population**
- **Data Manipulation**
- **Tkinter Interface**

# Project Description (Non-Technical):

The chosen database will model the operation of a music library. The main idea of the project is to create an application specially designed for music enthusiasts who want an easy way to organize and play their favorite music collections. With the help of this application, users can add and manage their favorite songs, artists, and albums, as well as create their own personalized library of songs, perfectly tailored to their mood or event. With RhythmiCore, every user can always have their favorite songs at hand and create their own personalized musical space based on the genre they resonate with, artist, song, or album, and ultimately have the possibility to rate them after listening.

# Technical Description:

The database aims to manage the following entities from a technical and analytical perspective:

1. **User Entity**:
   - User ID (primary key): numeric value, mandatory, unique for each user
   - Name: string value, mandatory, unique
   - Password: string value, mandatory
   - Email: string value, mandatory, unique

2. **Artist Entity**:
   - Artist ID (primary key): numeric value, mandatory, unique for each artist
   - Name: string value, mandatory, unique

3. **Album Entity**:
   - Album ID (primary key): numeric value, mandatory, unique for each album
   - Name: string value, mandatory

4. **Song Entity**:
   - Song ID (primary key): numeric value, mandatory, unique for each song
   - Name: string value, mandatory

5. **User Library Entity**:
   - User Library ID (primary key): numeric value, mandatory, unique for each user library
   - Rating: numeric value, mandatory
   - User ID (foreign key): links user library to user
   - Song ID (foreign key): links user library to song

6. **Music Genre Entity**:
   - Music Genre ID (primary key): numeric value, mandatory, unique for each music genre
   - Name: string value, mandatory
   - Details: string value, optional
   - Rating ID (foreign key): links music genre to rating

7. **Song Rating Entity**:
   - Rating: numeric value, mandatory, in the range 1-5
   - Vote count: numeric value, optional
   - Song ID (foreign key): links song to song rating

8. **Song Details Entity**:
   - Song ID (foreign key): links album to song details
   - Artist ID (foreign key): attribute used to solve the many-to-many relationship between song and artist entities
   - Album ID (foreign key): links album to song details
   - Details: string value, optional

9. **Genre Details Entity**:
   - Song ID (foreign key): attribute used to solve the many-to-many relationship between song and music genre entities
   - Music Genre ID (foreign key): attribute used to solve the many-to-many relationship between song and music genre entities
   - Description: string value, optional

In the context of the described application for managing the music library, some functionalities are covered or are the main purpose of the application. Here are some of these issues: user registration and authentication, song registration and exploration, artist and album management. Additionally, some of the most important entity relationships include user registration, user library records, artist-album relationships, song-album relationships, song-music genre relationships, and user-song rating relationships.

The application does not address: advanced music discovery features, personalized playlists, comments, and reviews.

## *Logical Schema*

The resolution of the many-to-many relationship: To solve the many-to-many relationship between Album-Song, Album-Artist, and Song-Artist, an intermediate entity named SongDetails is used, which will have foreign keys on all three entities (artist, album, and song).

![Logical](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/f6009690-f0db-4e3b-8a11-cd1fb70ae0c1)

## *Relational Schema*

**Normalization of Databases:**
Normalization represents the process of organizing (without losing information) the attributes and tables in a relational database with the aim of minimizing data redundancy and, implicitly, minimizing potential errors that may occur in data manipulation.

**First Normal Form (1NF):**
A relation is in the first normal form if it satisfies the following conditions:
- An attribute contains atomic values from its domain (and not groups of such values)
- It does not contain repeating groups

**Second Normal Form (2NF):**
A relation is in the second normal form if it satisfies the following conditions:
- It is in the first normal form
- All non-key attributes are fully dependent on ALL candidate keys

**Third Normal Form (3NF):**
A relation is in the third normal form if it satisfies the following conditions:
- It is in the second normal form
- All non-key attributes are directly (non-transitively) dependent on ALL candidate keys

The many-to-many relationship between the MusicGenre and Song tables indicates that a song can belong to multiple music genres and a music genre can be associated with multiple songs. In this case, the relational model includes the GenreDetails table to manage this relationship. We have a foreign key music_genre_id_music_genre to id_music_genre from the MusicGenre table, and we have a foreign key song_id_song to id_song from the Song table. This approach allows each song to be associated with multiple music genres, and each music genre to be associated with multiple songs. Through the GenreDetails table, the connection between these two entities is achieved, thus allowing a many-to-many relationship.

![Relational](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/157c50db-3ee7-41dd-92fe-ca592e554451)


The use of auto-increment allows for the automatic generation of primary key values in tables. This way, managing primary keys becomes much simpler, avoiding errors in manual assignment of unique values for each record in the database population script. Examples of auto-increment usage: on user_id, user_library_id, music_genre_id, album_id, artist_id, and song_id.

Using triggers for auto-increment, each table that uses a sequence to implement auto-increment has an associated trigger. The trigger ensures that before each insert operation, the sequence is called and the generated value is automatically assigned to the corresponding column attribute.

### *Technologies Used*

The back-end part was developed using the Python programming language. For the front-end part, the tkinter package was used, one of the most commonly used packages for implementing graphical interfaces in Python. Tkinter is a graphical user interface (GUI) library for the Python programming language. It allows developers to create user interfaces (UI) for desktop applications. Tkinter provides a set of tools and graphical widgets, such as windows, buttons, labels, and text fields, which can be used to create applications with customized user interfaces.

## *Graphical Interface Screenshots*
### *Login Window for Existing User*
![p1](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/3ebe7e08-1453-4979-bc40-f5d7a2046810)
![p2](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/4c8bc919-7b37-42e5-82f7-8e5721902478)


### *Register Window for New User*
![p3](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/0dec2884-6afc-4e1d-90b4-a716a9d9a1ea)

### *Viewing Window for User*
![4](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/55522647-5ef7-4128-9462-e3b512a7fbe7)

#### Presence of an "Insert" button that opens another window where the user can add a new song and provide a rating. If the song already exists, only the rating of the existing song in their library is updated.
![6](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/4dc9ce78-1b40-4306-ba97-fbce27bb6591)
![5](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/56c30673-305b-4ea4-ab49-a832239f7978)

### *Viewing Window for Admin*

![7](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/96edf3d2-f951-45f4-98c1-5930e1bc24d4)

![8](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/2a94ac8e-e0f2-4634-856b-7f0977d21039)

![9](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/c33d1f61-9625-4357-9dea-44f5931998f7)

![10](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/047a38de-2079-4dfb-a317-a42f499d1935)

![11](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/18b43fa1-0d5c-4c46-ac35-4aa73bf9114a)

![12](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/555a839a-c684-4c0b-b7da-021c5c552c4e)

![13](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/7ccc08c1-4ba3-4d54-8eb8-c23cfe6e5be7)

![14](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/40b7e74c-025d-4ca6-bfaf-834e0fbd4c06)

![15](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/05855c6c-ff22-4e59-a0b4-d4539e434a3c)

![16](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/264e4e79-4a6b-417a-ad2e-8869e976333e)

![17](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/10b79471-3648-4aed-bd9d-ab39f9b8cbbc)

![18](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/77e2b0d6-7805-448a-8716-510f2b8a3132)

![19](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/cf7d495c-1e71-4e5c-ae2b-952d204aa530)

![20](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/44bf67d0-7b58-4bcd-afc8-0320647298a4)

![21](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/61963bfe-069d-4e2a-8605-f42212c303a3)

![22](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/0fe2f6e6-2641-4940-921c-ea0585cc2e1e)

![23](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/3f703bff-1657-4081-ab07-23cd6159afa9)

![24](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/99eae255-b9e0-440b-8f85-43a52262b106)

![25](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/857571b6-5476-402e-af28-32852154eac9)

![26](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/60cab65a-41d6-4256-8c0d-204e7c152b5f)

![27](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/3bc58ff4-9bd8-468c-a8d8-76e0ba1adb40)

![28](https://github.com/alexxx0dbj/RhythmiCore-Where-Music-Meets-Magic/assets/121617664/9a3323ee-0910-41f4-83c0-2646390f7bf0)


