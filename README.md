# quran_cloud_mcp_server
MCP server to help LLMs to get access to Quran API (https://alquran.cloud/api) to prevent the hallucination with Quran text.

hallucination is a big problem specially when you are working on sensitive data that each character is important.

one way of reducing the hallucination is by providing the context to your LLM but of course with large chunk of text like the holy Quran it's not efficient if you put all text in each request.

So, in this repo I have created an MCP server that's connect your LLM to a free API https://alquran.cloud/api that enables your model to retrieve only the data he needs.

Also, I will show to you how we can connect this MCP server to Claude desktop application.

## Example of Claude the original response
![Claude original response](https://github.com/marwanWaly/quran_cloud_mcp_server/blob/main/imgs/original_claude_response.png?raw=true)

## Example of Claude the new response after connecting to Search-Quran MCP server 
![Claude New response](https://github.com/marwanWaly/quran_cloud_mcp_server/blob/main/imgs/new_claude_response.png?raw=true)

## Installation
make sure you have python 3.13 & pip

Open your terminal and write these commands

### Cloning
```
git clone https://github.com/marwanWaly/quran_cloud_mcp_server.git
```

### Move to project directory
```
cd quran_cloud_mcp_server
```

### Create virtual environment
```
python -m venv .venv
```

### Activate venv
On Windows
```
.\venv\Scripts\activate
```

On Mac or linux
```
source .venv/bin/activate
```

### Python packages installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt.
```
pip install -r requirements.txt
```

### Create .env file
```
OPENAI_API_KEY=Your-secret-key
```

### Run in terminal
```
python client.py
```

now you can directly chat with GPT4o in your terminal

![server running in terminal](https://github.com/marwanWaly/quran_cloud_mcp_server/blob/main/imgs/run_server_in_terminal.PNG)

## Connect the server to Claude Desktop
Download [Claude](https://claude.ai/download) desktop and open it

## Step 1
Select setting from the file menu

![add_mcp_to_claude_step-1.png](https://github.com/marwanWaly/quran_cloud_mcp_server/blob/main/imgs/add_mcp_to_claude_step-1.png)

## Step 2
Click on `Developer` then `Edit Config`

[add_mcp_to_claude_step-2.png](https://github.com/marwanWaly/quran_cloud_mcp_server/blob/main/imgs/add_mcp_to_claude_step-2.png)

## Step 3
Open `claude_desktop_config.json`

[add_mcp_to_claude_step-3.png](https://github.com/marwanWaly/quran_cloud_mcp_server/blob/main/imgs/add_mcp_to_claude_step-3.png)

## Step 4
Write this configuration in the file

```
{
  "mcpServers": {
    "Search-Quran": {
      "command": "python",
      "args": [
        "PROJECT_PATH_ON_YOUR_PC\\server.py"
      ],
      "host": "127.0.0.1",
      "port": 8080,
      "timeout": 30000
    }
  }
}
```

Don't forget to replace `PROJECT_PATH_ON_YOUR_PC` with the absolute path to your project server

[add_mcp_to_claude_step-4.png](https://github.com/marwanWaly/quran_cloud_mcp_server/blob/main/imgs/add_mcp_to_claude_step-4.png)

## Step 5
Restart Claude app (make sure it's completely closed from your taskbar by right click on Claude icon and select `Quit`)

Check if the new MCP has been added

[add_mcp_to_claude_step-5.png](https://github.com/marwanWaly/quran_cloud_mcp_server/blob/main/imgs/add_mcp_to_claude_step-5.png)

Click on tools icon 

[add_mcp_to_claude_step-6.png](https://github.com/marwanWaly/quran_cloud_mcp_server/blob/main/imgs/add_mcp_to_claude_step-6.png)
