import argparse
from openai_client import summarize, translate, sentiment

def main():
    parser = argparse.ArgumentParser(
        prog="tool",
        description="CLI Text Tool — Summarize, Translate, Sentiment Analysis"
    )

    subparsers = parser.add_subparsers(dest="command")

    summarize_parser = subparsers.add_parser("summarize")
    summarize_parser.add_argument("text", type=str)

    translate_parser = subparsers.add_parser("translate")
    translate_parser.add_argument("text", type=str)
    translate_parser.add_argument("--lang", type=str, default="Hindi")

    sentiment_parser = subparsers.add_parser("sentiment")
    sentiment_parser.add_argument("text", type=str)

    args = parser.parse_args()

    if args.command == "summarize":
        print("\n Summary:\n")
        print(summarize(args.text))

    elif args.command == "translate":
        print(f"\n Translation ({args.lang}):\n")
        print(translate(args.text, args.lang))

    elif args.command == "sentiment":
        print("\n Sentiment Analysis:\n")
        print(sentiment(args.text))

    else:
        parser.print_help()

if __name__ == "__main__":
    main()