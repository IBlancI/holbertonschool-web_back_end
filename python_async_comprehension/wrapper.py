#!/usr/bin/env python3

import sys
import importlib
import asyncio

# Ajouter le répertoire du projet au chemin de recherche des modules
sys.path.append(".")

# Importer dynamiquement le module `1-async_comprehension`
async_comprehension_module = importlib.import_module('1-async_comprehension')
async_comprehension = async_comprehension_module.async_comprehension

# Fonction principale pour exécuter l'async comprehension
async def main():
    result = await async_comprehension()
    print(result)

# Exécuter la fonction principale
if __name__ == "__main__":
    asyncio.run(main())
