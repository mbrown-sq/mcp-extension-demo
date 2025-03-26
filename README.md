# SmartHub MCP Extension

A Goose extension for accessing and managing SmartHub data through Snowflake.

## Features

- Test Snowflake connectivity
- List available SmartHub tables
- Get merchant information by token or business ID
- Query merchant portfolio data
- Access SmartHub analytics

## Installation

Install from PyPI:

```bash
pip install smarthub-extension
```

## Configuration

Add to your Goose configuration:

```yaml
extensions:
  smarthub:
    type: stdio
    command: uvicorn smarthub_extension.server:app --transport stdio
    environment:
      SMARTHUB_LOG_FILE: /tmp/smarthub_mcp.log
      PYTHONPATH: /path/to/smarthub_extension/src
```

### Environment Variables

- `SNOWFLAKE_USER`: Your Snowflake username (required)
- `SNOWFLAKE_ACCOUNT`: Snowflake account name (default: square)
- `SMARTHUB_LOG_FILE`: Path to log file (default: /tmp/smarthub_mcp.log)

## Usage

### In Goose

Once configured, the extension provides these tools:

1. `test_snowflake_connection`: Test connectivity to Snowflake
2. `list_available_tables`: List accessible SmartHub tables
3. `get_merchant_info`: Get merchant details by token/ID

Example:
```python
result = await test_snowflake_connection()
tables = await list_available_tables()
merchant = await get_merchant_info("MLM7X617NKATG")
```

### Development

For local development:

1. Clone the repository:
```bash
git clone https://github.com/block/smarthub-extension
cd smarthub-extension
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
```

3. Install dependencies:
```bash
pip install -e .
```

4. Run the server:
```bash
uvicorn smarthub_extension.server:app --reload
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details