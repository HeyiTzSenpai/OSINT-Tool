import argparse
import requests
from osint_tool import config


def main():
    parser = argparse.ArgumentParser(description='OSINT Tool to search global information about a specific individual')
    parser.add_argument('-p', '--prompt',
                        help='Initial prompt to search using OSINT (e.g. First name, Last name, City)')
    args = parser.parse_args()

    # If the user provided a prompt using -p
    if args.prompt:
        # 1. Package the data for n8n
        payload = {"query": args.prompt}

        # 2. Set the header if you used Header Auth in n8n
        headers = {"X-N8N-API-KEY": config.N8N_API_KEY}

        try:
            print(f"[*] Sending query to AI Agent: {args.prompt}")

            # 3. POST the data to n8n and wait for the response
            # Note: Ensure config.N8N_WEBHOOK_URL is set in your .env
            response = requests.post(config.N8N_WEBHOOK_URL, json=payload, headers=headers)
            response.raise_for_status()

            # 4. Print the output from the AI Agent
            print("\n--- AI AGENT OUTPUT ---")
            print(response.text)  # Use response.json() to parse as a dictionary
            print("-----------------------\n")

        except Exception as e:
            print(f"[!] Error: {e}")
        else:
            # If no -p flag was used, show the help message
            parser.print_help()




if __name__ == '__main__':
    main()
