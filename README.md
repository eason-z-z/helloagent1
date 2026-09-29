# HelloAgent 学习项目

这是一个用于学习大语言模型与 AI Agent 基础原理的 Python 练习仓库。项目包含 OpenAI 兼容接口封装、ReAct、Plan-and-Solve、Reflection、工具调用、多智能体协作，以及词向量、N-gram 和 Transformer 等基础示例。

> 本仓库以学习和实验为目的，部分脚本是独立示例，并非一个统一部署的应用。

## 项目内容

```text
helloagent/
├── ch4/
│   ├── helloagentllm.py       # OpenAI 兼容的 LLM 客户端（当前用于 DeepSeek）
│   ├── React.py               # ReAct 智能体
│   ├── plansolve.py           # Plan-and-Solve 智能体
│   ├── reflection.py          # Reflection 反思与迭代优化
│   ├── toolregister.py        # 简单的工具注册与调用机制
│   ├── search.py              # 搜索工具示例
│   ├── autogen/               # AutoGen 多智能体软件团队示例
│   └── autoscope/             # AgentScope 三国狼人杀多智能体示例
├── n_gram/                    # N-gram、词向量与 Transformer 原理练习
├── qw/                        # 本地加载 Qwen 模型的示例
└── tool_testfile/             # 天气、旅游搜索和函数调用练习
```

## 环境要求

- Python 3.10 或更高版本
- 使用在线模型示例时，需要相应服务的 API Key
- 运行本地 Qwen 示例时，建议准备足够的内存；Apple Silicon、CUDA 和 CPU 均可自动选择

建议为不同示例创建独立虚拟环境：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

核心 Agent 示例可安装：

```bash
pip install openai python-dotenv requests google-search-results tavily-python
```

AutoGen 示例：

```bash
pip install -r ch4/autogen/requirement.txt
```

AgentScope 示例：

```bash
pip install -r ch4/autoscope/requirements.txt
```

本地模型与基础算法示例还可能用到：

```bash
pip install numpy torch transformers
```

## 配置环境变量

在需要运行的脚本目录中创建 `.env` 文件。请勿将真实密钥提交到 Git。

基础 Agent 示例使用：

```dotenv
DEEPSEEK_API_KEY=your_api_key
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL_ID=deepseek-chat
DEEPSEEK_TIMEOUT=60
SERPAPI_API_KEY=your_serpapi_key
```

AgentScope 示例使用：

```dotenv
DASHSCOPE_API_KEY=your_dashscope_api_key
```

部分工具调用示例还会读取：

```dotenv
OPENAI_API_KEY=your_api_key
OPENAI_BASE_URL=your_openai_compatible_base_url
OPENAI_MODEL_ID=your_model_id
TAVILY_API_KEY=your_tavily_api_key
```

## 运行示例

基础 LLM 调用：

```bash
python ch4/helloagentllm.py
```

ReAct、Plan-and-Solve 和 Reflection：

```bash
python ch4/React.py
python ch4/plansolve.py
python ch4/reflection.py
```

AutoGen 软件开发团队：

```bash
python ch4/autogen/autogen_software_team.py
```

AgentScope 三国狼人杀：

```bash
python ch4/autoscope/main_cn.py
```

本地 Qwen 模型：

```bash
python qw/model_loader.py
```

N-gram 与词向量示例：

```bash
python n_gram/n-gram.py
python n_gram/embedding.py
```

## 学习重点

- 封装兼容 OpenAI API 的模型客户端
- 使用 Thought / Action / Observation 构建 ReAct 循环
- 将复杂问题拆分为规划和执行两个阶段
- 通过反思反馈迭代改进模型输出
- 注册外部工具并让智能体选择调用
- 使用 AutoGen 和 AgentScope 组织多智能体协作
- 理解 N-gram、Embedding、Attention 和 Transformer 的基础实现

## 安全说明

- `.env`、虚拟环境、缓存和运行日志已通过 `.gitignore` 排除。
- 如果密钥曾被提交到任何远程仓库，请立即在对应平台撤销并重新生成。
- 外部搜索、天气和模型接口可能产生费用，请留意各服务商的计费规则。

