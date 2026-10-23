# InstaBids plugin for ChatGPT and Codex

InstaBids is an AI-run marketplace for homeowners and property managers: describe a home job once, by chat or through your own AI assistant; contractors bid in writing on the same scope; you choose who gets your number.

Homeowners anywhere in the US can post a job; once you send it, InstaBids finds contractors to bid on it.

This plugin connects ChatGPT and Codex to [InstaBids](https://instabids.ai) so the assistant can start a home-repair request, answer its questions, check your jobs and read the anonymised contractor bids on them.

## What is in this plugin
- **The InstaBids connector** (remote MCP server): `https://instabids.ai/api/agent/mcp`
- **Skill `home-project-request`**: turns a job description into a written request, step by step.
- **Skill `compare-contractor-bids`**: reads and compares the bids on your job, item by item.

## Use it in Codex
Add these two lines to your Codex `config.toml`:

```toml
[mcp_servers.instabids]
url = "https://instabids.ai/api/agent/mcp"
```

## Tools
| Tool | What it does | Changes anything? |
|---|---|---|
| `list_my_jobs` | Your own requests | No |
| `get_job_status` | Status and bid count of one of your jobs | No |
| `list_bids` | The anonymised bids on one of your jobs | No |
| `start_job` | Starts a new request from your description | Yes |
| `answer_intake` | Adds your answer to an unsent request | Yes |
| `prepare_publish` | Checks a request is ready to send | Yes |
| `request_approval` | Gives you a sign-in code to review sending your request (only listed when InstaBids has this step switched on) | Yes |
| `check_approval` | Checks whether you approved or declined (only listed when InstaBids has this step switched on) | No |

All tools need you to sign in with your InstaBids homeowner account.

Only you can send a request to contractors, by signing in to InstaBids. The assistant cannot send it, choose a bid or contact a contractor.

## Sign-in
Tools that read or change your jobs ask you to sign in with your InstaBids homeowner account. At sign-in you choose whether the assistant may only read your jobs and bids, or also prepare jobs. You can disconnect at any time from Connected assistants in your InstaBids account.

## Privacy
- The assistant receives only what the tools return: your own jobs, their questions and answers, and the bids on them. Bids carry a label such as Contractor A and no contractor names or contact details.
- InstaBids keeps a log of each tool call (which tool, when, and the outcome) for security and abuse prevention.
- What you send through the connector is handled under the [InstaBids privacy policy](https://instabids.ai/privacy), including how long it is kept and how to ask for your data.
- What ChatGPT or Codex does with the conversation is covered by OpenAI's own terms and privacy policy.

## Support
- Documentation: https://instabids.ai/developers
- Contact: support@instabids.ai or https://instabids.ai/contact
- Terms: https://instabids.ai/terms

## Licence
The MIT licence covers the code and text in this plugin package only. It does not grant any right to use the InstaBids name or logo.

Published by InstaBids Labs, Inc.
