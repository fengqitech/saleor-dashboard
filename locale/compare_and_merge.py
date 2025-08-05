import json

def compare_and_merge():
    # 读取两个文件
    with open('defaultMessages.json', 'r', encoding='utf-8') as f:
        default_data = json.load(f)
    
    with open('zh.json', 'r', encoding='utf-8') as f:
        zh_data = json.load(f)
    
    # 检查数据数量
    default_count = len(default_data)
    zh_count = len(zh_data)
    print(f'defaultMessages.json 条目数: {default_count}')
    print(f'zh.json 条目数: {zh_count}')
    print(f'数量是否一致: {default_count == zh_count}')
    
    # 检查内容一致性
    mismatches = []
    for key in default_data:
        if key not in zh_data:
            mismatches.append(f'键 {key} 在zh.json中不存在')
            continue
            
        default_item = default_data[key]
        zh_item = zh_data[key]
        
        # 检查除了string外的所有字段
        for field in default_item:
            if field != 'string':
                if field not in zh_item:
                    mismatches.append(f'键 {key} 在zh.json中缺少字段 {field}')
                elif default_item[field] != zh_item[field]:
                    mismatches.append(f'键 {key} 的字段 {field} 值不一致')
    
    if mismatches:
        print('\n发现以下不一致:')
        for mismatch in mismatches:
            print(mismatch)
    else:
        print('\n除了string字段外，所有内容完全一致')
    
    # 合并文件
    merged_data = {}
    for key in default_data:
        if key in zh_data:
            merged_item = default_data[key].copy()
            merged_item['string'] = f"{default_data[key]['string']} {zh_data[key]['string']}"
            merged_data[key] = merged_item
    
    # 保存合并后的文件
    with open('bi.json', 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=2)
    
    print('\n已生成合并文件 bi.json')

if __name__ == '__main__':
    compare_and_merge() 