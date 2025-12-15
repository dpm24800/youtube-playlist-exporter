import yt_dlp
import csv
import re
import argparse
from time import sleep

# -------------------------
# UTILS
# -------------------------
def sanitize_filename(name):
    """Remove invalid characters for file names."""
    return re.sub(r'[<>:"/\\|?*]', '', name).strip()

def fetch_playlist_info(playlist_url):
    ydl_opts = {"extract_flat": True, "quiet": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(playlist_url, download=False)

def show_progress(current, total):
    print(f"\rProcessing {current}/{total}", end="", flush=True)

# -------------------------
# EXPORT FUNCTIONS
# -------------------------

def export_urls(info):
    """Bare URLs only (for download managers)."""
    rows = []
    total = len(info['entries'])
    for entry in info['entries']:
        url = f"https://www.youtube.com/watch?v={entry['id']}"
        rows.append([url])
    playlist_name = sanitize_filename(info.get('title', 'playlist'))
    filename = f"{playlist_name}_urls.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"✅ URLs exported to {filename}")

def export_indexed_urls(info):
    """Index + URLs."""
    rows = []
    total = len(info['entries'])
    for i, entry in enumerate(info['entries'], start=1):
        url = f"https://www.youtube.com/watch?v={entry['id']}"
        rows.append([i, url])
    playlist_name = sanitize_filename(info.get('title', 'playlist'))
    filename = f"{playlist_name}_indexed_urls.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"✅ Indexed URLs exported to {filename}")

def export_titles(info):
    """Bare titles only (for books, reading)."""
    rows = [[entry['title']] for entry in info['entries']]
    playlist_name = sanitize_filename(info.get('title', 'playlist'))
    filename = f"{playlist_name}_titles.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"✅ Titles exported to {filename}")

def export_indexed_titles(info):
    """Index + titles."""
    rows = [[i, entry['title']] for i, entry in enumerate(info['entries'], start=1)]
    playlist_name = sanitize_filename(info.get('title', 'playlist'))
    filename = f"{playlist_name}_indexed_titles.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"✅ Indexed titles exported to {filename}")

def export_indexed_titles_urls(info):
    """Index + titles + URLs."""
    rows = []
    for i, entry in enumerate(info['entries'], start=1):
        url = f"https://www.youtube.com/watch?v={entry['id']}"
        rows.append([i, entry['title'], url])
    playlist_name = sanitize_filename(info.get('title', 'playlist'))
    filename = f"{playlist_name}_indexed_titles_urls.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"✅ Indexed titles + URLs exported to {filename}")

def export_indexed_markdown(info):
    """Markdown export with playlist header."""
    playlist_name = sanitize_filename(info.get('title', 'playlist'))
    filename = f"{playlist_name}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"## {info.get('title', 'YouTube Playlist')}\n\n")
        for i, entry in enumerate(info['entries'], start=1):
            url = f"https://www.youtube.com/watch?v={entry['id']}"
            f.write(f"{i}. [{entry['title']}]({url})\n")
    print(f"✅ Markdown exported to {filename}")

# -------------------------
# MENU
# -------------------------
def show_menu():
    print("\n🎬 YouTube Playlist Exporter")
    print("1. Export URLs only (bare URLs for download manager)")
    print("2. Export indexed URLs")
    print("3. Export titles only (bare titles for books)")
    print("4. Export indexed titles")
    print("5. Export indexed titles + URLs")
    print("6. Export Markdown with playlist header")
    print("7. Export ALL")
    print("8. Exit")

def menu_mode(info):
    while True:
        show_menu()
        choice = input("Choose an option (1-8): ").strip()
        if choice == "1":
            export_urls(info)
        elif choice == "2":
            export_indexed_urls(info)
        elif choice == "3":
            export_titles(info)
        elif choice == "4":
            export_indexed_titles(info)
        elif choice == "5":
            export_indexed_titles_urls(info)
        elif choice == "6":
            export_indexed_markdown(info)
        elif choice == "7":
            export_urls(info)
            export_indexed_urls(info)
            export_titles(info)
            export_indexed_titles(info)
            export_indexed_titles_urls(info)
            export_indexed_markdown(info)
        elif choice == "8":
            print("👋 Exiting.")
            break
        else:
            print("❌ Invalid choice.")

# -------------------------
# ARGPARSE MODE
# -------------------------
def argparse_mode(args, info):
    if args.all:
        export_urls(info)
        export_indexed_urls(info)
        export_titles(info)
        export_indexed_titles(info)
        export_indexed_titles_urls(info)
        export_indexed_markdown(info)
    else:
        if args.urls:
            export_urls(info)
        if args.indexed_urls:
            export_indexed_urls(info)
        if args.titles:
            export_titles(info)
        if args.indexed_titles:
            export_indexed_titles(info)
        if args.indexed_titles_urls:
            export_indexed_titles_urls(info)
        if args.markdown:
            export_indexed_markdown(info)

# -------------------------
# ENTRY POINT
# -------------------------
def main():
    parser = argparse.ArgumentParser(description="YouTube Playlist Exporter")
    parser.add_argument("--url", help="YouTube playlist URL")
    parser.add_argument("--urls", action="store_true")
    parser.add_argument("--indexed_urls", action="store_true")
    parser.add_argument("--titles", action="store_true")
    parser.add_argument("--indexed_titles", action="store_true")
    parser.add_argument("--indexed_titles_urls", action="store_true")
    parser.add_argument("--markdown", action="store_true")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    playlist_url = args.url or input("Enter YouTube Playlist URL: ").strip()

    try:
        info = fetch_playlist_info(playlist_url)
    except Exception as e:
        print("❌ Failed to fetch playlist:", e)
        return

    if any([args.urls, args.indexed_urls, args.titles, args.indexed_titles, args.indexed_titles_urls, args.markdown, args.all]):
        argparse_mode(args, info)
    else:
        menu_mode(info)

if __name__ == "__main__":
    main()