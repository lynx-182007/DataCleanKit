from abc import ABC, abstractmethod


class CleaningError(Exception):
    """Base exception for errors encountered during data cleaning."""


class DataValidationError(CleaningError):
    """Raised when dataset structure, columns, data types, or values
    do not meet the required validation rules."""


class IDataSet(ABC):
    """Contract for dataset storage and management.

    Provides a common interface for loading, accessing, and updating
    dataset records.
    """

    @property
    @abstractmethod
    def data(self):
        """Return the currently stored dataset records."""

    @abstractmethod
    def load_data(self, data):
        """Load initial dataset records.

        Args:
            data: Records to be stored in the dataset.

        Raises:
            DataValidationError: If the provided data format is invalid.
        """

    @abstractmethod
    def get_data(self):
        """Return the current dataset records."""

    @abstractmethod
    def update_data(self, data):
        """Replace the current dataset records with updated records.

        Args:
            data: New records to replace the existing dataset.

        Raises:
            DataValidationError: If the provided data format is invalid.
        """


class IMissingValueHandler(ABC):
    """Contract for detecting and handling missing dataset values."""

    @abstractmethod
    def fill_missing(self, data, value):
        """Replace missing values in the dataset with the specified value.

        Args:
            data: Dataset records to process.
            value: Replacement value for missing entries.

        Returns:
            Updated dataset records.
        """

    @abstractmethod
    def drop_missing(self, data):
        """Remove records containing missing values.

        Args:
            data: Dataset records to process.

        Returns:
            Dataset records without missing values.
        """


class ITextNormalizer(ABC):
    """Contract for cleaning and standardizing text values."""

    @abstractmethod
    def trim_whitespace(self, text):
        """Remove leading, trailing, and unnecessary extra whitespace.

        Returns:
            A cleaned text string.
        """

    @abstractmethod
    def change_case(self, text):
        """Standardize the letter casing of a text string.

        Returns:
            A text string with standardized casing.
        """

    @abstractmethod
    def normalize_text(self, text):
        """Apply whitespace trimming and case standardization.

        Returns:
            A normalized text string.
        """


class IDuplicateRemover(ABC):
    """Contract for identifying and removing duplicate dataset records."""

    @abstractmethod
    def remove_duplicates(self, data):
        """Remove duplicate records while preserving unique records.

        Args:
            data: Dataset records to process.

        Returns:
            Dataset records without duplicates.
        """


class ISchemaValidator(ABC):
    """Contract for validating dataset structure and value types."""

    @abstractmethod
    def validate_columns(self, data, schema):
        """Check whether dataset columns match the expected schema.

        Returns:
            True if the columns are valid.

        Raises:
            DataValidationError: If columns do not match the schema.
        """

    @abstractmethod
    def validate_types(self, data, schema):
        """Check whether dataset values match the expected data types.

        Returns:
            True if all data types are valid.

        Raises:
            DataValidationError: If one or more values have invalid types.
        """


class ICleaningReport(ABC):
    """Contract for generating, storing, and displaying cleaning reports."""

    @property
    @abstractmethod
    def summary(self):
        """Return the generated cleaning report summary."""

    @abstractmethod
    def generate_report(self):
        """Generate and store a summary of the cleaning results."""

    @abstractmethod
    def display_report(self):
        """Display the generated cleaning report."""


class ICleaningPipeline(ABC):
    """Contract for coordinating dataset cleaning and validation."""

    @property
    @abstractmethod
    def dataset(self):
        """Return the dataset instance managed by the pipeline."""

    @abstractmethod
    def clean_data(self):
        """Execute the required cleaning and validation operations.

        Raises:
            CleaningError: If a cleaning or pipeline operation fails.
        """

    @abstractmethod
    def run_pipeline(self):
        """Run the complete cleaning pipeline and display its report."""