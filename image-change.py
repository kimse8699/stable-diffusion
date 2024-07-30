import os
from PIL import Image

# 이미지와 JSON 파일이 있는 디렉토리 경로
directory = r"C:\Users\ehowl\OneDrive\문서\dataset"

# 디렉토리 내의 모든 파일 리스트 가져오기
files = os.listdir(directory)

# 이미지 파일과 JSON 파일을 분류
image_files = [f for f in files if f.endswith(('.png', '.jpg', '.jpeg'))]
json_files = [f for f in files if f.endswith('.json')]

# 이미지 파일 처리
for image_file in image_files:
    image_path = os.path.join(directory, image_file)
    json_path = os.path.join(directory, os.path.splitext(image_file)[0] + '.json')
    
    try:
        with Image.open(image_path) as img:
            # 이미지 크기를 512x512로 변경
            img = img.resize((512, 512))
            img.save(image_path)
            print(f'Resized and saved: {image_file}')
    except Exception as e:
        # 에러가 발생하면 이미지 파일과 해당 JSON 파일 삭제
        print(f'Error processing {image_file}: {e}')
        if os.path.exists(image_path):
            os.remove(image_path)
            print(f'Deleted: {image_file}')
        if os.path.exists(json_path):
            os.remove(json_path)
            print(f'Deleted: {json_path}')
