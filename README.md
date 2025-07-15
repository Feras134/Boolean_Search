Features
Boolean Search: Supports AND (&) and OR (space) operations.

Tokenization: Cleans and splits text into lowercase words (removes punctuation).

Inverted Index: Efficiently maps keywords to document IDs for fast lookup.

Benchmarking: Measures query execution time in microseconds (µs).

⚙️ Installation
Clone the repository (if applicable) or download BolSearch.ipynb.

Ensure Python 3.x and Jupyter Notebook are installed.

Install dependencies (none beyond standard libraries: json, time).

🚀 Usage
Prepare Data:

Place your dataset (e.g., news.json) in the same directory.

Each JSON line should contain a "short_description" field (see load_dataset()).

Run the Notebook:

sh
jupyter notebook BolSearch.ipynb
Execute cells to:

Build the inverted index (Index_Creation).

Run sample queries (experiment() function).

Custom Queries:
Modify sample_queries in the __main__ block or call:

python
Boolean_Search("your&query", term_index)
🔍 How It Works
Tokenization:

Converts text to lowercase and removes punctuation.

Example: "Hello, world!" → ["hello", "world"].

Inverted Index:

Maps each word to a list of document IDs containing it.

Example: {"hello": [0, 2], "world": [0, 1]}.

Query Processing:

AND (&): Intersection of document IDs (e.g., king&salman).

OR (space): Union of document IDs (e.g., football basketball).


