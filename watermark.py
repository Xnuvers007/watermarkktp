#!/usr/bin/env python3
#/usr/bin/python3
#/usr/bin/env python3
#!/usr/bin/python3

import os, sys, time #glob
from sys import platform
os.system("clear||cls")

try:
    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw
    import matplotlib.pyplot as plt
    #import numpy as np
except ModuleNotFoundError:
    if platform == "linux" or platform == "linux2":
        print("mohon untuk install PIL dan matplotlib untuk termux/linux")
        print('''
        1. Termux
        2. Linux
        ''')
        pilih = int(input("Pilih: "))
        if pilih == 1:
            os.system("pkg install python3")
            os.system("pip3 install --default-timeout=100 pillow")
            os.system("pip3 install --default-timeout=100 matplotlib")
            os.system("pkg install -y ndk-sysroot clang make libjpeg-turbo")
            os.system("pip3 install --upgrade pip setuptools wheel")
        elif pilih == 2:
            os.system("sudo apt install python3-pip")
            os.system("sudo pip3 install --default-timeout=100 pillow")
            os.system("sudo pip3 install --default-timeout=100 matplotlib")
        else:
            print("Pilihan tidak ada")
            sys.exit(1)
    elif platform == "win32":
        os.system("pip install --default-timeout=100 pillow")
        os.system("pip install --default-timeout=100 matplotlib")
    else:
        print("device tidak terdeteksi")
        sys.exit()

sys.setrecursionlimit(5000)
sys.getrecursionlimit()

# image = Image.open("tanjiro.jpg")
#image.show()
# plt.imshow(image)


########### CUSTOM FONTS DENGAN PYTHON3 DAN HEX COLORING ##################
def customfonts():
    print('''
        1. Termux
        2. Windows
        3. Linux
        ''')
    try:
        tanya = int(input("Apakah Kamu menggunakan Termux/Windows/Linux [1-2-3] : "))

        if tanya == 1:
            print("Kamu Menggunakan Termux")
            ter = str(input("apakah anda sudah mengetik command termux-setup-storage ? [Y/n] : "))
            if ter == 'Y' or ter == 'y':
                print("Saran , Jika ingin menggunakan Aplikasi/Program ini taruh gambar yang ingin di watermark ke dalam folder downloads/FILEGAMBARKAMU.jpg [jpg atau png, harus ada akhiran]")
                username = os.getlogin()
                print("Selamat datang {}".format(username))
                # try:
                #     os.system("mkdir storage/dcim/watermarktermux")
                # except FileExistsError:
                #     pass

                namafile = str(input("Masukkan Nama File : "))
                berkas = "storage/downloads/{}".format(namafile)
                letak = berkas
            elif ter == 'N' or ter == 'n':
                os.system("termux-setup-storage")
                print("Wajib , Jika ingin menggunakan Aplikasi/Program ini taruh gambar yang ingin di watermark ke dalam folder downloads/FILEGAMBARKAMU.jpg [jpg atau png, harus ada akhiran]")
                # try:
                #     os.system("mkdir storage/dcim/watermarktermux")
                # except FileExistsError:
                #     pass
                namafile = str(input("Masukkan Nama File : "))
                berkas = "storage/downloads/{}".format(namafile)
                letak = berkas
        elif tanya == 2:
            print("kamu menggunakan windows")
            username = os.getlogin()
            print("Wajib, jika ingin menggunakan Aplikasi ini, taruh gambar ini di folder C:/Users/{}/Pictures/Gambarkamu.jpg [jpg atau png, harus ada akhiran]".format(username))
            namafile = str(input("Masukan Nama File : "))
            berkas = "C:/Users/{}/Pictures/{}".format(username,namafile)
            letak = berkas
        elif tanya == 3:
            print("kamu menggunakan Linux")
            username = os.getlogin()
            print("Wajib, Jika ingin menggunakan Program ini, taruh gambar ini di /home/{}/Pictures/FILEGAMBARKAMU.jpg [jpg atau png, harus ada akhiran]".format(username))
            namafile = str(input("Masukan Nama File : "))
            berkas = "/home/{}/Pictures/{}".format(username,namafile)
            letak = berkas
        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    except (ValueError,KeyboardInterrupt):
        print("Inputan anda salah")
        sys.exit()
        
    try:
        watermark_image = Image.open(letak)
        draw = ImageDraw.Draw(watermark_image)
    except FileNotFoundError:
        if platform=="win32":
            path = "C:/Users/{}/Pictures/{}".format(username,namafile)
            name_path,extension = os.path.splitext(path)
            print("\nFile Tidak ada, harap periksa kembali")
            print("File berada di direktory : {}".format(name_path))
            print("File berekstensi : {}".format(extension))
            print("harap di periksa kembali")
            input("Enter to end")
            sys.exit(1)
        elif platform=="linux" or platform=="linux2":
            termx = str(input("apakah anda menggunakan Termux ? [y/N] : "))
            if termx=='Y' or termx=='y':
                path = "storage/downloads/{}".format(namafile)
                name_path,extension = os.path.splitext(path)
                print("\nFile tidak ada, harap periksa kembali")
                print("file berada di direktori : {}".format(name_path))
                print("File Berekstensi : {}".format(extension))
                print("harap di periksa kembali")
                input("enter to end")
                sys.exit(1)
            elif termx=='N' or termx=='n':
                path = "/home/{}/Pictures/{}".format(username,namafile)
                name_path,extension = os.path.splitext(path)
                print("\nFile tidak ada, harap periksa kembali")
                print("file berada di direktori : {}".format(name_path))
                print("File Berekstensi : {}".format(extension))
                print("harap di periksa kembali")
                input("enter to end")
                sys.exit(1)
            else:
                print("invalid option")
                sys.exit(1)
        else:
            print("cannot detect this operating system")
            sys.exit(1)
#    draw = ImageDraw.Draw(watermark_image)
    fon = int(input("Masukan Ukuran Font (40 , 30, 25, 13). Rekomendasi 30 : "))
    print("\n")
    # nil = 0
    # for x in os.listdir("./fonts"):
    #     nil += 1
    #     for i in range(x.find('fonts') + 1,len(x)):
    #         # i += 0
    #         if x.endswith(".ttf"):
    #             print(nil,x)         #nil adalah angka, x adalah nama file
    #             break
    #         else:
    #             pass
    if platform=="win32":
        print("Jika anda menggunakan Windows dan sudah mendownload fontsnya maka ada di folder C:/Users/{}/Downloads/(Nama fontsnya.ttf) disarankan menggunakan/format ttf".format(username))
    elif platform=="linux" or platform=="linux2":
        print("jika anda menggunakan termux dan sudah mendownload fontnya maka ada di folder storage/downloads/(nama fontsnya.ttf) disarankan menggunakan/format ttf")
        print("Jika anda menggunakan Linux dan sudah mendownload fontsnya maka ada di folder /home/{}/Downloads/(Nama fontsnya.ttf) disarankan menggunakan/format ttf".format(username))
    else:
        sys.exit(1)

    print("\n")
    tanyafont = str(input("Masukan / Letakan File Font yang kalian mau gunakan : "))
    font = ImageFont.truetype(tanyafont,fon)
    print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
    20/09/2022 untuk verifikasi peminjaman online\n''')
    masukan = str(input("Masukan Text Watermark : "))
    draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
    xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

    if xx=='Y' or xx=='y':
        watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
        print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
        term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

        if term=='Y' or term=='y':
            watermark_image.save("storage/downloads/{}".format(watermar))
            print("File Berhasil di simpan di storage/downloads/")
            print("Tekan Enter untuk keluar")
            input()
            sys.exit()

        elif term=='N' or term=='n':

            if platform=="win32":
                watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif platform=="linux" or platform=="linux2":
                watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif xx=='N' or xx=='n':
        warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
        warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
        print(warning,"\n",warn2)
        plt.subplot(1,2,2)
        plt.title("Images")
        watermark_image.show()
        plt.imshow(watermark_image)
        input("enter to exit")

    else:
        print("akan keluar dalam 3 detik")
        for i in range(1,4):
            i += 0
            time.sleep(0.5)
            print(i)
        sys.exit()


def defaultfonts():
    print('''
        1. Termux
        2. Windows
        3. Linux
        ''')
    try:
        tanya = int(input("Apakah Kamu menggunakan Termux/Windows/Linux [1-2-3] : "))

        if tanya == 1:
            print("Kamu Menggunakan Termux")
            ter = str(input("apakah anda sudah mengetik command termux-setup-storage ? [Y/n] : "))
            if ter == 'Y' or ter == 'y':
                print("Saran , Jika ingin menggunakan Aplikasi/Program ini taruh gambar yang ingin di watermark ke dalam folder downloads/FILEGAMBARKAMU.jpg [jpg atau png, harus ada akhiran]")
                username = os.getlogin()
                print("Selamat datang {}".format(username))
                # try:
                #     os.system("mkdir storage/dcim/watermarktermux")
                # except FileExistsError:
                #     pass
                namafile = str(input("Masukkan Nama File : "))
                berkas = "storage/downloads/{}".format(namafile)
                letak = berkas
            elif ter == 'N' or ter == 'n':
                os.system("termux-setup-storage")
                print("Wajib , Jika ingin menggunakan Aplikasi/Program ini taruh gambar yang ingin di watermark ke dalam folder downloads/FILEGAMBARKAMU.jpg [jpg atau png, harus ada akhiran]")
                # try:
                #     os.system("mkdir storage/dcim/watermarktermux")
                # except FileExistsError:
                #     pass
                namafile = str(input("Masukkan Nama File : "))
                berkas = "storage/downloads/{}".format(namafile)
                letak = berkas
        elif tanya == 2:
            print("kamu menggunakan windows")
            username = os.getlogin()
            print("Wajib, jika ingin menggunakan Aplikasi ini, taruh gambar ini di folder C:/Users/{}/Pictures/FILEGAMBARKAMU.jpg [jpg atau png, harus ada akhiran]".format(username))
            namafile = str(input("Masukan Nama File : "))
            berkas = "C:/Users/{}/Pictures/{}".format(username,namafile)
            letak = berkas
        elif tanya == 3:
            print("kamu menggunakan Linux")
            username = os.getlogin()
            print("Wajib, Jika ingin menggunakan Program ini, taruh gambar ini di /home/{}/Pictures/FILEGAMBARKAMU.jpg [jpg atau png, harus ada akhiran]".format(username))
            namafile = str(input("Masukan Nama File : "))
            berkas = "/home/{}/Pictures/{}".format(username,namafile)
            letak = berkas
        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    except (ValueError,KeyboardInterrupt):
        print("Inputan anda salah")
        sys.exit()

    try:
        watermark_image = Image.open(letak)
        draw = ImageDraw.Draw(watermark_image)
    except FileNotFoundError:
        if platform=="win32":
            path = "C:/Users/{}/Pictures/{}".format(username,namafile)
            name_path,extension = os.path.splitext(path)
            print("\nFile Tidak ada, harap periksa kembali")
            print("File berada di direktory : {}".format(name_path))
            print("File berekstensi : {}".format(extension))
            print("harap di periksa kembali")
            input("Enter to end")
            sys.exit(1)
        elif platform=="linux" or platform=="linux2":
            termx = str(input("apakah anda menggunakan Termux ? [y/N] : "))
            if termx=='Y' or termx=='y':
                path = "storage/downloads/{}".format(namafile)
                name_path,extension = os.path.splitext(path)
                print("\nFile tidak ada, harap periksa kembali")
                print("file berada di direktori : {}".format(name_path))
                print("File Berekstensi : {}".format(extension))
                print("harap di periksa kembali")
                input("enter to end")
                sys.exit(1)
            elif termx=='N' or termx=='n':
                path = "/home/{}/Pictures/{}".format(username,namafile)
                name_path,extension = os.path.splitext(path)
                print("\nFile tidak ada, harap periksa kembali")
                print("file berada di direktori : {}".format(name_path))
                print("File Berekstensi : {}".format(extension))
                print("harap di periksa kembali")
                input("enter to end")
                sys.exit(1)
            else:
                print("invalid option")
                sys.exit(1)
        else:
            print("cannot detect this operating system")
            sys.exit(1)
    #font = ImageFont.load_default()
    fon = int(input("Masukan Ukuran Font (40 , 30, 25, 13). Rekomendasi 30 : "))
    print("\n")
    # dir_path = r'./fonts/*.ttf'
    # for file in glob.glob(dir_path):
    #     print(file)
    nil = 0
    for x in os.listdir("./fonts"):
        nil += 1
        for i in range(x.find('fonts') + 1,len(x)):
            # i += 0
            if x.endswith(".ttf"):
                print(nil,x)         #nil adalah angka, x adalah nama file
                break
            else:
                pass

    tanyafont = int(input("\nMasukan Font yang kalian ingin gunakan, sesuai dengan nomornya : "))

    if tanyafont==1:
        font = ImageFont.truetype("./fonts/Yaahowu-Thick-Italic.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("Enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==2:
        font = ImageFont.truetype("./fonts/Yaahowu-Italic.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==3:
        font = ImageFont.truetype("./fonts/comic.ttf",fon)
        masukan = str(input("Masukan Text Watermark : "))
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==4:
        font = ImageFont.truetype("./fonts/Yaahowu-Light.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==5:
        font = ImageFont.truetype("./fonts/Fira-Code-Light-300.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==6:
        font = ImageFont.truetype("./fonts/Yaahowu-Thick.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==7:
        font = ImageFont.truetype("./fonts/Futuram.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==8:
        font = ImageFont.truetype("./fonts/Yaahowu-Bold-Italic.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==9:
        font = ImageFont.truetype("./fonts/Yagora.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==10:
        font = ImageFont.truetype("./fonts/AmaticSC-Regular.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==11:
        font = ImageFont.truetype("./fonts/Yaahowu.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==12:
        font = ImageFont.truetype("./fonts/Cascadia.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==13:
        font = ImageFont.truetype("./fonts/Amatic-Bold.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==14:
        font = ImageFont.truetype("./fonts/Yaahowu-Light-Italic.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==15:
        font = ImageFont.truetype("./fonts/Fira-Code-Medium-500.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==16:
        font = ImageFont.truetype("./fonts/Fira-Code-Retina-450.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==17:
        font = ImageFont.truetype("./fonts/Yaahowu-Bold.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==18:
        font = ImageFont.truetype("./fonts/Fira-Code-Regular-400.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==19:
        font = ImageFont.truetype("./fonts/Fira-Code-Bold-700.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

    elif tanyafont==20:
        font = ImageFont.truetype("./fonts/UniversCondensed.ttf",fon)
        print('''\nContoh Watermark : 13/8/2022 untuk verifikasi Tokopedia
        20/09/2022 untuk verifikasi peminjaman online\n''')
        masukan = str(input("Masukan Text Watermark : "))
        draw.text((30, 380), masukan, (kode1, kode2, kode3), font=font)
        xx = str(input("Ingin Di Simpan atau dilihat dulu/tidak [Y/n] : "))

        if xx=='Y' or xx=='y':
            watermar = str(input("Masukan Nama file yang ingin di simpan (dengan jpg/png) : "))
            print("jika pilihannya N, maka akan otomatis mengarah ke windows / linux, akan terdeteksi sendiri , user menggunakan apa...")
            term = str(input("apakah anda menggunakan termux ? [Y/n] : "))

            if term=='Y' or term=='y':
                watermark_image.save("storage/downloads/{}".format(watermar))
                print("File Berhasil di simpan di storage/downloads/")
                print("Tekan Enter untuk keluar")
                input()
                sys.exit()

            elif term=='N' or term=='n':

                if platform=="win32":
                    watermark_image.save("C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di C:/Users/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

                elif platform=="linux" or platform=="linux2":
                    watermark_image.save("/home/{}/Pictures/{}".format(username,watermar))
                    print("File Berhasil di simpan di /home/{}/Pictures/{}".format(username,watermar))
                    print("Tekan Enter untuk keluar")
                    input()
                    sys.exit()

            else:
                print("akan keluar dalam 3 detik")
                for i in range(1,4):
                    i += 0
                    time.sleep(0.5)
                    print(i)
                sys.exit()

        elif xx=='N' or xx=='n':
            warning = "perhatian , matplotlib termux tidak support untuk melihat gambar".upper()
            warn2 = "jika gambar tidak muncul, jalankan sekali lagi".upper()
            print(warning,"\n",warn2)
            plt.subplot(1,2,2)
            plt.title("Images")
            watermark_image.show()
            plt.imshow(watermark_image)
            input("enter to end")

        else:
            print("akan keluar dalam 3 detik")
            for i in range(1,4):
                i += 0
                time.sleep(0.5)
                print(i)
            sys.exit()

def pydroid3():
    os.system("pip3 install --default-timeout=100 matplotlib")
    os.system("pip3 install --default-timeout=100 pillow")
    #os.system("pip3 install --default-timeout=100 numpy")
    username = os.getlogin()
    print("selamat datang {}".format(username))
    

print('''
    [+] Author : Xnuvers007
    [+] Github : Xnuvers007
    [+] Instagram : Indradwi.25
    [+] Youtube : Xnuvers007
    [+] Website : https://mykingbee.blogspot.com
    [+] License : GPL-3.0 license
    [+] Donate : https://saweria.co/xnuvers007
    [+] Donate 2 : https://trakteer.id/Xnuvers007
''')
print('''
    1. Custom Fonts
    2. Default Fonts

    ingin menggunakan metode yang mana ? [1/2]
    \n
''')
menu = int(input("Pilih : "))

print('''
    jika malas liat di color.txt
    bisa liat list ini (hanya menampilkan warna dasar)

    1. Biru = 0,0,255
    2. Merah = 255,0,0
    3. Kuning = 255,255,0
    4. Hijau = 0,128,0

    ''')
print("Pilih kode warna yang ingin kalian mau, bisa diihat di color.txt")
print("\n")
kode1 = int(input("Masukan Kode Pertama 0-255 : "))
kode2 = int(input("Masukan kode Kedua 0-255 : "))
kode3 = int(input("Masukan Kode Ketiga 0-255 : "))

if menu==1:
    customfonts()
elif menu==2:
    defaultfonts()
else:
    print("akan keluar dalam 3 detik")
    for i in range(1,4):
        i += 0
        time.sleep(0.5)
        print(i)
    sys.exit()


# font = ImageFont.truetype('./fonts/comic.ttf', fon)
# draw.text((30, 380), "loli ini", (255, 255, 255), font=font)
# plt.subplot(1,2,2)
# plt.title("putih")
# watermark_image.show()
# plt.imshow(watermark_image)
# watermark_image.save("watermarked.jpg")
