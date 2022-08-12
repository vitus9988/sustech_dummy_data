import random
import json
import os
from faker import Faker
import glob
from module import make_obj
import concurrent.futures
import time


# 인자로 받은 수 만큼 무작위 이름으로 된 폴더 생성 (label 폴더 이하)
def make_folder(labeler: int) -> bool:
    count = 0
    fake = Faker("ko-KR")
    while labeler:
        if len(glob.glob("./label/*")) > labeler-1:
            break
        labeler_name = fake.name()
        try:
            os.makedirs(f"./label/{labeler_name}")
        except FileExistsError:
            print("해당 경로에 이미 존재하는 폴더")
            return False
        count += 1
        if count == labeler:
            break
    return True


# 인자로 받은 수 만큼 무작위 json 파일 생성 (label/이름 폴더 이하)
def make_json(path):
    file = 100
    for i in range(1, file+1):
        filenum = random.randint(10,10000)
        with open(f'{path}/1555{filenum}9869.json', 'w') as f:
            dataset = [make_obj() for x in range(random.randint(100, 300))]
            json.dump(dataset, f, indent="\t")


if __name__ == '__main__':
    make_folder(labeler=30)
    namepath = './label/*'
    namelist = glob.glob(namepath)
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        executor.map(make_json, namelist)
    print(time.time()-start)
