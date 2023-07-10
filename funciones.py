import os
import glob
from connect_db.conn import DAO

dao = DAO()

def data_detection(path_img, description):
    image = convert_to_binary(path_img)
    desc = description
    id_tipo = 1

    data = (image, desc, id_tipo)
    return data

def convert_to_binary(path):
    with open(path, 'rb') as file:
        blob = file.read()
    return blob

def validate_route():
    path = './runs/detect/'

    if os.path.exists(path):
        # print('Exist!')

        list_directory = os.listdir(path)
        list_directory.sort()
        print(list_directory)

        path_images = f'{path}{list_directory[-1]}/crops/Gun/'
        if os.path.exists(path_images):
            # print('Exist!!')

            list_images = glob.glob(path_images + '*.jpg')
            list_images.sort(key=os.path.getctime)
            print('\n'.join(list_images))

            last_img = list_images[-1]
            description = 'Gun Detected'
            data = data_detection(last_img, description)
            # print(data)
            dao.save_data(data)

# validate_route()