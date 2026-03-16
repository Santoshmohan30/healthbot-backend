def chunk_text(text: str, chunk_size: int = 800, overlap: int = 120) -> list[str]:
    text = text.strip()
    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text):
        end = min(len(text), start + chunk_size)
        chunks.append(text[start:end])

        if end == len(text):
            break

        start = end - overlap

    return chunks
