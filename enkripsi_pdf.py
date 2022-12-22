from PyPDF2 import PdfWriter, PdfReader
  
# buat objek pdf writer
out = PdfWriter()
  
# buka file pdf asli 
file = PdfReader("D:/Enkripsi_RSA/IMK Pertemuan 4.pdf")
  
# identifikasi total halaman file
num = file.numPages
  
#program membaca setiap halaman file sesuai halaman yg diidentifikasi 
for page in file.pages:
    # tambahkan halaman ke objek pdf writer
    out.add_page(page)
  
  
# masukkan password enkripsi 
password = "najwa"
  
# enkripsi masing-masing halaman 
out.encrypt(password)
  
# buka file enkripsi "myfile_encrypted.pdf"
with open("D:/Enkripsi_RSA/enkripsi.pdf", "wb") as f:
    
    # simpan pdf 
    out.write(f)
