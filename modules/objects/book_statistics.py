class BookStatistics:
    def __init__(self, stats_id: int, count_lines: int, count_spaces: int,
                 count_words: int, count_pattern: int, /):
        self.id = stats_id
        self.count_lines = count_lines
        self.count_spaces = count_spaces
        self.count_words = count_words
        self.count_pattern = count_pattern

    # TODO: Do I need this?
    @property
    def get_book_statistics(self) -> "BookStatistics":  # Type hint because it is Python
        return self
