# mcp_pypi

MCP PyPI Insights
A Python project that leverages the Model Context Protocol (MCP) to create a server for fetching and analyzing Python package information from PyPI. This tool enables AI agents to access up-to-date package metadata through a standardized interface.

Overview
MCP PyPI Insights provides a seamless way to retrieve package information from the Python Package Index (PyPI) using the Model Context Protocol. The project consists of:

An MCP server that exposes PyPI package information as a tool

A client implementation for interacting with the server

Integration with LLM providers like Groq

Features
PyPI Package Information: Fetch metadata including version, dependencies, and release notes

Interactive Chat Interface: Communicate with AI models while providing access to PyPI data

Conversation Memory: Maintain context throughout interactions

Easy Integration: Works with any MCP-compatible client or agent

Installation
bash
# Clone the repository
git clone https://github.com/yourusername/mcp-pypi-insights.git
cd mcp-pypi-insights

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e .
Configuration
Create a .env file with your API keys:

text
GROQ_API_KEY=your_groq_api_key_here
Update the server.json file with the correct paths for your environment:

json
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
Usage
Starting the MCP Server
The PyPI tool server can be started directly:

bash
python pypi_tool.py
Using the Client
Run the interactive chat client to communicate with an AI model that has access to PyPI package information:

bash
python client.py
In the chat interface:

Type your questions about Python packages

Type 'clear' to reset conversation history

Type 'exit' or 'quit' to end the session

Example Interactions
