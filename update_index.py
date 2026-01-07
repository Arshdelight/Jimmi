import os
from pathlib import Path


def collect_markdown_files(directory):
    """收集目录下所有的markdown文件，排除index.md"""
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') and file != 'index.md':
                full_path = os.path.join(root, file)
                md_files.append(full_path)
    return sorted(md_files)


def read_file_content(file_path):
    """读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"读取文件 {file_path} 失败: {e}")
        return ""


def generate_index_content(md_files, base_dir):
    """生成index.md的内容"""
    content_parts = []
    
    for md_file in md_files:
        relative_path = os.path.relpath(md_file, base_dir)
        file_content = read_file_content(md_file)
        
        entry = f"# {relative_path}\n{file_content}"
        content_parts.append(entry)
    
    return "\n\n".join(content_parts)


def process_category(category_name):
    """处理单个分类目录"""
    base_dir = Path(__file__).parent / 'Docs' / category_name
    index_file = base_dir / 'index.md'
    
    if not base_dir.exists():
        print(f"目录不存在: {base_dir}")
        return
    
    print(f"正在处理 {category_name} 目录...")
    
    md_files = collect_markdown_files(str(base_dir))
    
    if not md_files:
        print(f"  {category_name} 目录下没有markdown笔记")
        content = ""
    else:
        print(f"  找到 {len(md_files)} 个markdown文件")
        content = generate_index_content(md_files, str(base_dir))
    
    try:
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  已更新 {index_file}")
    except Exception as e:
        print(f"  写入 {index_file} 失败: {e}")


def main():
    """主函数"""
    categories = ['Knowledge', 'Practice', 'Thoughts']
    
    print("开始更新index.md文件...")
    print("=" * 50)
    
    for category in categories:
        process_category(category)
        print()
    
    print("=" * 50)
    print("更新完成！")


if __name__ == '__main__':
    main()
