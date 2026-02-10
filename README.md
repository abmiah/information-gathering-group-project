# Information Gathering - Group Project

### Contributers 
- Akshay - https://github.com/akshaykkarn-ops
- Arjeta - Add link
- Amrol - https://github.com/abmiah

## Legal Disclaimer 

Please be advised that the intent of this presentation and accompanying script is solely educational. We strongly encourage caution for anyone who chooses to utilise this script, as it is imperative that it be used within legal boundaries. Engaging in any attempts to execute the script on known companies is illegal and constitutes unauthorised access. This is in accordance with several legal frameworks, including India’s Information Technology Act of 2000, the United Kingdom's Computer Misuse Act of 1990, the European Union’s NIS2 Directive, the UAE’s Federal Decree-Law No. 34 of 2021 on Combatting Rumours and Cybercrime, and the United States' Computer Fraud and Abuse Act (CFAA).

Please ensure that this script is utilised legally for testing purposes and not for any malicious intent.

Contents
--------
- `main.py` — orchestrates the tools and user interaction.
- `ping_command.py` — ping utility.
- `scanner.py` — IP/domain helpers and port scanner.
- `scriptHunter.py` — Hunter.io API helper to fetch email counts/data.

Quick start
-----------
1. Install Python 3.10+.
2. (Optional) Create and activate a virtual environment:

   python3 -m venv .venv
   source .venv/bin/activate

3. Install dependencies (the project uses `pyhunter` for Hunter.io access):

   pip install pyhunter

4. (Optional) Set your Hunter.io API key as an environment variable:

   export HUNTER_API_KEY="your_api_key_here"

Usage
-----
Run the main script:

   python3 main.py

When running, `main.py` prints an intro message, then allows you to use the ping tool, the scanner (IP/domain resolution and port scanning), and the Hunter lookup.

Notes
-----
- Do not commit API keys. Use environment variables.
- Port scanning across many ports sequentially can be slow. Consider adding concurrency (threads or async) to `scanner.py`.
- If a module appears to run twice, check that the module doesn't call its own `main()` at import time (use `if __name__ == '__main__'` guards).

Summaries
---------
scriptHunter.py:

scriptHunter.py provides an interactive wrapper around Hunter.io API calls to retrieve email-related information for a domain.

Core behavior:
- It creates a PyHunter client using an API key (usually provided via environment variable or hard-coded — environment variables are recommended).
- It exposes a function (for example `main()` or `main_hunter()`) that:
  - Prompts the user for a domain if one isn't provided.
  - Validates that a domain string exists.
  - Calls Hunter.io methods such as `email_count(domain)` or `domain_search(domain)` using the `PyHunter` client to fetch data.
  - Handles `None` or empty responses by printing friendly messages like "No email information found for domain `...`."
  - Prints results to the console and returns a status (or exits).

Important implementation notes:
- Avoid executing the module's main logic at import time. Ensure long-running network calls are inside a guarded `if __name__ == '__main__'` block or inside functions that are called explicitly by `main.py`.
- Handle network errors, rate limits and API failures gracefully.
- The module is intended for educational/demonstration use; do not use it for unauthorized reconnaissance.

Ensure you replace the api key placeholder with your actual Hunter.io API key, and do not share it publicly.

main.py:

`main.py` acts as the top-level orchestrator. Its responsibilities:
- Print an introductory message explaining the tools and safety disclaimers.
- Import the three helper modules (`ping_command`, `scanner`, `scriptHunter`) and call their primary functions in sequence.
- Present a simple menu to the user for interactive actions (ping, resolve/scan, hunter lookup), or call each module sequentially depending on design.
- Print a friendly outro when finished.

Implementation guidance:
- Ensure `intro_message()` is called before `main()` when the script runs (put the call order explicitly in the `if __name__ == '__main__'` block).
- Use `hasattr()` or try/except around function calls if module function names may vary, but avoid importing modules that run code on import.
- Prevent duplicate execution by verifying that modules do not call `main()` at import time.

Troubleshooting tips
--------------------
- If `main_hunter()` executes twice, open `scriptHunter.py` and ensure it doesn't call its own main on import. All invocation should come from `main.py`.
- To speed up the scanner, convert the sequential port loop into a thread pool (concurrent.futures.ThreadPoolExecutor) or use asynchronous sockets.
- If a function like `check_domain()` calls `user_input()` multiple times, refactor to call it once and reuse the result.

License & Authors
-----------------
Educational project. Add a license file if you want to share it publicly.

Authors: Akshay, Arjeta and Amrol

Enjoy exploring the code!
