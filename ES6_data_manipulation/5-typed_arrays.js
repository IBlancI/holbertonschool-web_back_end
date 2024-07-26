function createInt8TypedArray(length, position, value) {
  // Check if the position is valid
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }

  // Create a new ArrayBuffer
  const buffer = new ArrayBuffer(length);
  const int8View = new Int8Array(buffer); // Create Int8Array view of the buffer

  // Set the value at the specified position
  int8View[position] = value;

  // Return a DataView for the ArrayBuffer
  return new DataView(buffer);
}

export default createInt8TypedArray;
