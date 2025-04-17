class BookStatistics:
    def __init__(self, stats_id: int, line_count: int, space_count: int, word_count: int, /,
                 pattern_count: int | None = None):
        self.id = stats_id
        self.line_count = line_count
        self.space_count = space_count
        self.word_count = word_count
        self.pattern_count = pattern_count

    @property
    def has_pattern(self) -> bool:
        return self.pattern_count is not None
