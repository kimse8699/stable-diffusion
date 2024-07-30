import os

# 이미지와 JSON 파일이 있는 디렉토리 경로
directory = r"C:\Users\ehowl\OneDrive\문서\dataset"

# 디렉토리 내의 모든 파일 리스트 가져오기
files = os.listdir(directory)

# 이미지 파일과 JSON 파일을 분류
image_files = [f for f in files if f.endswith(('.png', '.jpg', '.jpeg'))]
json_files = [f for f in files if f.endswith('.json')]

# 이미지 파일 이름에서 확장자를 제거한 세트
image_names = set(os.path.splitext(f)[0] for f in image_files)
# JSON 파일 이름에서 확장자를 제거한 세트
json_names = set(os.path.splitext(f)[0] for f in json_files)

# 두 세트가 일치하는지 확인
if image_names == json_names:
    print("이미지 파일과 JSON 파일의 수가 일치합니다.")
    print(len(image_names))
else:
    print("이미지 파일과 JSON 파일의 수가 일치하지 않습니다.")
    # 일치하지 않는 파일을 출력
    missing_images = json_names - image_names
    missing_jsons = image_names - json_names

    if missing_images:
        print("다음 이미지 파일이 누락되었습니다:", missing_images)
    if missing_jsons:
        print("다음 JSON 파일이 누락되었습니다:", missing_jsons)
