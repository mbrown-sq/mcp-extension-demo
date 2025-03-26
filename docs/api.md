# SmartHub MCP Extension API Documentation

## Overview

The SmartHub MCP extension provides natural language access to SmartHub data through three main tools:

1. `test_snowflake_connection`: Test connectivity to SmartHub Snowflake tables
2. `list_available_tables`: List all accessible tables in the APP_MERCH_GROWTH database
3. `get_merchant_info`: Get comprehensive merchant information using token or business ID

## Tools

### test_snowflake_connection

Test if we can connect to and query the SmartHub Snowflake tables.

**Parameters**: None

**Returns**:
```python
ConnectionResponse:
    status: str  # "success" or "error"
    role: Optional[str]  # Current Snowflake role if successful
    message: Optional[str]  # Error message if status is "error"
```

**Example**:
```python
result = await test_snowflake_connection()
if result["status"] == "success":
    print(f"Connected as role: {result['role']}")
```

### list_available_tables

List all tables available in the APP_MERCH_GROWTH database.

**Parameters**: None

**Returns**:
```python
TablesResponse:
    status: str  # "success" or "error"
    tables: Optional[List[TableInfo]]  # List of available tables if successful
    message: Optional[str]  # Error message if status is "error"

TableInfo:
    name: str  # Table name
    schema: str  # Schema name
    database: str  # Database name
    kind: str  # Object type (TABLE, VIEW, etc.)
```

**Example**:
```python
result = await list_available_tables()
if result["status"] == "success":
    for table in result["tables"]:
        print(f"Table: {table['name']} in {table['schema']}")
```

### get_merchant_info

Get comprehensive information about a merchant using their token or business ID.

**Parameters**:
- `merchant_token`: str - Either a merchant token (e.g., 'MLM7X617NKATG') or business ID (e.g., '302718489')

**Returns**:
```python
MerchantResponse:
    status: str  # "success" or "error"
    summary: Optional[MerchantSummary]  # Summary of merchant information
    details: Optional[Dict[str, Union[MerchantOwnership, AMInfo, BusinessInfo]]]  # Detailed data
    data_sources: List[str]  # List of data sources queried
    message: Optional[str]  # Error message if status is "error"

MerchantSummary:
    merchant_token: Optional[str]  # Merchant token
    business_id: Optional[str]  # Business ID
    business_name: Optional[str]  # Business name
    current_am: Optional[str]  # Current Account Manager
    am_team: Optional[str]  # AM team
    is_current: Optional[bool]  # Whether ownership is current
    last_updated: Optional[str]  # Last update timestamp
```

**Example**:
```python
result = await get_merchant_info("MLM7X617NKATG")
if result["status"] == "success":
    print(f"Business Name: {result['summary']['business_name']}")
    print(f"Current AM: {result['summary']['current_am']}")
```

## Data Sources

The extension queries the following tables:

1. `APP_MERCH_GROWTH.PUBLIC.DIM_AM_OWNERSHIP_HISTORICAL`
   - Historical ownership data
   - AM assignments
   - Current ownership status

2. `APP_MERCH_GROWTH.PUBLIC.ITD_RUN_MERCHANTS_COMBINED_AM_TEAM`
   - AM team information
   - Treatment groups
   - Treatment history

3. `APP_MERCH_GROWTH.PUBLIC.PAYOUT_TOOL_BUSINESS_ID_MAP_EXAMPLE`
   - Business information
   - Parent-child relationships
   - Merchant clustering

## Error Handling

All tools follow a consistent error handling pattern:

1. Success responses include:
   - `status: "success"`
   - Relevant data in response fields
   - `message: null`

2. Error responses include:
   - `status: "error"`
   - Data fields set to `null`
   - `message` containing error details

Common error scenarios:
- Connection failures
- Invalid merchant tokens
- Missing data
- Permission issues

## Configuration

The extension requires the following configuration:

```python
Config:
    snowflake_user: str
    snowflake_account: str
    snowflake_role: str
    snowflake_warehouse: str
    log_file: str
    debug: bool = False
```

Configuration is validated on startup and can be provided via:
1. Environment variables
2. Configuration file
3. Direct initialization