import os
import glob

def validate_route():
    path = './runs/detect/'

    if os.path.exists(path):
        print('Exist!')

        list_directory = os.listdir(path)
        list_directory.sort()
        print(list_directory)

        path_images = f'{path}{list_directory[-1]}/crops/Gun/'
        if os.path.exists(path_images):
            # print('Exist!!')

            list_images = glob.glob(path_images + '*.jpg')
            list_images.sort(key=os.path.getctime)
            print('\n'.join(list_images))

# validate_route()