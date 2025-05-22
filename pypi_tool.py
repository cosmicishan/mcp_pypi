from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("pypi_insights")

async def fetch_url(package: str):

    PYPI_URL = "https://pypi.org/pypi/{package}/json"

    async with httpx.AsyncClient() as client:

        try:
            response = await client.get(PYPI_URL.format(package = package), timeout = 60.0)
            return response.json()
        
        except httpx.TimeoutException:
            print("Request timed out!")
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        except httpx.RequestError as e:
            print(f"Network error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return None
    
@mcp.tool()
async def get_package_info(package: str):

    """
    Fetches metadata for a Python package from PyPI.

    Args:
        package: The PyPI package name (e.g., "requests").

    Returns:
        Dict with name, summary, latest version, dependencies, and homepage.
    """

    data = await fetch_url(package)

    if not data:

        return f"Package {package} not found on PyPI."
    
    info = data["info"]
    requires_dist = info.get("requires_dist", [])
    summary = info.get("summary", "")
    version = info.get("version", "")
    homepage = info.get("home_page", info.get("project_url", ""))

    # Optionally, fetch and summarize release notes from description or homepage
    description = info.get("description", "")
    # Optionally, use BeautifulSoup to extract release notes if homepage is a GitHub releases page

    return {
        "name": package,
        "summary": summary,
        "latest_version": version,
        "dependencies": requires_dist,
        "homepage": homepage,
        "release_notes": description[:500] + "..." if description else "N/A"
    }

if __name__ == "__main__":
    mcp.run(transport='stdio')
