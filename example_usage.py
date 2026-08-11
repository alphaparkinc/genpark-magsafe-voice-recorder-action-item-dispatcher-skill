from client import MagsafeVoiceRecorderActionItemDispatcherClient

def main():
    client = MagsafeVoiceRecorderActionItemDispatcherClient()
    res = client.process_and_dispatch_audio("magsafe_rec_001.m4a", ["Slack", "Notion"])
    print(f"Dispatched Actions: {res['dispatched_actions_count']}")
    print(res["processed_notes_markdown"])

if __name__ == "__main__":
    main()
