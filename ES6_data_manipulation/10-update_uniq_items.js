function updateUniqueItems(groceries) {
  // Check if the argument is a Map
  if (!(groceries instanceof Map)) {
    throw new Error('Cannot process');
  }

  // Iterate over the Map entries
  for (const [item, quantity] of groceries) {
    // Update the quantity if it is 1
    if (quantity === 1) {
      groceries.set(item, 100);
    }
  }
  
  return groceries; // Return the updated Map
}

export default updateUniqueItems;
