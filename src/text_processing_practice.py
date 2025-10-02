"""Module for cleaning sensitive names from text reports."""


class TextCleaner:
    """Cleans a text report by replacing specific names.

    Attributes:
        names (list[str]): List of names to clean.
        report (str): The text report to clean.
        replacement (str): The replacement string for names.
    """

    names: list[str]
    report: str
    replacement: str

    def __init__(
        self, names: list[str], report: str, replacement: str = 'Suspect'
    ) -> None:
        """Initializes the TextCleaner.

        Args:
            names (list[str]): Names to replace.
            report (str): The text report to process.
            replacement: Replacement string
        """
        self.names = names
        self.report = report
        self.replacement = replacement

    def clean_names(self) -> str:
        """Replaces all names in the report with the replacement string.

        Returns:
            str: The cleaned report
        """
        for name in self.names:
            self.report = self.report.replace(name, name.lower()).replace(
                name.lower(), self.replacement
            )
        return self.report


report = """
Anthony Soprano was arrested for Murder
Transcript:
Mr.Soprano - "We definitely murdered that guy."
Heisenberg - "That's true tony. jesse also did some crimes."
"""

names = ['Anthony Soprano', 'Mr.Soprano', 'Heisenberg', 'tony', 'jesse']
cleaner = TextCleaner(names, report)
clean = cleaner.clean_names()
print(clean)
