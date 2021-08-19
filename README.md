# KelompokH-Final Project : Snake Game

**Snake Game**

Aplikasi permainan ular menggunakan _pygame_. Terinspirasi dari permainan ular yang ada di awal perkembangan teknologi secara _mobile_ dengan membuat permainan tersebut menggunakan bahasa python dan _library Pygame_. 

_Source code_ untuk membuat _snake game_ ini dengan _pygame_ 

1. Persyaratan 
Sebelum menggunakan _source code_ dalam _snake game_ ini, terlebih dahulu menginstalisasi _pygame_:

> Pip install pygame

_Pygame_ merupakan modul phyton yang berisikan fungsi dan _class_ yang dibutuhkan dalam pembuatan permainan.

Setelah melakukan instalisasi pygame kemudian dilakukan pengecekan terlebih dahulu pygame yang sudah terinstal di phyton dengan masuk ke _shell_ python dengan mengetik perintah :
>>> import pygame

2. Cara menggunakan _source code_
Sebelum masuk ke dalam permainan snake game, berikut ini beberapa bagian yang membangun permainan ular dengan python:
- Membuat jendela layar permainan
- Membuat model ular
- Memindahkan Ular
- _Game over_ saat ular mencapai batas
- Menambahkan makanan
- Meningkatkan panjang badan ular
- Menampilkan Skor permainan

_Source code_ ini terdiri dari fungsi _Pygame_ yang telah digunakan di permainan ular ini beserta penjelasannya.
![tabel 1  fungsi](https://user-images.githubusercontent.com/89029568/130014934-82d99366-e15f-4b83-8291-673901fa7a51.PNG)

Sebelum memulai permainan, terlebih dahulu memasukkan _import library_ untuk perintah fungsi dalam menjalankan permainan ini.

![pic 1](https://user-images.githubusercontent.com/89029568/130015157-35278052-2a72-4972-bcd7-26bc073528fb.png)

3. Cara menjalankan _snake game_
Cara menjalankan permainan ini dimulai memindahkan gerakan ularnya mengikuti pergerakan dijendela permainan dengan menggunakan perintah yang ada di kelas KEYDOWN di _pygame_. Event yang digunakan di sini adalah, K_UP, K_DOWN, K_LEFT, dan K_RIGHT untuk membuat ular bergerak ke atas, bawah, kiri dan kanan, seperti yang ditampilkan output dibawah ini:

![pygame berpindah 1](https://user-images.githubusercontent.com/89029568/130015470-8ec72a18-654e-4707-af36-c1d4513b4eb7.PNG)

![pygame berpindah 2](https://user-images.githubusercontent.com/89029568/130015578-edab5740-fecc-442b-9296-0bcd2aa1ba04.PNG)

![pic 2](https://user-images.githubusercontent.com/89029568/130015785-9224c3a3-af98-4ca1-99ad-0d3d6347d6b5.png)

Kemudian untuk pergerakan permainan ular ini mengikuti perpindahan letak makanan ularnya berada. Ketika ular melewati makanan itu akan mendapat pesan yang mengatakan "Yummy!!" dan diikuti dengan penambahan panjang ular saat memakan makanannya. Panjang ular pada dasarnya terkandung dalam daftar dan ukuran awal yang ditentukan dalam kode berikut adalah satu blok. Kemudian setelah ular berhasil melewati makanannya pertambahan panjang ular akan bertambah 1 dan juga akan menampilkan dibagian skornya sesuai dengan tampilan output dibawah ini: 

![pygame makan 1](https://user-images.githubusercontent.com/89029568/130016028-16d76928-8764-4973-a859-b1e2afe17e16.PNG)

![pygame makan 2](https://user-images.githubusercontent.com/89029568/130016066-a1764c9f-298c-4111-9ed4-bd52e59f155c.PNG)

![pic 3](https://user-images.githubusercontent.com/89029568/130016172-17a538e7-2e9f-4843-91aa-1d46823f33d0.png)

Dalam permainan ular ini, jika ular mencapai batas layar, maka kalah. Untuk menentukan ini, menggunakan pernyataan 'jika' yang mendefinisikan batas koordinat x dan y ular menjadi kurang dari atau sama dengan _layer_. 

Ketika permainan sudah kalah dan ingin melanjutkan permainannya kembali, dengan menggunakan perintah tekan tombol keyboard C untuk memulai kembali dan jika ingin keluar dari permainan ini dengan menekan tombol keyboard Q untuk keluar, seperti yang ditampilkan pada output dibawah ini: 

![pygame kalah 1](https://user-images.githubusercontent.com/89029568/130016319-7f0b1e2c-e530-4299-84ad-73737132bb96.PNG)

![pygame kalah 2](https://user-images.githubusercontent.com/89029568/130016370-59356c85-0c3c-4cbe-bf7d-c4dee07ccea6.PNG)

![pic 4](https://user-images.githubusercontent.com/89029568/130016514-896a0c1d-88dc-45b3-9c2a-9e2c3f030a9b.png)

![pic 5](https://user-images.githubusercontent.com/89029568/130016624-d526018d-e8ff-43dc-8b68-2e491e49f639.png)

Referensi permainan :

-	https://medium.com/edureka/snake-game-with-pygame-497f1683eeaa
-	https://www.edureka.co/blog/snake-game-with-pygame/

Referensi musik :
-	https://studio.youtube.com/channel/UCedSLyHpT3Cn7RAuq7tIZDw/music

