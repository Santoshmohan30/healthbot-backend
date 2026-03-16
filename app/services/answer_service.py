def build_debug_answer(question: str, contexts: list[dict]) -> str:
    if not contexts:
        return "I could not find anything relevant in the knowledge base."

    unique_points = []
    seen = set()

    for item in contexts:
        snippet = item["text"].replace("\n", " ").strip()
        short = snippet[:160]
        if short not in seen:
            seen.add(short)
            unique_points.append(short)

    lines = ["Here is what I found relevant to your question:"]
    for i, point in enumerate(unique_points, start=1):
        lines.append(f"{i}. {point}")

    return "\n".join(lines)
