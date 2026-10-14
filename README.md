# InstaBids plugin for Claude

Connect Claude to [InstaBids](https://instabids.ai) to start a home-repair request, answer its questions, check your jobs and read the anonymised contractor bids on them.

InstaBids is an early pilot in Broward and Palm Beach counties, Florida. It is still building its contractor network, so a request may get no bids. Homeowners pay InstaBids nothing.

## What is in this plugin
- **The InstaBids connector** (remote MCP server): `https://instabids.ai/api/agent/mcp`
- **Skill `home-project-request`**: turns a job description into a written request, step by step.
- **Skill `compare-contractor-bids`**: reads and compares the bids on your job, item by item.

## Tools
| Tool | What it does | Changes anything? |
|---|---|---|
| `how_instabids_works` | How the service works, cost and contact privacy (no sign-in) | No |
| `bid_checklist` | Items to compare in a bid (no sign-in) | No |
| `check_service_area` | Pilot-area guidance for a ZIP code (no sign-in) | No |
| `permit_facts` | Published permit facts for some pilot towns (no sign-in) | No |
| `list_my_jobs` | Your own requests | No |
| `get_job_status` | Status and bid count of one of your jobs | No |
| `list_bids` | The anonymised bids on one of your jobs | No |
| `start_job` | Starts a new request from your description | Yes |
| `answer_intake` | Adds your answer to an unsent request | Yes |
| `prepare_publish` | Checks a request is ready to send | Yes |
| `request_approval` | Gives you a sign-in code to review sending your request | Yes |
| `check_approval` | Checks whether you approved or declined | No |

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

Published by InstaBids Labs, Inc.
