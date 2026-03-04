def build_answer(question: str, contexts: list[dict]) -> str:
    if not contexts:
        return (
            "I couldn't find anything in the knowledge base to answer that. "
            "Please ingest relevant notes first."
        )

    bullets = []
    for c in contexts[:4]:
        title = c["meta"].get("title", "source")
        doc_id = c["meta"].get("doc_id", "unknown")
        snippet = c["text"].strip().replace("\n", " ")
        bullets.append(f"- ({title}, doc_id={doc_id}) {snippet[:220]}")

    return (
        f"Question: {question}\n\n"
        "Here’s what I found in your knowledge base:\n" + "\n".join(bullets)
    )
