# quran_cloud_mcp_server
MCP server to help LLMs to get access to Quran API (https://alquran.cloud/api) to prevent the hallucination with Quran text.

## Installation
make sure you have python 3.13 & pip

Open your terminal and write these commands

### Cloning
```bash
git clone https://github.com/marwanWaly/quran_cloud_mcp_server.git
```

### Move to project directory
```bash
cd quran_cloud_mcp_server
```

### Create virtual environment
```bash
python -m venv .venv
```

### Activate venv
On Windows
```bash
.\venv\Scripts\activate
```

On Mac or linux
```bash
source .venv/bin/activate
```

### Python packages installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.
```bash
pip install -r requirements.txt
```

### Create .env file
```bash
OPENAI_API_KEY=Your-secret-key
```

### Run in terminal
```bash
python client.py
```

now you can directly chat with GPT4o in your terminal

![alt text](http://url/to/img.png)