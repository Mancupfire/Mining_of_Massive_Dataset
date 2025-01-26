# Mapper
def map_function(record):
    id, name, age, salary = record.split(",")
    if int(age) > 28:  # Filter condition
        return (id, record)  # Emit key-value pair
    return None

# Reducer
def reduce_function(mapped_data):
    selected_records = []
    for key, value in mapped_data:
        if value is not None:
            selected_records.append(value)
    return selected_records

# Input Dataset
data = [
    "1, Alice, 30, 70000",
    "2, Bob, 45, 85000",
    "3, Charlie, 25, 50000",
    "4, David, 28, 60000"
]

# Map Phase
mapped_data = [map_function(record) for record in data]
mapped_data = [item for item in mapped_data if item]  # Remove None values

# Reduce Phase
output = reduce_function(mapped_data)

# Output Results
for record in output:
    print(record)
