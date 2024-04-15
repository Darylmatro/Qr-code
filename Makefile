# Définir le compilateur Python
PYTHON = python3

# Définir le nom du script
SCRIPT = src/main.py

# Définir le fichier de sortie
OUTPUT = myqr.png

# La cible par défaut qui est exécutée quand aucune cible n'est spécifiée
all: $(OUTPUT)

# Règle pour créer le fichier QR Code
$(OUTPUT): $(SCRIPT)
	$(PYTHON) $(SCRIPT)

# Règle pour nettoyer les fichiers générés
clean:
	rm -f $(OUTPUT)

# Règle pour exécuter le script sans créer de fichier de sortie dépendant
run:
	$(PYTHON) $(SCRIPT)
