# 🧠 Jimmi - AI-Ready Knowledge Base Manager

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Markdown](https://img.shields.io/badge/Markdown-Supported-black?style=flat-square&logo=markdown)
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

**连接个人知识与 AI 的桥梁**

[快速开始](#-快速开始) • [核心功能](#-核心功能) • [目录结构](#-目录结构) • [隐私配置](#-隐私与个性化)

</div>

---

## 📖 项目简介

**Jimmi** 是一个轻量级、基于 Markdown 的文本知识库管理工具。它通过 Python 脚本和 Git 流程，帮你将零散的笔记自动汇总，生成适合 AI（如 Google NotebookLM、Gemini）直接读取的语料格式。

其核心设计理念是 **"Write Locally, Chat AI-ly"** —— 你只需专注于本地写作，Jimmi 负责将其转化为 AI 的大脑。

## ✨ 核心功能

- **🤖 AI 友好型汇总**：自动扫描 `Docs` 下的子目录，将散落的 `.md` 文件聚合成单一的 `Jimmi.md`，专为投喂 NotebookLM 设计。
- **📂 自动分类管理**：程序自动识别目录结构作为知识分类，无需手动维护索引。
- **🔒 隐私与公共分离**：完美集成 `.gitignore`。你可以拥有一个公开的知识库，同时通过忽略特定目录，保留私有的 `index.md` 而不将其暴露在汇总文件中。
- **⚡ 零依赖**：基于 Python 标准库开发，无需安装繁重的 pip 包，开箱即用。

## 📂 目录结构

Jimmi 采用清晰的三层架构设计，默认包含以下分类（支持自定义）：

```text
/Jimmi
├── /Docs                   # 核心资料库
│   ├── /Knowledge          # 📘 知识：客观事实、教程、百科
│   │   ├── ...
│   │   └── index.md        # 自动生成：该目录的汇总
│   ├── /Practice           # 🛠️ 经验：项目实战、踩坑记录
│   │   ├── ...
│   │   └── index.md
│   └── /Thoughts           # 💡 思考：灵感、随笔、复盘
│       ├── ...
│       └── index.md
├── Jimmi.md                # 🚀 最终产物：全库汇总（Public）
├── update_index.py         # ⚙️ 核心脚本
├── .gitignore              # 🙈 隐私配置文件
└── requirements.txt        # 环境依赖（仅作占位，无额外依赖）

## 🚀 快速开始

1. **克隆仓库**

```bash
git clone https://github.com/Arshdelight/Jimmi.git
cd Jimmi
```

2. **填充内容**

在 /Docs 目录下创建你的分类文件夹，或直接使用默认的 Knowledge、Practice、Thoughts 目录，放入你的 Markdown 笔记。

3. **生成知识库**

运行根目录下的脚本：

```bash
python update_index.py
```

脚本执行逻辑：
- **扫描**：遍历 Docs 下所有子目录
- **生成索引**：在每个子目录根部生成 index.md（包含该目录下所有笔记全文）
- **全局汇总**：检查 .gitignore，跳过被忽略的目录，将剩余目录的 index.md 合并生成根目录下的 Jimmi.md

4. **投喂 AI**

将根目录生成的 Jimmi.md 直接上传至 NotebookLM 或发送给 Gemini，即可开启基于你个人知识库的问答。

## 🔒 隐私与个性化

Jimmi 允许你高度定制自己的知识库，同时保护隐私。

### 自定义分类

你不需要拘泥于默认的三个分类。任何在 /Docs 下创建的文件夹都会被脚本自动识别为一个新的"知识板块"。

### 隐私保护模式

如果你希望某些笔记（例如"个人日记"或"特定智能体的设定"）只在本地生成索引，而不包含在最终公开的 Jimmi.md 中：

1. 在 /Docs 下创建目录，例如 /Docs/PrivateDiary
2. 在 .gitignore 文件中添加该目录：

```text
Docs/PrivateDiary/
```

3. 运行 `python update_index.py`

**结果**：/Docs/PrivateDiary/index.md 依然会被生成（方便你单独使用），但其内容不会出现在根目录的 Jimmi.md 中。

## 🤝 贡献与反馈

如果你有新的想法或发现了 Bug，欢迎提交 Issue 或 Pull Request。让我们一起打造更高效的个人知识库工具！

<div align="center"> <sub>Built with ❤️ by Arshdelight</sub> </div>