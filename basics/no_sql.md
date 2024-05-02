Has flexible schemas that allow programmers to create and manage modern applications.
Do not use a traditional row/column table database design with fixed schemas.

# Types

key-value store
Document-based: Store ech record and its associated in a document, enable indexing.
Column-based: Data is stored in cells grouped as columns of data instead of rows
Graph-based

## Types de bases de données :

Les bases de données sont des outils essentiels pour stocker et organiser de grandes quantités de données. Elles sont utilisées dans divers domaines, du commerce de détail à la finance en passant par les soins de santé. 

Le choix du type de base de données adapté dépend de plusieurs facteurs, tels que le type de données à stocker, les requêtes à effectuer et les performances attendues. Voici quelques-uns des types de bases de données les plus courants :

**1. Bases de données clé-valeur (Key-Value)**

* **Fonctionnement:** Les bases de données clé-valeur stockent les données sous forme de paires clé-valeur, où la clé est un identifiant unique et la valeur est une donnée associée à la clé. Les paires clé-valeur ne sont pas structurées et ne sont pas liées entre elles.
* **Exemple:** Imaginez une base de données clé-valeur stockant des informations sur les utilisateurs d'un site Web. La clé pourrait être l'identifiant de l'utilisateur et la valeur pourrait être un objet JSON contenant le nom, l'adresse e-mail et d'autres informations de l'utilisateur.
* **Avantages:** Simples, évolutives, rapides pour les recherches par clé.
* **Inconvénients:** Manque de structure, requêtes complexes difficiles.

**2. Bases de données orientées document (Document-Based)**

* **Fonctionnement:** Les bases de données orientées document stockent les données sous forme de documents, qui sont des structures de données semi-structurées pouvant contenir du texte, des nombres, des tableaux et d'autres objets. Les documents sont stockés au format JSON ou BSON.
* **Exemple:** Imaginez une base de données orientée document stockant des articles de blog. Chaque article serait un document contenant le titre, le contenu, la date de publication et d'autres informations.
* **Avantages:** Flexibles, faciles à stocker des données non structurées, requêtes puissantes avec des documents imbriqués.
* **Inconvénients:** Peuvent être moins performantes pour les recherches par champs spécifiques.

**3. Bases de données orientées colonne (Column-Based)**

* **Fonctionnement:** Les bases de données orientées colonne stockent les données dans des tableaux où chaque colonne représente un attribut et chaque ligne représente un ensemble d'enregistrements. Les colonnes peuvent être compressées et indexées pour des performances optimales.
* **Exemple:** Imaginez une base de données orientée colonne stockant des données de vente. Chaque colonne pourrait représenter un attribut tel que le nom du produit, le prix, la quantité et la date de vente.
* **Avantages:** Compression efficace, accès rapide aux colonnes spécifiques, requêtes analytiques puissantes.
* **Inconvénients:** Moins flexibles pour les données non structurées, les mises à jour de lignes entières peuvent être moins efficaces.

**4. Bases de données orientées graphe (Graph-Based)**

* **Fonctionnement:** Les bases de données orientées graphe stockent les données sous forme de graphes, où les nœuds représentent des entités et les arêtes représentent les relations entre les entités. Les graphes peuvent être utilisés pour modéliser des relations complexes entre des données.
* **Exemple:** Imaginez une base de données orientée graphe stockant un réseau social. Les nœuds pourraient représenter des utilisateurs et les arêtes pourraient représenter des relations d'amitié.
* **Avantages:** Modélisation efficace des relations complexes, requêtes sur les chemins et les relations, exploration des données.
* **Inconvénients:** Plus complexes à modéliser et à interroger que les modèles relationnels.


En plus de ces types de bases de données courants, il existe d'autres types spécialisés, tels que les bases de données temporelles et les bases de données spatiales. Le choix du type de base de données adapté dépend des besoins spécifiques de chaque application.

**Il est important de noter que ce ne sont que des exemples de base de données et qu'il existe de nombreux autres systèmes disponibles.** Le choix du bon type de base de données pour votre application dépend de vos besoins spécifiques en matière de données et de performances.
