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

### Langkah Kelima
Menyiapkan Command. CMD ["python", "app.py"] adalah perintah default dalam Dockerfile yang akan dijalankan saat container Docker berjalan. Perintah ini akan menjalankan skrip app.py menggunakan interpreter Python di dalam container.

![image](https://github.com/scofieId16/Linux-Container-Pacmann/blob/263ace3f2bd9518b06abe40519716acd46927cea/pictures/command.png)

### Langkah Keenam
Memastikan apakah flask sudah berjalan. Hal ini bisa dilakukan dengan menjalankan localhost:5000 pada browser, apabila website terbuka tanpa error, maka flask sudah berhasil dijalankan.

![image](https://github.com/scofieId16/Linux-Container-Pacmann/blob/263ace3f2bd9518b06abe40519716acd46927cea/pictures/web1.png)

## Setup Postgresql Images
### Langkah Pertama
Mengambil (Pull) images. Image yang akan digunakan akan dipilih dan diambil dari registry Docker Hub. Projek ini menggunakan image versi terbaru

![image](https://github.com/scofieId16/Linux-Container-Pacmann/blob/747daf95e664d157a09096cb9d902467a3c1a4c5/pictures/image%20pg.png)

### Langkah Kedua
Membuat container. Berikut command yang digunakan untuk membuat container:
```
docker run -d -p 5432:5432 --name pg-container --network my-network -v postgres-volume:/var/lib/postgresql/data pg-img:1.0
```

![image](https://github.com/scofieId16/Linux-Container-Pacmann/blob/5c12f447119c39022d8ba7d38d563c8560fdcc3b/pictures/dockercontainer.png)

### Langkah Ketiga
Mengecek apakah postgresql sudah berjalan. Hal ini bisa dilakukan dengan melakukan koneksi ke postgresql melalui DBeaver. Masukkan database, username, dan password sesuai yang dibuat sebelumnya. 

![image](https://github.com/scofieId16/Linux-Container-Pacmann/blob/5c12f447119c39022d8ba7d38d563c8560fdcc3b/pictures/dbeaver1.png)

## Create Docker-Compose To Create And Run Services and Volumes
Langkah selanjutnya adalah membuat docker compose untuk flask dan postgresql. Perintah dilakukan pada file 'docker-compose.yml'.
```
version: '3'

services:
  flask:
    build:
      context: ./Flask
      dockerfile: Dockerfile
    container_name: flaskproject
    ports:
      - 5000:5000
    networks:
      - app-networks

  postgres:
    build:
      context: ./Postgres
      dockerfile: Dockerfile
    hostname: postgres
    container_name: pgproject
    ports:
      - 5433:5432
    volumes:
      - postgres-volumes:/var/lib/postgresql/data
    networks:
      app-networks:
        ipv4_address: 172.25.0.3

volumes:
  postgres-volumes:
    driver: local

networks:
  app-networks:
    driver: bridge
    ipam:
      config:
        - subnet: 172.25.0.0/24
```
Code tersebut adalah sebuah konfigurasi Docker Compose yang digunakan untuk membuat dan mengatur lingkungan pengembangan lokal yang terdiri dari dua layanan: postgres dan flask-app.

Setelah membuat konfigurasi terhadap docker compose, maka selanjutnya docker compose akan dibuild dengan command 'docker compose up -d' pada terminal. Apabila sudah selesai, maka akan muncul docker compose pada docker desktop, seperti pada gambar dibawah:

![image](https://github.com/scofieId16/Linux-Container-Pacmann/blob/5c12f447119c39022d8ba7d38d563c8560fdcc3b/pictures/dockercompose.png)

Kemudian, bisa di cek lagi koneksi database dan flasknya seperti yang dilakukan sebelumnya

![image](https://github.com/scofieId16/Linux-Container-Pacmann/blob/5c12f447119c39022d8ba7d38d563c8560fdcc3b/pictures/web1.png)

![image](https://github.com/scofieId16/Linux-Container-Pacmann/blob/5c12f447119c39022d8ba7d38d563c8560fdcc3b/pictures/web2.png)

![image](https://github.com/scofieId16/Linux-Container-Pacmann/blob/5c12f447119c39022d8ba7d38d563c8560fdcc3b/pictures/dbeaver1.png)

![image](https://github.com/scofieId16/Linux-Container-Pacmann/blob/5c12f447119c39022d8ba7d38d563c8560fdcc3b/pictures/dbeaver2.png)



