#Hago el upload del archivo, usando el contenido binario del archivo



def upload_file(s3, bucket_name, file_name):

    with open(file_name, 'rb') as data:
        s3.Bucket(bucket_name).put_object(Key= file_name, Body = data) #este file name es el nombre que va
        #tener en el bucket


    #valido que el archivo subio al bucket correspondiente
    my_bucket = s3.Bucket(bucket_name)
    object_exists = any(obj.key == file_name for obj in my_bucket.objects.all())


    if object_exists:
        print(f'file {file_name} uploaded successfully')
    else:
        print(f'file {file_name} could not be uploaded')
    



