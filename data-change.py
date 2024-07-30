import os
import json
import shutil

# 이미지와 JSON 파일이 있는 디렉토리 경로
directory = r"C:\Users\ehowl\OneDrive\문서\dataset"
output_file = r"C:\Users\ehowl\OneDrive\문서\dataset\metadata.jsonl"

# 디렉토리 내의 모든 파일 리스트 가져오기
files = os.listdir(directory)

# JSON 파일을 분류
json_files = [f for f in files if f.endswith('.json')]

# JSONL 파일 작성
with open(output_file, 'w', encoding='utf-8-sig') as outfile:
    for idx, json_file in enumerate(json_files):
        json_path = os.path.join(directory, json_file)
        try:
            with open(json_path, 'r', encoding='utf-8-sig') as infile:
                data = json.load(infile)
                # imageInfo 리스트의 첫 번째 항목 추출
                if 'imageInfo' in data and len(data['imageInfo']) > 0:
                    image_info = data['imageInfo'][0]
                    original_file_name = image_info.get('srcImageFile', '')
                    text = image_info.get('srcText', '')
                    
                    # 새로운 파일 이름 생성
                    new_file_name = f"{idx + 1:04}.jpg"
                    original_image_path = os.path.join(directory, original_file_name)
                    new_image_path = os.path.join(directory, new_file_name)

                    # 이미지 파일 이름 변경
                    if os.path.exists(original_image_path):
                        shutil.move(original_image_path, new_image_path)
                    
                    # JSONL 형식으로 작성
                    output_data = {
                        "file_name": new_file_name,
                        "text": text
                    }
                    outfile.write(json.dumps(output_data, ensure_ascii=False) + '\n')
                    print(f'Processed: {json_file} -> {new_file_name}')
                else:
                    print(f'No imageInfo found in {json_file}')
        except Exception as e:
            print(f'Error processing {json_file}: {e}')

print(f'All data has been written to {output_file}')
