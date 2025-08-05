import json
import os
import math

def split_messages():
    # 读取原始文件
    with open('defaultMessages.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 创建default文件夹
    if not os.path.exists('default'):
        os.makedirs('default')
    
    # 计算需要多少个文件
    total_items = len(data)
    items_per_file = 50
    num_files = math.ceil(total_items / items_per_file)
    
    # 获取所有键
    keys = list(data.keys())
    
    # 分割并保存文件
    for i in range(num_files):
        start_idx = i * items_per_file
        end_idx = min((i + 1) * items_per_file, total_items)
        
        # 创建当前批次的字典
        current_batch = {key: data[key] for key in keys[start_idx:end_idx]}
        
        # 保存default文件
        default_filename = f'default/default_{i+1:02d}.json'
        with open(default_filename, 'w', encoding='utf-8') as f:
            json.dump(current_batch, f, ensure_ascii=False, indent=2)
        
        # 创建对应的zh文件
        zh_filename = f'default/zh_{i+1:02d}.json'
        with open(zh_filename, 'w', encoding='utf-8') as f:
            json.dump(current_batch, f, ensure_ascii=False, indent=2)
        
        print(f'Created {default_filename} and {zh_filename}')

if __name__ == '__main__':
    split_messages() 