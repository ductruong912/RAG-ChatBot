def đeuplicate_chunks(chunks):

    seen = set()
    unique_chunks = []

    for chunk in chunks:
        key = hash(chunk)
        if key not in seen:
            seen.add(key)
            unique_chunks.append(chunk)
            
    return unique_chunks