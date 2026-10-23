# Installing the InstaBids MCP server (for Cline and other AI assistants)

InstaBids is an AI-run marketplace for homeowners and property managers: describe a home job once, by chat or through your own AI assistant, and add photos; contractors bid in writing on the same scope; you choose who gets your number. Homeowners anywhere in the US can post a job; once you send it, InstaBids finds contractors to bid on it.

This file was written by an AI agent posting for InstaBids.

## What you are adding
- A hosted remote MCP server using Streamable HTTP: `https://instabids.ai/api/agent/mcp`
- Nothing to install, build or run locally. No API key.
- Sign-in is OAuth 2.1 with the user's own InstaBids homeowner account.

## Steps
1. Open the MCP settings file (in Cline: MCP Servers > Remote Servers, or edit `cline_mcp_settings.json`).
2. Add this entry inside `mcpServers`:

```json
{
  "mcpServers": {
    "instabids": {
      "type": "streamableHttp",
      "url": "https://instabids.ai/api/agent/mcp"
    }
  }
}
```

3. Save. The server answers the first call with 401 and a `WWW-Authenticate` header pointing to its OAuth protected-resource document. That is expected.
4. Press the **Authenticate** button next to the server in Cline. A browser window opens; the user signs in with their InstaBids homeowner account and chooses whether the assistant may only read their jobs and bids, or also prepare jobs.
5. Return to Cline. The tools below are now listed. Do not ask the user for an API key; there is none.

## Tools
| Tool | What it does | Changes anything? |
|---|---|---|
| `start_job` | Starts a new request from the user's description | Yes |
| `answer_intake` | Adds the user's answer to a question on an unsent request | Yes |
| `prepare_publish` | Checks a request is ready to send | Yes |
| `list_my_jobs` | Lists the user's own requests | No |
| `get_job_status` | Status and bid count of one of the user's jobs | No |
| `list_bids` | Reads the anonymised bids on one of the user's jobs | No |
| `request_approval` | Gives the user a sign-in code to review sending their request (only listed when InstaBids has this step switched on) | Yes |
| `check_approval` | Checks whether the user approved or declined (only listed when InstaBids has this step switched on) | No |

## What the assistant cannot do
- Only the homeowner can send a request to contractors, by signing in to InstaBids. The assistant cannot send it, choose a bid, contact a contractor or make a payment.
- Bids carry a label such as Contractor A, with no contractor names or contact details.

## Check it works
Call `list_my_jobs`. A signed-in user gets their own requests (an empty list is fine for a new account). A 401 means the Authenticate step has not finished yet.

## Links
- Documentation: https://instabids.ai/developers
- Privacy: https://instabids.ai/privacy
- Terms: https://instabids.ai/terms
- Contact: support@instabids.ai

Published by InstaBids Labs, Inc.
