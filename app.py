import requests
import subprocess

def download_and_run_bash_script(url, local_filename):
    # Mendownload file dari URL
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_filename, 'wb') as file:
            file.write(response.content)
        print(f"File berhasil diunduh: {local_filename}")

        # Menjalankan file bash
        process = subprocess.Popen(["bash", local_filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            print(f"Ada kesalahan: {stderr.decode()}")
        else:
            print(f"Output dari skrip: {stdout.decode()}")
    else:
        print(f"Gagal mengunduh file: {response.status_code}")

# Ganti URL dan nama file lokal sesuai dengan kebutuhan Anda
download_and_run_bash_script('https://try.gitea.io/mustofa/shc/src/branch/master/boled03.sh', 'boled03.sh')
