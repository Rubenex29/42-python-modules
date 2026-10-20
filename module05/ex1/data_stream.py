from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional


# Abstract Base Class representing a generic Data Stream.
class DataStream(ABC):
    stream_type = "Unknown"

    def __init__(self, stream_id):
        self.stream_id = stream_id

    # Abstract method: enforces streams must know how to process a batch
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    # Concrete method: Common filtering logic inherited by all streams.
    # Subclasses can use this directly or override it (optional).
    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria is None:
            return data_batch
        if criteria == "numeric":
            return [x for x in data_batch if isinstance(x, (int, float))]
        if criteria == "text":
            return [x for x in data_batch if isinstance(x, str)]
        return []

    # Concrete method: Returns metadata about the stream.
    def get_stats(self) -> str:
        return f"Stream ID: {self.stream_id}, Type: {self.stream_type}"


# Concrete implementation for Sensor Data.
class SensorStream(DataStream):
    stream_type = "Environmental Data"

    # Polymorphism: Implementation specific to sensor data processing.
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            print(
                f"Processing sensor batch: [temp:{data_batch[0]}, "
                f"humidity:{data_batch[1]}, pressure:{data_batch[2]}]"
            )
            a = len(data_batch)
            return (
                f"Sensor analysis: {a} readings processed, "
                f"avg temp: {data_batch[0]}°C"
            )

        except Exception as e:
            return f"Error processing sensor batch: {e}"


# Concrete implementation for Financial Transactions.
class TransactionStream(DataStream):
    stream_type = "Financial Data"

    # Polymorphism: Implementation specific to transaction logic.
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            total_buy = 0
            total_sell = 0
            summary = []

            for item in data_batch:
                if isinstance(item, dict):
                    if "buy" in item:
                        total_buy += item["buy"]
                        summary.append(f"buy:{item['buy']}")
                    elif "sell" in item:
                        total_sell += item["sell"]
                        summary.append(f"sell:{item['sell']}")

            net_flow = total_buy - total_sell
            count = len(summary)

            print(f"Processing transaction batch: [{', '.join(summary)}]")

            return (
                f"Transaction analysis: {count} operations, "
                f"net flow: {net_flow:+d} units"
            )

        except Exception as e:
            return f"Error processing transaction batch: {e}"


# Concrete implementation for System Events.
class EventStream(DataStream):
    stream_type = "System Events"

    # Polymorphism: Implementation specific to event counting.
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            error = 0
            print(
                f"Processing event batch: [{data_batch[0]}, "
                f"{data_batch[1]}, {data_batch[2]}]"
            )
            for event in data_batch:
                if isinstance(event, str):
                    if event == "error":
                        error += 1
            total = len(data_batch)
            return (f"Event analysis: {total} events, "
                    f"{error} error detected")
        except Exception as e:
            return f"Error processing event batch: {e}"


# The Manager class that treats all streams uniformly.
class StreamProcessor():
    def __init__(self):
        # Polymorphic collection: Stores different types of DataStream objects.
        self.streams: Dict[str, DataStream] = {}

    def add_stream(self, stream: DataStream):
        self.streams[stream.stream_id] = stream

    # This method works with ANY DataStream subclass (Sensor, Transaction, etc)
    # because they all share the same interface (process_batch).
    def process_stream(self, stream_id: str, data_batch: List[Any]):
        if stream_id in self.streams:
            # Calls the implementation of process_batch for the object.
            return self.streams[stream_id].process_batch(data_batch)
        else:
            print("Error: stream ID not found")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    a = SensorStream("SENSOR_001")
    processor = StreamProcessor()
    processor.add_stream(a)
    sensor_data = [22.5, 65, 1013]
    print(a.get_stats())
    print(processor.process_stream("SENSOR_001", sensor_data))

    print("\nInitializing Transaction Stream...")
    b = TransactionStream("TRANS_001")
    processor.add_stream(b)
    trans_data = [{"buy": 100}, {"sell": 150}, {"buy": 75}]
    print(b.get_stats())
    print(processor.process_stream("TRANS_001", trans_data))

    print("\nInitializing Event Stream...")
    c = EventStream("EVENT_001")
    processor.add_stream(c)
    event_data = ["login", "error", "logout"]
    print(c.get_stats())
    print(processor.process_stream("EVENT_001", event_data))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    raw_sensor_data = [22.5, "reading_error", 65, 1013, "null"]

    # Retrieving the object as a generic DataStream
    sensor_obj = processor.streams["SENSOR_001"]
    # Using the shared method filter_data defined in the Base Class
    filtered_data = sensor_obj.filter_data(raw_sensor_data, criteria="numeric")

    print("Batch 1 Results:")
    print("- Sensor data: " +
          f"{processor.process_stream('SENSOR_001', filtered_data)}")

    print("\nStream filtering active: Numeric filter applied to Sensor Stream")
    print(f"Original data: {raw_sensor_data}")
    print(f"Filtered results: {filtered_data}")
    print("All streams processed successfully. Nexus throughput optimal.")
