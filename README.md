# DeepSeek Gradio Chat

一个基于 Python、DeepSeek API 和 Gradio 构建的AI多轮对话应用。

这是我学习 AI Agent 开发过程中的第一个完整项目，主要用于学习和实践：
Python 调用大模型 API、对话上下文管理以及 Gradio Web 界面的构建。

## 功能

- 调用 DeepSeek API 与大语言模型进行对话
- 使用 Gradio 构建 Web 聊天界面
- 支持多轮对话上下文
- 使用环境变量管理 API Key
- 支持生成 Gradio 临时公网链接

## 技术栈

- Python 3.10
- DeepSeek API
- OpenAI Python SDK
- Gradio

## 项目结构

```text
demo1/
├── chat.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 安装依赖

克隆项目后安装所需 Python 库：

```bash
pip install -r requirements.txt
```

## 配置 API Key

本项目不会在代码中保存 API Key。

运行前需要设置环境变量：

```bash
export DEEPSEEK_API_KEY="your_api_key"
```

## 运行项目

```bash
python chat.py
```

运行成功后，Gradio 会生成本地访问地址。

如果代码中使用：

```python
demo.launch(share=True)
```

还会生成临时公网分享链接。

## 学习内容

通过这个项目，我主要实践了：

1. 使用 Python SDK 调用大模型 API
2. 理解 API Key、base_url、model 和 messages
3. 使用函数封装大模型调用
4. 使用 Gradio 构建简单的 AI 应用界面
5. 将历史对话重新组织为 messages，实现多轮上下文
6. 使用环境变量避免 API Key 泄露

## 后续计划

- 增加异常处理
- 优化多轮对话管理
- 学习 Function Calling / Tool Calling
- 在当前项目基础上进一步实现具有工具调用能力的 AI Agent