# 🎬 YouTube Playlist Exporter
A **CLI-based Python tool** that extracts information from a YouTube playlist and exports in multiple formats for different use cases. Designed for **interns / junior developers** and real-world automation.

---

## ✨ Features
- ✅ Export modes:
  - **Bare URLs** (for download managers)
  - **Indexed URLs**
  - **Bare titles** (for books, reading)
  - **Indexed titles**
  - **Indexed titles + URLs**
  - **Markdown with playlist header**
  - Export ALL at once
- 🧠 Fetch playlist metadata only once (fast)
- 📊 Progress indicator during export
- 🖥️ Interactive CLI menu
- ⚙️ Argparse support for automation
- 📛 Output files named after the playlist (sanitized)

---

## 📁 Output Examples

Generated files examples:

```text
My Awesome Playlist_urls.csv
My Awesome Playlist_indexed_urls.csv
My Awesome Playlist_titles.csv
My Awesome Playlist_indexed_titles.csv
My Awesome Playlist_indexed_titles_urls.csv
My Awesome Playlist.md
```

- `urls.csv` → Bare URLs only (no index)
- `titles.csv` → Bare titles only (no index)
- `indexed_*.csv` → Include index
- `.md` → Markdown with playlist header and links

---

## 🛠️ Requirements

- Python 3.8+
- yt-dlp

Install dependencies:

```bash
pip install yt-dlp
```

---

## 🚀 Usage

### Interactive Menu Mode

```bash
python exporter.py
```

Choose export mode from the menu.

### CLI Flag Mode (Automation Friendly)

```bash
python exporter.py --url PLAYLIST_URL --all
python exporter.py --url PLAYLIST_URL --titles
python exporter.py --url PLAYLIST_URL --urls
python exporter.py --url PLAYLIST_URL --indexed_titles_urls
```

Available flags:

- `--urls` → Bare URLs only
- `--indexed_urls` → Index + URL
- `--titles` → Bare titles only
- `--indexed_titles` → Index + title
- `--indexed_titles_urls` → Index + title + URL
- `--markdown` → Markdown export with playlist header
- `--all` → Export all formats

---

## 🎯 Use Cases
<!-- - Dataset creation for ML / NLP projects
- Content curation
- Automation pipelines -->

- Playlist backups
- Export titles for books, URLs for download managers

---

## 🧑‍💻 Author
**Dipak Pulami Magar**  
Aspiring Python / Data / AI Engineer  

GitHub: https://github.com/dpm24800

<!-- ---

## ⭐ Future Improvements

- ZIP export
- JSON support
- Resume failed exports
- Package as pip module
- Channel playlist auto-detection -->

---

If you find this project helpful, don’t forget to ⭐ the repo!
