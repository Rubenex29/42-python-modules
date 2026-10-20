from abc import ABC, abstractmethod
from typing import Any


# Abstract Base Class (ABC) defining the structure for all processors.
# This enforces a contract: subclasses MUST implement 'process' and 'validate'.
class DataProcessor(ABC):

    # Abstract method: Must be overridden by subclasses.
    # Defines the interface for processing data.
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    # Abstract method: Must be overridden by subclasses.
    # Defines the interface for validating data.
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    # Concrete method: Shared by all subclasses.
    # Provides common functionality for formatting the output.
    def format_output(self, result: str) -> str:
        return f"Output: {result}"


# Concrete class implementing the DataProcessor interface for numeric data.
class NumericProcessor(DataProcessor):

    # Implementation of validation logic specific to numeric lists.
    def validate(self, data: Any) -> bool:
        if not isinstance(data, list) or len(data) == 0:
            return False
        for n in data:
            if not isinstance(n, (int, float)):
                return False
        return True

    # Implementation of processing logic specific to calculating stats.
    def process(self, data: Any) -> str:
        try:
            size = len(data)
            total = sum(data)
            avg = total / size
            res = f"Processed {size} numeric values, sum={total}, avg={avg}"
            # Reuses the shared format_output method from the base class.
            return self.format_output(res)
        except Exception as e:
            return self.format_output(f"Error in NumericProcessor: {e}")


# Concrete class implementing the DataProcessor interface for text data.
class TextProcessor(DataProcessor):

    # Implementation of validation logic specific to non-empty strings.
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and len(data) > 0

    # Implementation of processing logic specific to text analysis.
    def process(self, data: Any) -> str:
        try:
            char_count = len(data)
            word_count = len(data.split())
            res = (f"Processed text: {char_count} characters, "
                   f"{word_count} words")
            return self.format_output(res)
        except Exception as e:
            return self.format_output(f"Error in TextProcessor: {e}")


# Concrete class implementing the DataProcessor interface for log data.
class LogProcessor(DataProcessor):

    # Implementation of validation logic specific to log patterns.
    def validate(self, data: Any) -> bool:
        if not isinstance(data, str):
            return False
        return data[0:6] == "INFO: " or data[0:7] == "ERROR: "

    # Implementation of processing logic specific to parsing logs.
    def process(self, data: Any) -> str:
        try:
            parts = data.split(": ", 1)
            level = parts[0]
            msg = parts[1]
            tag = "[ALERT]" if level == "ERROR" else "[INFO]"
            res = f"{tag} {level} level detected: {msg}"
            return self.format_output(res)
        except Exception as e:
            return self.format_output(f"Error in LogProcessor: {e}")


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    # List of test cases to demonstrate polymorphism.
    # Each item contains: (Processor, Data, Name, Validation Message)
    test_cases = [
        (NumericProcessor(), [1, 2, 3, 4, 5],
         "Numeric Processor", "Numeric data verified"),
        (TextProcessor(), "Hello Nexus World",
         "Text Processor", "Text data verified"),
        (LogProcessor(), "ERROR: Connection timeout",
         "Log Processor", "Log entry verified")
    ]

    for i, (processor, data, name, val_msg) in enumerate(test_cases):
        if i > 0:
            print()  # Add a blank line between cases

        print(f"Initializing {name}...")

        # Format the data display: strings get quotes, lists don't
        d_str = f'"{data}"' if isinstance(data, str) else str(data)
        print(f"Processing data: {d_str}")

        if processor.validate(data):
            print(f"Validation: {val_msg}")
            # Polymorphic call: 'process' works for any DataProcessor
            print(processor.process(data))
