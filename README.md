# Docker

## Project Objective & Background
Salah satu tantangan sebagai calon Software & Data Engineer adalah bisa melakukan deployment project dengan baik. Objective dari projek ini adalah melakukan deployment terhadap sebuah aplikasi website yang sudah dibuat sebelumnya. Website yang telah dibuat sebelumnya akan dideploy menggunakan docker sebagai tools utama. Dalam pengerjaannya, akan terdapat fitur-fitur dan batasan yang perlu diikuti. Dalam pengerjaan projek ini, hasil/objektif akhir yang diharapkan adalah terbuatnya dua buah image (flask dan postgresql) dan docker compose yang akan membangun kedua image tersebut.

##  Create Dockerfile to Build Flask App Images
### Langkah Pertama
Membuat file didalam direktori flask. Dockerfile ini akan berisi serangkaian perintah yang diperlukan untuk membangun image.

![image](https://github.com/scofieId16/Linux-Container-Pacmann/blob/334035cd6623d1c431d7d233dca7e8a91dcc6eb9/pictures/docker.png)

### Langkah Kedua
Melakukan pull image. Anda perlu menentukan image yang akan digunakan atau diambil dari registry Docker Hub. Image ini akan menjadi dasar (base) untuk membangun image yang akan Anda buat.

![image](https://github.com/scofieId16/Linux-Container-Pacmann/blob/263ace3f2bd9518b06abe40519716acd46927cea/pictures/image.png)

### Langkah Ketiga
Melakukan copy data. Projek ini melakukan copy data dari './app' sehingga 'COPY . /app' akan menyalin semua file dan direktori yang ada dalam direktori saat ini (di mana Dockerfile berada) ke direktori /app di dalam container. 

![image](https://github.com/scofieId16/Linux-Container-Pacmann/blob/263ace3f2bd9518b06abe40519716acd46927cea/pictures/copy.png)

### Langkah Keempat
Menginstall requirements. Projek ini akan menginstall requirements yang terdaftar dalam 'requirements.txt'.

![image](https://github.com/scofieId16/Linux-Container-Pacmann/blob/263ace3f2bd9518b06abe40519716acd46927cea/pictures/req1.png)

![image](https://github.com/scofieId16/Linux-Container-Pacmann/blob/263ace3f2bd9518b06abe40519716acd46927cea/pictures/req2.png)

Berikut adalah penjelasan code pada gambar diatas: 
1. 'python -m' pip menjalankan perintah pip menggunakan interpreter Python yang terpasang di dalam container.
2. 'install' adalah perintah yang diberikan kepada pip untuk memulai proses instalasi.
3. '-r requirements.txt' memberikan argumen kepada pip untuk menginstal semua dependensi yang terdaftar dalam file requirements.txt. -r menunjukkan bahwa dependensi diambil dari file requirements.

### Langkah Kelima
Menyiapkan Command. CMD ["python", "run.py"] adalah perintah default dalam Dockerfile yang akan dijalankan saat container Docker berjalan. Perintah ini akan menjalankan skrip run.py menggunakan interpreter Python di dalam container.

![image](https://github.com/Alexander-2912/Docker/assets/118685091/42998db8-e39c-40a9-b510-821aeb4bac00)
