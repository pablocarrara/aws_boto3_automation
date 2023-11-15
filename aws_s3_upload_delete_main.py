#Main para subir un archivo o borrarlo de AWS S3
#en aws_upload.py, aws_delete.py esta el codigo que debo importar

import boto3
import aws_s3_upload, aws_s3_delete




s3 = boto3.resource('s3')
file_name = 'joa_dia_tradicion.jpeg'
bucket_name = 'mypyscriptsforjoa'


print('''1- Subir archivo
2- Borrar archivo
3- Salir''')
print()



while True:
    option = int(input('Opcion: '))

    if option == 1:
        aws_upload.upload_file(s3, bucket_name, file_name)
    elif option == 2:
        aws_delete.delete_file(s3, bucket_name, file_name)
    elif option == 3:
        break
    else:
        option = int(input('Opcion invalida. Opcion: '))
