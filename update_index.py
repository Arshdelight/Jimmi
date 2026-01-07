import os
import sys
from pathlib import Path


def get_base_path():
    """获取程序的基础路径，兼容打包后的 exe 和普通 Python 脚本"""
    if getattr(sys, 'frozen', False):
        # 如果是打包后的 exe，使用 exe 所在目录
        return Path(sys.executable).parent
    else:
        # 如果是普通 Python 脚本，使用脚本所在目录
        return Path(__file__).parent


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
    base_dir = get_base_path() / 'Docs' / category_name
    index_file = base_dir / 'index.md'
    
    if not base_dir.exists():
        print(f"目录不存在: {base_dir}")
        return None
    
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
        return content
    except Exception as e:
        print(f"  写入 {index_file} 失败: {e}")
        return None


def read_gitignore():
    """读取 .gitignore 文件，返回需要忽略的目录列表"""
    gitignore_file = get_base_path() / '.gitignore'
    ignored_dirs = []
    
    if not gitignore_file.exists():
        return ignored_dirs
    
    try:
        with open(gitignore_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if line.startswith('Docs/'):
                        dir_name = line[5:].strip('/')
                        if dir_name:
                            ignored_dirs.append(dir_name)
    except Exception as e:
        print(f"读取 .gitignore 失败: {e}")
    
    return ignored_dirs


def generate_jimmi_md(categories):
    """生成根目录下的 Jimmi.md 文件"""
    print("正在生成 Jimmi.md...")
    
    ignored_dirs = read_gitignore()
    if ignored_dirs:
        print(f"  忽略的目录: {', '.join(ignored_dirs)}")
    
    content_parts = []
    
    for category in categories:
        if category in ignored_dirs:
            print(f"  跳过 {category} 目录（在 .gitignore 中）")
            continue
        
        index_file = get_base_path() / 'Docs' / category / 'index.md'
        if index_file.exists():
            index_content = read_file_content(str(index_file))
            content_parts.append(f"【{category}】\n{index_content}")
        else:
            print(f"  警告: {category}/index.md 不存在")
    
    jimmi_content = "\n\n".join(content_parts)
    
    jimmi_file = get_base_path() / 'Jimmi.md'
    try:
        with open(jimmi_file, 'w', encoding='utf-8') as f:
            f.write(jimmi_content)
        print(f"  已生成 {jimmi_file}")
    except Exception as e:
        print(f"  写入 {jimmi_file} 失败: {e}")


def get_all_categories():
    """获取 Docs 目录下的所有分类目录"""
    docs_dir = get_base_path() / 'Docs'
    if not docs_dir.exists():
        print(f"Docs 目录不存在: {docs_dir}")
        return []
    
    categories = []
    for item in docs_dir.iterdir():
        if item.is_dir():
            categories.append(item.name)
    
    return sorted(categories)


def main():
    """主函数"""
    categories = get_all_categories()
    
    if not categories:
        print("未找到任何分类目录")
        return
    
    print(f"找到 {len(categories)} 个分类目录: {', '.join(categories)}")
    print("开始更新index.md文件...")
    print("=" * 50)
    
    for category in categories:
        process_category(category)
        print()
    
    print("=" * 50)
    
    generate_jimmi_md(categories)
    
    print("=" * 50)
    print("更新完成！")


if __name__ == '__main__':
    main()
