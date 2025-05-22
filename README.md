# MCP PyPI Insights

A Python project that leverages the **Model Context Protocol (MCP)** to create a server for fetching and analyzing Python package information from PyPI. This tool enables AI agents to access up-to-date package metadata through a standardized interface.

---

## Overview

**MCP PyPI Insights** provides a seamless way to retrieve package information from the Python Package Index (PyPI) using the Model Context Protocol. The project consists of:

- An MCP server that exposes PyPI package information as a tool  
- A client implementation for interacting with the server  
- Integration with LLM providers like **Groq**

---

## Features

- **PyPI Package Information**: Fetch metadata including version, dependencies, and release notes  
- **Interactive Chat Interface**: Communicate with AI models while providing access to PyPI data  
- **Conversation Memory**: Maintain context throughout interactions  
- **Easy Integration**: Works with any MCP-compatible client or agent

---

## Installation

```bash
# Clone the repository
git clone https://github.com/cosmicishan/mcp_pypi.git
cd mcp_pypi

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .
```

---

## Configuration

Create a `.env` file with your API keys:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Update the `server.json` file with the correct paths for your environment:

```json
{
  "mcpServers": {
    "pypi_server": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/your/project/",
        "run",
        "--python",
        ".venv/bin/python",
        "pypi_tool.py"
      ]
    }
  }
}
```

---

## Usage

### Starting the MCP Server

The PyPI tool server can be started directly:

```bash
python pypi_tool.py
```

### Using the Client

Run the interactive chat client to communicate with an AI model that has access to PyPI package information:

```bash
python client.py
```

In the chat interface:

- Type your questions about Python packages  
- Type `clear` to reset conversation history  
- Type `exit` or `quit` to end the session

---

## Example Interactions

### 🧠 Model Context Protocol Inspector

The MCP Inspector is a developer tool for testing and debugging MCP servers like our PyPI package information server. 

![MCP Inspector Screenshot](https://github.com/user-attachments/assets/d9386522-96b1-447f-9858-f770c694923c)

---

### 💬 Interactive Chat via `client.py`

You can start the client to initiate a chat-based session with the AI model. The model can now fetch real-time PyPI data and respond to your queries intelligently.

Below is an example screenshot of a live session using `client.py`, where the model answers questions about Python packages using up-to-date metadata:

![Client Interaction Screenshot](https://github.com/user-attachments/assets/0eb2ed84-1fdb-4bee-aed2-5373727824f8)

---

