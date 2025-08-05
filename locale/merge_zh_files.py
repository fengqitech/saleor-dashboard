import json
import os
import glob

def merge_zh_files():
    # 获取所有zh_xx.json文件并按数字排序
    zh_files = glob.glob('default/zh_*.json')
    zh_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))
    
    # 创建合并后的字典
    merged_data = {}
    
    # 按顺序读取并合并每个文件
    for file_path in zh_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            merged_data.update(data)
    
    # 将合并后的数据写入zh.json
    with open('zh.json', 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)
    
    print(f'Successfully merged {len(zh_files)} files into zh.json')

if __name__ == '__main__':
    merge_zh_files() 