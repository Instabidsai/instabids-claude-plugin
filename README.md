# InstaBids plugin for Claude

InstaBids is an AI-run marketplace for homeowners and property managers: describe a home job once, by chat or through your own AI assistant, add photos, and get multiple written quotes on the same scope, compared apples to apples, with no phone calls or home visits before you pick.

Homeowners anywhere in the US can post a job; once you send it, InstaBids finds contractors to bid on it.

## Install
- **Claude Code**: `/plugin install instabids --marketplace Instabidsai/instabids-claude-plugin`
- **Gemini CLI**: `gemini extensions install https://github.com/Instabidsai/instabids-claude-plugin`
- **Cline**: see [Cline](#cline) below.

## Cline
Add the hosted server to Cline (MCP Servers > Remote Servers, or `cline_mcp_settings.json`). Nothing to install and no API key:

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

Then press **Authenticate** and sign in with your InstaBids homeowner account (OAuth 2.1). Step-by-step notes for an AI assistant are in [llms-install.md](llms-install.md).

## What is in this plugin
- **The InstaBids connector** (remote MCP server): `https://instabids.ai/api/agent/mcp`
- **Skill `home-project-request`**: turns a job description into a written request, step by step.
- **Skill `compare-contractor-bids`**: reads and compares the bids on your job, item by item.

## Tools
No-account tools: how_instabids_works, bid_checklist, check_service_area, permit_facts, start_job, job_status. More after you sign in: your jobs, intake questions, bids, and publishing with your OK.

Only you can send a request to contractors, by signing in to InstaBids. Claude cannot send it, choose a bid or contact a contractor.

## Sign-in
Tools that read or change your jobs ask you to sign in with your InstaBids homeowner account. At sign-in you choose whether Claude may only read your jobs and bids, or also prepare jobs. You can disconnect at any time from Connected assistants in your InstaBids account.

## Privacy
- Claude receives only what the tools return: your own jobs, their questions and answers, and the bids on them. Bids carry a label such as Contractor A and no contractor names or contact details.
- InstaBids keeps a log of each tool call (which tool, when, and the outcome) for security and abuse prevention.
- What you send through the connector is handled under the [InstaBids privacy policy](https://instabids.ai/privacy), including how long it is kept and how to ask for your data.
- What Claude does with the conversation is covered by Anthropic's own terms and privacy policy.

## Support
- Documentation: https://instabids.ai/developers
- Contact: support@instabids.ai or https://instabids.ai/contact
- Terms: https://instabids.ai/terms

## Licence
The MIT licence covers the code and text in this repository only. It does not grant any right to use the InstaBids name or logo.

Published by InstaBids Labs, Inc.
