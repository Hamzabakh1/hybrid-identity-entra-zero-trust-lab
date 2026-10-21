# Read-only Graph example for a separately approved test tenant.
[CmdletBinding()]
param([Parameter(Mandatory)][guid]$ExpectedTenantId)
$ErrorActionPreference = 'Stop'
if (-not (Get-Command Get-MgContext -ErrorAction SilentlyContinue)) { throw 'Microsoft Graph PowerShell SDK is unavailable.' }
$context = Get-MgContext
if (-not $context -or $context.TenantId -ne $ExpectedTenantId.ToString()) { throw 'Graph context does not match the approved tenant.' }
if (-not (Get-Command Get-MgUser -ErrorAction SilentlyContinue)) { throw 'Graph Users module is unavailable.' }
Get-MgUser -Filter "startsWith(userPrincipalName,'lab.')" -ConsistencyLevel eventual -All -Property Id,DisplayName,UserPrincipalName,AccountEnabled |
    Select-Object Id,DisplayName,UserPrincipalName,AccountEnabled
