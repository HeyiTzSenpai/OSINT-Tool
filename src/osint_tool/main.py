import argparse
from osint_tool.services.n8n_service import N8NService
from osint_tool.utils.file_utils import save_result

def main():
    parser = argparse.ArgumentParser(description='OSINT Tool to search global information about a specific individual')
    parser.add_argument('-p', '--prompt',
                        help='Initial prompt to search using OSINT (e.g. First name, Last name, City)')
    args = parser.parse_args()

    if args.prompt:
        n8n_service = N8NService()
        try:
            print(f"[*] Sending query to AI Agent: {args.prompt}")
            output_md = n8n_service.search(args.prompt)
            output_file = save_result(args.prompt, output_md)
            print(f"[*] Markdown file saved to {output_file.resolve()}")

        except Exception as e:
            print(f"[!] Error: {e}")
    else:
        parser.print_help()




if __name__ == '__main__':
    main()
