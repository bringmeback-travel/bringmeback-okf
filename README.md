# bringmeback-okf

Contrat commun de **bringmeback-travel** : schémas, vocabulaires et règles de publication, sans données de voyage personnelles. Les deux autres dépôts portent les enregistrements :
- `bringmeback-content` (privé actuellement, contenu **publiable après validation**) ;
- `bringmeback-private` (privé durablement, données intimes et extensions privées).

**État du projet au 20 septembre 2026 :** les trois dépôts ne contenaient qu'un README initial. Ce commit introduit le *premier profil de projet* BringMeBack ; ce n'est pas une affirmation qu'une spécification OKF universelle a été adoptée. Le champ `okf_version: "0.2"` conserve la cible historique du projet ; `x-bringmeback.version: "1.0.0"` identifie séparément ce modèle évolutif. Voir [contrat](docs/contract.md), [séparation](docs/publication.md) et [modèles](templates/).

## Amsterdam pilote
- `bringmeback-content/content/destinations/nl/amsterdam/` : destination, lieux ordinaires, carnet et médias ;
- `bringmeback-private/content/destinations/nl/amsterdam/` : notes intimes, plateformes et lieux libertins ; Muiden et Zaandijk sont rangés sous leurs **propres villes**, non artificiellement dans Amsterdam.
- Identifiants stables `bmb:place:nl:amsterdam:rosalias-menagerie`, distincts des slugs et adresses.
- Aucun lien réciproque depuis le socle publiable vers l'overlay privé.

La connaissance structurée ne doit pas être confondue avec l'article WordPress ou la future interface Astro. Un article est une **projection éditoriale choisie**, jamais une exportation aveugle du dépôt.
