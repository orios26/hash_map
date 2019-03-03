#hash map implementation using separate chaining collision implementation
class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]

  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code%self.array_size

  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key,value])
    list_at_array = self.array[array_index]
    for node in list_at_array:
      if key == node[0]:
        node[1] = value
        return
    list_at_array.insert(payload)


  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]
    for node in list_at_index:
      if key == node[0]:
        return node[1]
      else:
        return None
