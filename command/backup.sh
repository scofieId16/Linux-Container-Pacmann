#!/bin/bash

NOW=$(date +"%y%m%d")

# Ganti path output sesuai dengan lokasi yang diinginkan di Windows
OUTPUT_PATH="/mnt/e/SEM 8/Work/Data Engineer/Pacmann SDE/Linux and Container/finalproject/postgres_backup/backup_${NOW}.sql"

/usr/bin/docker exec -t pgproject pg_dumpall -U postgres > "${OUTPUT_PATH}"

# Menambahkan pesan jika backup berhasil
if [ $? -eq 0 ]; then
  echo "Backup berhasil disimpan di: ${OUTPUT_PATH}"
else
  echo "Backup gagal."
fi