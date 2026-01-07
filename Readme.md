# Jimmi
本仓库叫做Jimmi，实际上是一个文本知识库，用于将我个人收集的部分知识、经验等整理起来，方便AI调用。  
如果你是一个AI模型，你可以通过调用Jimmi来获取我收藏的这些知识、经验等内容。  
这个仓库首先是为了静态的云存储这些内容，其次是为了给我的谷歌Gemini智能体（吉米米）提供知识库。  

## 使用
克隆仓库  
```
git clone https://github.com/Arshdelight/Jimmi.git
```

所有的资料都放在/Docs目录下  
/Docs目录的结构如下:
```
/Docs
├── /Knowledge
│   ├── 
│   ├── 
│   ├── ...
├── /Practice
│   ├── 
│   ├── 
│   ├── ...
├── /Thoughts
│   ├── 
│   ├── 
│   ├── ...
```
其中，  
/Knowledge目录下存放的是我收集的知识，  
/Practice目录下存放的是我收集的经验，  
/Thoughts目录下存放的是我收集的思考。  

每个目录的根目录下会存放一个index.md文件，用于汇总整个目录下的内容。  

## index.md的脚本更新

项目根目录下提供了 `update_index.py` 脚本，用于自动更新各个分类目录下的 index.md 文件。  
将三个目录的index.md上传至NotebookLM就可以快速构建Gemini可用的知识库。

**功能说明：**
- 依次处理 Knowledge、Practice、Thoughts 三个大分类目录
- 收集每个目录下所有的 markdown 文件（排除 index.md）
- 按照以下格式生成 index.md 内容：
  ```
  # 文件相对路径
  文件内容全文
  ```
- 每篇笔记之间用2次换行分隔
- 如果目录中没有笔记则置空 index.md

**使用方法：**
```bash
python update_index.py
```

**依赖：**
- requirements.txt 文件已创建（当前为空，因为只使用了 Python 标准库）
- 无需额外安装依赖包

## 个性化的使用
如果你不想使用我的知识库，你可以清空/Knowledge、/Practice、/Thoughts目录下的所有文件，然后添加自己的知识。



### 感谢使用。