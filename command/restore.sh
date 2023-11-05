#!/bin/bash

# Tentukan path file backup
BACKUP_FILE="/mnt/e/SEM 8/Work/Data Engineer/Pacmann SDE/Linux and Container/finalproject/postgres_backup/backup_${NOW}.sql"

# Tentukan nama database yang akan di-restore
DB_NAME="pgproject"

# Eksekusi perintah restore menggunakan Docker
/usr/bin/docker exec -i pgproject psql -U postgres -d pgproject < "$1"

# Periksa apakah restore berhasil atau gagal
if [ $? -eq 0 ]; then
  echo "Restore berhasil."
else
  echo "Restore gagal."
fi