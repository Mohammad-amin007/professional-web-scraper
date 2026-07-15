import argparse
import asyncio


def create_parser():

    parser = argparse.ArgumentParser(
        description="Professional Web Scraper CLI"
    )


    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )


    subparsers.add_parser(
        "scrape",
        help="Run scraper pipeline"
    )


    subparsers.add_parser(
        "analytics",
        help="Show analytics"
    )


    subparsers.add_parser(
        "export",
        help="Export data"
    )


    return parser



def main():

    parser = create_parser()

    args = parser.parse_args()


    if args.command == "scrape":

        from app import run

        run()


    elif args.command == "analytics":

        from services.cli_service import CLIService

        service = CLIService()

        asyncio.run(
            service.show_analytics()
        )


    elif args.command == "export":

        from services.cli_service import CLIService

        service = CLIService()

        asyncio.run(
            service.export_books()
        )



if __name__ == "__main__":
    main()