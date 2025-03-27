# Testing the SmartHub MCP Extension

## Installation Steps

1. **Install Goose Desktop**
   - Download Goose Desktop from: https://block.github.io/goose/
   - Install and launch the application

2. **Add the Extension**
   - Open Goose Desktop
   - Click the menu icon (⋮) in the top right
   - Select "Settings"
   - Go to the "Extensions" tab
   - Click "Add Extension"
   - Enter the following details:
     ```
     Name: SmartHub
     Type: Standard IO
     Command: path/to/python path/to/smarthub_extension/src/run_server.py
     Environment Variables:
     - PYTHONPATH: path/to/smarthub_extension/src
     - SMARTHUB_LOG_FILE: /tmp/smarthub_mcp.log
     ```

3. **Install Python Dependencies**
   ```bash
   # Create a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install the extension
   git clone https://github.com/mbrown-sq/mcp-extension-demo.git
   cd mcp-extension-demo
   pip install -e .
   ```

4. **Configure the Extension**
   Create a file named `.env` in the extension directory:
   ```
   SNOWFLAKE_USER=your_username
   SNOWFLAKE_ACCOUNT=your_account
   SNOWFLAKE_ROLE=your_role
   SNOWFLAKE_WAREHOUSE=your_warehouse
   ```

## Testing the Extension

1. **Basic Connection Test**
   In Goose, try:
   ```
   Can you test the Snowflake connection?
   ```

2. **List Available Tables**
   ```
   What tables are available in SmartHub?
   ```

3. **Look up Merchant Info**
   ```
   Can you look up information for merchant token MLM7X617NKATG?
   ```

## Example Queries

Here are some example queries to try:

1. **Basic Merchant Lookup**
   ```
   What's the current AM for merchant MLM7X617NKATG?
   ```

2. **Business Information**
   ```
   Tell me about business ID 302718489
   ```

3. **Table Exploration**
   ```
   What tables are available in the APP_MERCH_GROWTH database?
   ```

## Troubleshooting

1. **Connection Issues**
   - Verify Snowflake credentials in .env file
   - Check if VPN is required
   - Ensure Python environment is activated

2. **Extension Not Found**
   - Check the path in Goose settings
   - Verify virtual environment is activated
   - Check log file for errors

3. **Permission Errors**
   - Verify Snowflake role has necessary permissions
   - Check if tables are accessible

## Getting Help

If you encounter issues:
1. Check the log file at /tmp/smarthub_mcp.log
2. Look for error messages in Goose Desktop
3. Contact the extension author for help

## Feedback

Please provide feedback on:
- Query understanding
- Response accuracy
- Performance
- Any errors or issues
- Feature suggestions