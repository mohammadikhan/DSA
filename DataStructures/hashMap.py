class HashMap:

    def __init__(self, size):
        self.size = size
        self.hashMap = self.createBuckets()

    def createBuckets(self):
        return [[] for _ in range(self.size)]
    
    def __str__(self):
        return "".join(str(item) for item in self.hashMap)
    
    # Inserting key-value pairs into HashMap
    def insert(self, key, val):
        
        # hash the key to get the index
        hashKey = hash(key) % self.size

        # Get the bucket that corresponds to the index
        bucket = self.hashMap[hashKey]

        keyFound = False
        for index, record in enumerate(bucket):
            recordKey, recordVal = record

            # Check to see if the bucket has the same key as the key that is being inserted
            if recordKey == key:
                keyFound = True
                break
        
        # If they bucket has the same value as the key to be inserted, we can update the keys value
        # Otherwise, add they key-value pair to the bucket

        if keyFound:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    def getValue(self, key):
        
        # Get the index from key
        hashKey = hash(key) % self.size

        # Get the bucket corresponding to the index
        bucket = self.hashMap[hashKey]

        keyFound = False

        for index, record in enumerate(bucket):
            recordKey, recordVal = record

            # Check if the bucket has the same key as the given key
            if recordKey == key:
                keyFound = True
                break

        # If the key was found, return its corresponding value, otherwise say that the record wasn't found
        if keyFound:
            return recordVal
        else:
            return "No record found"
        
    # Remove pair with specific key
    def delete(self, key):

        hashKey = hash(key) % self.size

        bucket = self.hashMap[hashKey]

        keyFound = False

        for index, record in enumerate(bucket):
            recordKey, recordVal = record

            if recordKey == key:
                keyFound = True
                break

        
        if keyFound:
            bucket.pop(index)
        else:
            return "Key does not exist in HashMap"

        return
    

if __name__=="__main__":

    # Create HashMap and insert key-value pairs into it
    hashMap = HashMap(5)
    hashMap.insert(1, "First Key")
    hashMap.insert(2, "Second Key")
    print(hashMap)

    # Get the value of the key 1
    print("Key 1 value: ", hashMap.getValue(1))

    # Update Key 2's value by calling insert on it again
    hashMap.insert(2, "Updated the second keys value")
    print("Updating the second keys value: ")
    print(hashMap)

    # Deleting Key 1
    hashMap.delete(1)
    print("HashMap after deleting key 1")
    print(hashMap)

    # Get the value for a key that doesn't exist in the HashMap
    print("Getting the value for Key 3: ", end="")
    print(hashMap.getValue(3))
    
    # Delete a key that doesn't exist in the HashMap
    print("Deleting Key 5: ", end="")
    print(hashMap.delete(5))