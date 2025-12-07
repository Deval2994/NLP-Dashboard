"""
Mathematical Calculations for POS Tagging
Handles all probability calculations and data aggregation
"""

def map_tag_to_short(tag):
    """
    Convert full tag name to short form

    Parameters:
    -----------
    tag : str
        Full tag name ('Noun', 'Verb', 'Modal Auxiliary')

    Returns:
    --------
    str
        Short form ('n', 'v', 'm') or None if invalid
    """
    if tag == "Noun":
        return 'n'
    elif tag == "Verb":
        return 'v'
    elif tag == "Modal Auxiliary":
        return 'm'
    return None


def update_pos_count(pos_count, words, pos_tags):
    """
    Update POS count dictionary based on tagged words

    Parameters:
    -----------
    pos_count : dict
        Existing POS count dictionary
    words : list
        List of words
    pos_tags : dict
        Dictionary mapping word indices to POS tags

    Returns:
    --------
    dict
        Updated POS count dictionary
    """
    for word_idx, word in enumerate(words):
        word_lower = word.lower()
        tag = pos_tags[word_idx]

        tag_short = map_tag_to_short(tag)
        if tag_short is None:
            continue

        if word_lower not in pos_count:
            pos_count[word_lower] = {'n': 0, 'v': 0, 'm': 0}

        pos_count[word_lower][tag_short] += 1

    return pos_count


def calculate_emission_probability(pos_count):
    """
    Calculate emission probability table from POS counts

    Parameters:
    -----------
    pos_count : dict
        POS count dictionary

    Returns:
    --------
    dict
        Emission probability table with probabilities for each word
    """
    n_total = sum(pos_count[word]['n'] for word in pos_count.keys())
    v_total = sum(pos_count[word]['v'] for word in pos_count.keys())
    m_total = sum(pos_count[word]['m'] for word in pos_count.keys())

    emission_probability_table = {}

    for word in pos_count.keys():
        emission_probability_table[word] = {
            'n': pos_count[word]['n'] / n_total if n_total > 0 else 0,
            'v': pos_count[word]['v'] / v_total if v_total > 0 else 0,
            'm': pos_count[word]['m'] / m_total if m_total > 0 else 0
        }

    return emission_probability_table


def calculate_transition_count(all_tagged_sentences):
    """
    Calculate transition count table from tagged sentences
    Counts how many times each POS tag transitions to another POS tag

    Parameters:
    -----------
    all_tagged_sentences : list
        List of dictionaries containing tagged sentences
        Format: [{"words": [...], "tags": {0: "Noun", 1: "Verb", ...}}, ...]

    Returns:
    --------
    dict
        Transition count table
        Format: {"start": {"Noun": count, "Verb": count, ...}, "Noun": {...}, ...}
    """
    # Initialize transition table with all POS tags including 'start' and 'end'
    pos_tags = {"start"}

    # Collect all unique POS tags from sentences
    for sentence in all_tagged_sentences:
        for tag in sentence["tags"].values():
            pos_tags.add(tag)

    # Initialize transition count table
    transition_table = {}
    for pos in pos_tags:
        transition_table[pos] = {
            "Noun": 0,
            "Verb": 0,
            "Modal Auxiliary": 0,
            "end": 0
        }

    # Extract POS sequences from tagged sentences
    pos_sequences = [list(sentence["tags"].values()) for sentence in all_tagged_sentences]

    # Count transitions
    for sequence in pos_sequences:
        # Count transition from 'start' to first POS
        first_pos = sequence[0]
        transition_table["start"][first_pos] += 1

        # Count transitions between consecutive POS tags
        for i in range(len(sequence) - 1):
            current_pos = sequence[i]
            next_pos = sequence[i + 1]
            transition_table[current_pos][next_pos] += 1

        # Count transition from last POS to 'end'
        last_pos = sequence[-1]
        transition_table[last_pos]["end"] += 1

    return transition_table


def calculate_transition_probability(transition_table):
    """
    Calculate transition probability table from transition counts

    Parameters:
    -----------
    transition_table : dict
        Transition count table

    Returns:
    --------
    dict
        Transition probability table
        Format: {"Noun": {"Noun": probability, "Verb": probability, ...}, ...}
    """
    transition_probability_table = {}

    for current_pos in transition_table.keys():
        # Calculate total transitions from this POS
        total = sum(transition_table[current_pos].values())

        # Calculate probability for each next POS
        transition_probability_table[current_pos] = {}
        for next_pos in transition_table[current_pos].keys():
            if total > 0:
                transition_probability_table[current_pos][next_pos] = transition_table[current_pos][next_pos] / total
            else:
                transition_probability_table[current_pos][next_pos] = 0

    return transition_probability_table